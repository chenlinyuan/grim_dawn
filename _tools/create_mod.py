"""Create mod via Mod->New with name, then verify structure."""
import time, os
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

    menu = win.menu()
    find_item(menu, "Mod").click_input(); time.sleep(1.2)
    ps = popups()
    find_item(ps[0].menu(), "New").click_input(); time.sleep(2.5)

    # Fill the New Mod dialog
    dlg = None
    for w in Desktop(backend="win32").windows():
        try:
            if w.is_visible() and w.window_text() == "New Mod":
                dlg = w
        except Exception:
            pass
    if not dlg:
        log("New Mod dialog not found")
        return
    log("filling mod name:", MOD)
    edits = [c for c in dlg.descendants() if c.class_name() == "Edit"]
    log("edits:", [c.window_text() for c in edits])
    # first edit = name, second = root dir
    name_edit = edits[0]
    name_edit.set_edit_text(MOD)
    time.sleep(0.8)
    ok = [c for c in dlg.descendants() if c.window_text() == "OK"][0]
    ok.click_input()
    time.sleep(3)

    # handle any confirmation
    for w in Desktop(backend="win32").windows():
        try:
            if w.is_visible() and w.class_name() == "#32770" and w.window_text() != "New Mod":
                log("confirm dialog:", repr(w.window_text()))
                for c in w.children():
                    if c.window_text():
                        log("   ", c.class_name(), repr(c.window_text()))
        except Exception:
            pass

    log("=== resulting structure ===")
    for root in (os.path.join(GD, "Working", "mods", MOD), os.path.join(GD, "mods", MOD)):
        log("--", root, "exists:", os.path.isdir(root))
        if os.path.isdir(root):
            for dp, dn, fn in os.walk(root):
                for f in fn:
                    log("   ", os.path.join(dp, f).replace(root + "\\", ""))
    log("done")

if __name__ == "__main__":
    main()
