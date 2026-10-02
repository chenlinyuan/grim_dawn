"""Complete AssetManager automation: launch -> offline -> select mod -> build -> verify."""
import time, os, struct
from pywinauto import Application, Desktop

GD = r"H:\SteamLibrary\steamapps\common\Grim Dawn"
MOD = "StarterGodWeapon"
ARZ = os.path.join(GD, "mods", MOD, "database", MOD + ".arz")

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

def handle_dialogs():
    n = 0
    for w in Desktop(backend="win32").windows():
        try:
            if w.is_visible() and w.class_name() == "#32770":
                log("  dialog:", repr(w.window_text()))
                for label in ("No To All", "No", "Yes To All", "Yes", "OK"):
                    try:
                        b = w.child_window(title=label, class_name="Button")
                        if b.exists():
                            b.click_input(); n += 1
                            log(f"    clicked '{label}'")
                            break
                    except Exception:
                        pass
        except Exception:
            pass
    return n

def arz_info():
    if not os.path.exists(ARZ):
        return "no arz"
    d = open(ARZ, 'rb').read()
    ver, off1, c1, c2, off2, sz2, flags, x = struct.unpack_from('<IIIIIIII', d, 0)
    return f"size={len(d)} strings={c1} files={c2}"

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
    log("initial status:", status(win))

    # --- Mod -> Select -> MOD ---
    menu = win.menu()
    m = find_item(menu, "Mod")
    log("Mod item:", m)
    m.click_input(); time.sleep(1.2)
    ps = popups()
    log("popups after Mod:", len(ps))
    sel = find_item(ps[0].menu(), "Select")
    log("Select item:", sel)
    sel.click_input(); time.sleep(1.5)
    ps2 = popups()
    target = None
    for p in ps2:
        it = find_item(p.menu(), MOD)
        if it: target = it; break
    log("mod item:", target)
    if target is None:
        log("FAILED to find mod in Select submenu")
        return
    target.click_input(); time.sleep(3)
    log("status after select:", status(win))

    # --- Build -> Build ---
    win.set_focus(); time.sleep(1)
    menu = win.menu()
    b = find_item(menu, "Build")
    b.click_input(); time.sleep(1.5)
    ps3 = popups()
    bld = None
    for p in ps3:
        it = find_item(p.menu(), "Build")
        if it: bld = it; break
    log("build item:", bld)
    if bld is None:
        log("FAILED to find Build item")
        return
    bld.click_input()

    # monitor
    for i in range(30):
        time.sleep(1.0)
        handle_dialogs()
        s = status(win)
        if i % 2 == 0:
            log(f"  t={i}s {s}")
    handle_dialogs()
    log("final status:", status(win))
    log("ARZ:", arz_info())

if __name__ == "__main__":
    main()
