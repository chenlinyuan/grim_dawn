"""Full fresh automation: login -> Mod->Select->Mod -> Build->Build, monitor."""
import time, os
from pywinauto import Application, Desktop

GD = r"H:\SteamLibrary\steamapps\common\Grim Dawn"
MOD = "StarterGodWeapon"

def log(*a): print(*a, flush=True)

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

def status(win):
    try:
        return win.child_window(class_name='msctls_statusbar32').texts()
    except Exception:
        return ["err"]

def main():
    os.system('taskkill /F /IM AssetManager.exe >nul 2>&1')
    time.sleep(1.5)
    app = Application(backend="win32").start(os.path.join(GD, "AssetManager.exe"), work_dir=GD)
    time.sleep(6)
    try:
        dlg = app.window(title="Asset Manager Login")
        if dlg.exists(timeout=6):
            dlg.set_focus(); time.sleep(0.4)
            dlg.child_window(title="Work Offline").click_input()
            time.sleep(2.5)
    except Exception as e:
        log("login:", e)
    win = app.window(title="Asset Manager")
    win.wait("exists visible", timeout=15)
    win.set_focus(); time.sleep(1.2)

    log("status0:", status(win))
    menu = win.menu()
    find_item(menu, "Mod").click_input(); time.sleep(1.0)
    ps = popups()
    log("popups after Mod:", [p.window_text() for p in ps])
    find_item(ps[0].menu(), "Select").click_input(); time.sleep(1.2)
    ps2 = popups()
    target = None
    for p in ps2:
        it = find_item(p.menu(), MOD)
        if it: target = it; break
    log("selecting:", target)
    target.click_input(); time.sleep(2.5)
    log("status after select:", status(win))

    win.set_focus(); time.sleep(0.8)
    menu = win.menu()
    find_item(menu, "Build").click_input(); time.sleep(1.2)
    ps3 = popups()
    bld = None
    for p in ps3:
        it = find_item(p.menu(), "Build")
        if it: bld = it; break
    log("build item:", bld)
    bld.click_input()

    for i in range(16):
        time.sleep(1.5)
        log(f"  t={i*1.5:.0f}s {status(win)}")
        for w in Desktop(backend="win32").windows():
            try:
                if w.is_visible() and w.class_name() == "#32770":
                    log("  DIALOG:", repr(w.window_text()))
                    for c in w.children():
                        if c.window_text():
                            log("     ", c.class_name(), repr(c.window_text()))
            except Exception:
                pass
    log("final:", status(win))
    log("done")

if __name__ == "__main__":
    main()
