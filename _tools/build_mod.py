"""Automate Grim Dawn AssetManager to build the StarterGodWeapon mod."""
import sys, time, os
from pywinauto import Application, Desktop

GD = r"H:\SteamLibrary\steamapps\common\Grim Dawn"
MOD = "StarterGodWeapon"

def log(*a):
    print(*a, flush=True)

def dismiss_login(app):
    try:
        dlg = app.window(title="Asset Manager Login")
        if dlg.exists(timeout=6):
            log("login dialog found; clicking Work Offline")
            dlg.set_focus(); time.sleep(0.4)
            btn = dlg.child_window(title="Work Offline")
            btn.click_input()
            time.sleep(2)
            return True
    except Exception as e:
        log("login handling:", e)
    return False

def dump_popups(tag=""):
    for w in Desktop(backend="win32").windows():
        try:
            if w.is_visible() and w.class_name() == "#32768":
                log(f"{tag} POPUP '{w.window_text()}'")
                try:
                    for it in w.menu().items():
                        log("     ", it)
                except Exception as e:
                    log("      (menu err)", e)
        except Exception:
            pass

def main():
    os.system('taskkill /F /IM AssetManager.exe >nul 2>&1')
    time.sleep(1)
    app = Application(backend="win32").start(os.path.join(GD, "AssetManager.exe"), work_dir=GD)
    time.sleep(6)
    dismiss_login(app)
    time.sleep(2)

    win = app.window(title="Asset Manager")
    win.wait("exists visible", timeout=15)
    win.set_focus(); time.sleep(0.8)

    menu = win.menu()
    log("menu:", [str(i) for i in menu.items()])

    # click Mod (index 2)
    for idx in range(menu.item_count()):
        it = menu.item(idx)
        log(f"  item[{idx}] = {it}")
        if "Mod" in str(it):
            it.click_input()
            log("clicked Mod")
            break
    time.sleep(1.2)
    dump_popups("MOD")

    log("done")

if __name__ == "__main__":
    main()
