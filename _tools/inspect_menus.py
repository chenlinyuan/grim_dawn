"""Inspect Build menu and try building assets."""
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
    win.wait("exists visible", timeout=20); win.set_focus(); time.sleep(2)

    for menu_name in ("Build", "Tools", "Mod"):
        win.set_focus(); time.sleep(0.8)
        menu = win.menu()
        it = find_item(menu, menu_name)
        log(f"--- {menu_name} menu ---")
        it.click_input(); time.sleep(1.5)
        ps = popups()
        for p in ps:
            for sub in p.menu().items():
                log("   ", sub)
        # close menu
        from pywinauto.keyboard import send_keys
        send_keys("{ESC}"); time.sleep(0.8)
    log("done")

if __name__ == "__main__":
    main()
