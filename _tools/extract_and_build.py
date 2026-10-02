"""Extract Game Files via Tools menu, then build the mod. Safe builddir."""
import time, os, struct
from pywinauto import Application, Desktop

GD = r"H:\SteamLibrary\steamapps\common\Grim Dawn"
MOD = "StarterGodWeapon"

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

def dialogs():
    return [w for w in Desktop(backend="win32").windows() if w.is_visible() and w.class_name() == "#32770"]

def status(win):
    try:
        return win.child_window(class_name='msctls_statusbar32').texts()
    except Exception:
        return ["err"]

def open_menu(win, name, retries=4):
    for _ in range(retries):
        win.set_focus(); time.sleep(0.6)
        try:
            menu = win.menu()
            it = find_item(menu, name)
            if it:
                it.click_input(); time.sleep(1.3)
                ps = popups()
                if ps:
                    return ps[0].menu()
        except Exception as e:
            log("open_menu err:", e)
        time.sleep(0.8)
    return None

def main():
    os.system('taskkill /F /IM AssetManager.exe >nul 2>&1'); time.sleep(1.5)
    app = Application(backend="win32").start(os.path.join(GD, "AssetManager.exe"), work_dir=GD)
    time.sleep(7)
    try:
        dlg = app.window(title="Asset Manager Login")
        if dlg.exists(timeout=8):
            dlg.set_focus(); time.sleep(0.5)
            dlg.child_window(title="Work Offline").click_input(); time.sleep(3)
    except Exception as e:
        log("login:", e)
    win = app.window(title="Asset Manager")
    win.wait("exists visible", timeout=20); win.set_focus(); time.sleep(1.5)

    # Tools -> Extract Game Files
    tm = open_menu(win, "Tools")
    log("tools menu:", [str(i) for i in tm.items()] if tm else None)
    eg = find_item(tm, "Extract Game Files")
    log("extract item:", eg)
    eg.click_input(); time.sleep(4)
    ds = dialogs()
    log("dialogs after extract:", [d.window_text() for d in ds])
    for d in ds:
        for c in d.descendants():
            if c.window_text():
                log("   ", c.class_name(), repr(c.window_text()))
    log("done")

if __name__ == "__main__":
    main()
