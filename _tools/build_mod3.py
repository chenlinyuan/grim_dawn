"""Fully automate: Mod -> Select -> StarterGodWeapon -> Build -> Build."""
import sys, time, os
from pywinauto import Application, Desktop

GD = r"H:\SteamLibrary\steamapps\common\Grim Dawn"
MOD = "StarterGodWeapon"

def log(*a): print(*a, flush=True)

def dismiss_login(app):
    try:
        dlg = app.window(title="Asset Manager Login")
        if dlg.exists(timeout=6):
            dlg.set_focus(); time.sleep(0.4)
            dlg.child_window(title="Work Offline").click_input()
            time.sleep(2)
    except Exception as e:
        log("login:", e)

def popups():
    res = []
    for w in Desktop(backend="win32").windows():
        try:
            if w.is_visible() and w.class_name() == "#32768":
                res.append(w)
        except Exception:
            pass
    return res

def find_item(menu, name):
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
    dismiss_login(app); time.sleep(2)
    win = app.window(title="Asset Manager")
    win.wait("exists visible", timeout=15)
    win.set_focus(); time.sleep(1)

    menu = win.menu()
    # Mod -> Select -> StarterGodWeapon
    find_item(menu, "Mod").click_input(); time.sleep(1.0)
    ps = popups()
    log("popups after Mod:", len(ps))
    sel = find_item(ps[0].menu(), "Select")
    sel.click_input(); time.sleep(1.2)
    ps2 = popups()
    log("popups after Select:", len(ps2))
    # find the submenu containing StarterGodWeapon
    target = None
    for p in ps2:
        it = find_item(p.menu(), MOD)
        if it:
            target = it; break
    if not target:
        log("ERROR: mod item not found")
        return
    log("clicking", target)
    target.click_input(); time.sleep(2.5)

    # Now Build -> Build
    win.set_focus(); time.sleep(0.5)
    menu = win.menu()
    b = find_item(menu, "Build")
    log("Build menu:", b)
    b.click_input(); time.sleep(1.2)
    ps3 = popups()
    log("popups after Build:", len(ps3))
    for p in ps3:
        for it in p.menu().items():
            log("   build item:", it)
    bld = None
    for p in ps3:
        it = find_item(p.menu(), "Build")
        if it:
            bld = it; break
    if bld:
        log("clicking Build ->", bld)
        bld.click_input()
        log("build started, waiting...")
        time.sleep(30)
    else:
        log("Build item not found")

    log("done")

if __name__ == "__main__":
    main()
