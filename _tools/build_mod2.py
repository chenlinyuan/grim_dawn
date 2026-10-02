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
            log("login found -> Work Offline")
            dlg.set_focus(); time.sleep(0.4)
            dlg.child_window(title="Work Offline").click_input()
            time.sleep(2)
    except Exception as e:
        log("login:", e)

def popup():
    for w in Desktop(backend="win32").windows():
        try:
            if w.is_visible() and w.class_name() == "#32768":
                return w
        except Exception:
            pass
    return None

def menu_item(menu, name):
    for i in range(menu.item_count()):
        it = menu.item(i)
        if name.lower() in str(it).lower():
            return it
    return None

def main():
    os.system('taskkill /F /IM AssetManager.exe >nul 2>&1')
    time.sleep(1)
    app = Application(backend="win32").start(os.path.join(GD, "AssetManager.exe"), work_dir=GD)
    time.sleep(6)
    dismiss_login(app)
    time.sleep(2)

    win = app.window(title="Asset Manager")
    win.wait("exists visible", timeout=15)
    win.set_focus(); time.sleep(1)

    menu = win.menu()
    # Mod -> Select
    menu_item(menu, "Mod").click_input()
    time.sleep(1.0)
    p = popup()
    log("Mod popup:", p.window_text() if p else None)
    sel = menu_item(p.menu(), "Select")
    log("Select item:", sel)
    sel.click_input()
    time.sleep(1.5)

    # A submenu / dialog should appear listing mods. Dump popups + windows.
    log("--- after Select ---")
    for w in Desktop(backend="win32").windows():
        try:
            if w.is_visible():
                cn = w.class_name(); t = w.window_text()
                if cn == "#32768" or "Select" in t or "Mod" in t:
                    log(f"  win '{t}' class={cn}")
                    if cn == "#32768":
                        for it in w.menu().items():
                            log("      ", it)
        except Exception:
            pass

    log("done")

if __name__ == "__main__":
    main()
