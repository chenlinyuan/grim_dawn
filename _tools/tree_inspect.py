"""Inspect the folder dialog tree items to navigate reliably."""
import time, os
from pywinauto import Application, Desktop

GD = r"H:\SteamLibrary\steamapps\common\Grim Dawn"

def log(*a): print(*a, flush=True)

def popups():
    return [w for w in Desktop(backend="win32").windows() if w.is_visible() and w.class_name() == "#32768"]

def find_item(menu, name):
    try:
        for i in range(menu.item_count()):
            it = menu.item(i)
            if name.lower() in str(it).lower():
                return it
    except Exception:
        pass
    return None

def dlg(t):
    for w in Desktop(backend="win32").windows():
        try:
            if w.is_visible() and w.window_text() == t:
                return w
        except Exception:
            pass
    return None

def main():
    os.system('taskkill /F /IM AssetManager.exe >nul 2>&1'); time.sleep(2)
    app = Application(backend="win32").start(os.path.join(GD, "AssetManager.exe"), work_dir=GD)
    time.sleep(8)
    try:
        d = app.window(title="Asset Manager Login")
        if d.exists(timeout=8):
            d.set_focus(); time.sleep(0.5)
            d.child_window(title="Work Offline").click_input(); time.sleep(3)
    except Exception as e:
        log("login:", e)
    win = app.window(title="Asset Manager")
    win.wait("exists visible", timeout=20); win.set_focus(); time.sleep(2)
    menu = win.menu(); find_item(menu, "Tools").click_input(); time.sleep(1.5)
    ps = popups()
    find_item(ps[0].menu(), "Extract Game Files").click_input(); time.sleep(3.5)

    w = dlg("浏览文件夹")
    if not w:
        log("no dialog"); return
    tv = [c for c in w.descendants() if c.class_name() == "SysTreeView32"][0]
    log("tree handle:", tv.handle)
    # Enumerate root items using win32 tree API
    import ctypes
    from ctypes import wintypes
    TVM_GETNEXTITEM = 0x110A
    TVGN_ROOT = 0x0000
    TVGN_NEXT = 0x0001
    TVGN_CHILD = 0x0004
    TVM_GETITEMTEXTW = 0x1132
    user32 = ctypes.windll.user32
    # Use SendMessage to get root
    root = user32.SendMessageW(tv.handle, TVM_GETNEXTITEM, TVGN_ROOT, 0)
    log("root item:", root)
    # iterate siblings
    cur = root
    items = []
    while cur:
        items.append(cur)
        cur = user32.SendMessageW(tv.handle, TVM_GETNEXTITEM, TVGN_NEXT, cur)
    log("root count:", len(items))
    # get text of each
    class TVITEM(ctypes.Structure):
        _fields_ = [("mask", wintypes.UINT), ("hItem", ctypes.c_void_p),
                    ("state", wintypes.UINT), ("stateMask", wintypes.UINT),
                    ("pszText", ctypes.c_void_p), ("cchTextMax", ctypes.c_int),
                    ("iImage", ctypes.c_int), ("iSelectedImage", ctypes.c_int),
                    ("cChildren", ctypes.c_int), ("lParam", ctypes.c_void_p)]
    TVIF_TEXT = 0x0001
    for h in items:
        buf = ctypes.create_unicode_buffer(260)
        ti = TVITEM()
        ti.mask = TVIF_TEXT
        ti.hItem = h
        ti.pszText = ctypes.cast(buf, ctypes.c_void_p)
        ti.cchTextMax = 260
        user32.SendMessageW(tv.handle, TVM_GETITEMTEXTW, h, ctypes.byref(ti))
        log("  root item:", repr(buf.value))
    log("done")

if __name__ == "__main__":
    main()
