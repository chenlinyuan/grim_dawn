"""Extract Game Files with careful folder navigation."""
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

def dlg_by_title(t):
    for w in Desktop(backend="win32").windows():
        try:
            if w.is_visible() and w.window_text() == t:
                return w
        except Exception:
            pass
    return None

def any_dialog():
    res = []
    for w in Desktop(backend="win32").windows():
        try:
            if w.is_visible() and w.class_name() == "#32770":
                res.append(w)
        except Exception:
            pass
    return res

def main():
    os.system('taskkill /F /IM AssetManager.exe >nul 2>&1'); time.sleep(1.5)
    app = Application(backend="win32").start(os.path.join(GD, "AssetManager.exe"), work_dir=GD)
    time.sleep(7)
    try:
        d = app.window(title="Asset Manager Login")
        if d.exists(timeout=8):
            d.set_focus(); time.sleep(0.5)
            d.child_window(title="Work Offline").click_input(); time.sleep(3)
    except Exception as e:
        log("login:", e)
    win = app.window(title="Asset Manager")
    win.wait("exists visible", timeout=20); win.set_focus(); time.sleep(1.5)

    # Tools -> Extract Game Files
    menu = win.menu(); find_item(menu, "Tools").click_input(); time.sleep(1.3)
    ps = popups()
    find_item(ps[0].menu(), "Extract Game Files").click_input(); time.sleep(3)

    # Folder dialog
    w = dlg_by_title("浏览文件夹")
    if not w:
        log("no folder dialog; dialogs:", [d.window_text() for d in any_dialog()])
        return
    log("folder dialog found")
    tv = [c for c in w.descendants() if c.class_name() == "SysTreeView32"][0]
    tv.set_focus(); time.sleep(0.6)
    # Type full path into the tree (shell tree supports typing full path)
    send_keys("H", pause=0.05); time.sleep(1.0)
    send_keys("{ENTER}", pause=0.05); time.sleep(1.2)
    # Now navigate down
    for part in ["SteamLibrary", "steamapps", "common", "Grim Dawn"]:
        w = dlg_by_title("浏览文件夹")
        if not w:
            log("dialog closed early after", part)
            break
        tv = [c for c in w.descendants() if c.class_name() == "SysTreeView32"][0]
        tv.set_focus(); time.sleep(0.4)
        send_keys(part, pause=0.03); time.sleep(0.8)
        send_keys("{ENTER}", pause=0.05); time.sleep(1.0)
        log("navigated to", part)
    # Click OK
    w = dlg_by_title("浏览文件夹")
    if w:
        for c in w.descendants():
            if c.window_text() == "确定":
                c.click_input(); log("clicked OK"); break
    time.sleep(3)
    # Confirm
    c = dlg_by_title("Confirm")
    if c:
        for x in c.descendants():
            if "是" in x.window_text():
                x.click_input(); log("confirmed extraction"); break
    log("waiting for extraction...")
    for i in range(40):
        time.sleep(3)
        ds = any_dialog()
        if ds:
            log(f"  t={i*3}s dialog:", [d.window_text() for d in ds])
            for d in ds:
                log("     ", [c.window_text() for c in d.descendants() if c.window_text()])
        else:
            log(f"  t={i*3}s no dialog (extraction running or done)")
    log("done")

if __name__ == "__main__":
    main()
