"""Create mod fresh via Mod->New, then copy records, then build."""
import time, os, shutil, struct
from pywinauto import Application, Desktop

GD = r"H:\SteamLibrary\steamapps\common\Grim Dawn"
MOD = "StarterGodWeapon"
WORK = os.path.join(GD, "Working", "mods", MOD)
SRC_RECORDS = os.path.join(GD, "mods", MOD, "database", "Records")

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

def status(win):
    try:
        return win.child_window(class_name='msctls_statusbar32').texts()
    except Exception:
        return ["err"]

def dialogs():
    res = []
    for w in Desktop(backend="win32").windows():
        try:
            if w.is_visible() and w.class_name() == "#32770":
                res.append(w)
        except Exception:
            pass
    return res

def main():
    os.system('taskkill /F /IM AssetManager.exe >nul 2>&1')
    time.sleep(1.5)
    app = Application(backend="win32").start(os.path.join(GD, "AssetManager.exe"), work_dir=GD)
    time.sleep(7)
    try:
        dlg = app.window(title="Asset Manager Login")
        if dlg.exists(timeout=8):
            dlg.set_focus(); time.sleep(0.5)
            dlg.child_window(title="Work Offline").click_input()
            time.sleep(3)
    except Exception as e:
        log("login:", e)
    win = app.window(title="Asset Manager")
    win.wait("exists visible", timeout=20)
    win.set_focus(); time.sleep(1.5)

    # Mod -> New
    menu = win.menu()
    find_item(menu, "Mod").click_input(); time.sleep(1.2)
    ps = popups()
    newit = find_item(ps[0].menu(), "New")
    log("New item:", newit)
    newit.click_input(); time.sleep(2.5)

    # A "New Mod" dialog should appear
    dlg = None
    for w in dialogs():
        log("dialog:", repr(w.window_text()))
        for c in w.children():
            if c.window_text():
                log("   ", c.class_name(), repr(c.window_text()))
        dlg = w
    log("done")

if __name__ == "__main__":
    main()
