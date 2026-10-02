"""Extract Game Files: navigate folder tree by typing full path."""
import time, os
from pywinauto import Application, Desktop
from pywinauto.keyboard import send_keys

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
        log("no folder dialog")
        return
    log("folder dialog found")
    tv = [c for c in w.descendants() if c.class_name() == "SysTreeView32"][0]
    tv.set_focus(); time.sleep(0.8)
    # Type the full path char-by-char (shell tree auto-completes)
    for ch in GD:
        send_keys(ch, pause=0.02)
        time.sleep(0.03)
    time.sleep(2.0)
    send_keys("{ENTER}", pause=0.05); time.sleep(2.0)
    w = dlg("浏览文件夹")
    log("dialog still open after enter:", w is not None)
    if w:
        # click OK
        for c in w.descendants():
            if c.window_text() == "确定":
                c.click_input(); log("clicked OK"); break
        time.sleep(2)
    c = dlg("Confirm")
    if c:
        for x in c.descendants():
            if "是" in x.window_text():
                x.click_input(); log("confirmed"); break
    log("extraction started; waiting 120s")
    for i in range(40):
        time.sleep(3)
        ds = [d for d in Desktop(backend="win32").windows() if d.is_visible() and d.class_name() == "#32770" and d.window_text() != "Asset Manager Login"]
        if ds:
            log(f"  t={i*3}s dialogs:", [d.window_text() for d in ds])
    log("done")

if __name__ == "__main__":
    main()
