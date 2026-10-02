"""Build with dialog handling."""
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

def handle_dialogs():
    n = 0
    for w in Desktop(backend="win32").windows():
        try:
            if w.is_visible() and w.class_name() == "#32770":
                txt = w.window_text()
                log("  dialog:", repr(txt))
                # click "No To All" if present, else "No"
                for label in ("No To All", "No", "OK"):
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

def main():
    win = None
    for w in Desktop(backend="win32").windows():
        try:
            if w.window_text() == "Asset Manager" and w.class_name().startswith("Afx"):
                win = w
        except Exception:
            pass
    if win is None:
        log("AssetManager main window not found; launching")
        os.system('taskkill /F /IM AssetManager.exe >nul 2>&1'); time.sleep(1.5)
        app = Application(backend="win32").start(os.path.join(GD, "AssetManager.exe"), work_dir=GD)
        time.sleep(6)
        try:
            dlg = app.window(title="Asset Manager Login")
            if dlg.exists(timeout=6):
                dlg.set_focus(); time.sleep(0.4)
                dlg.child_window(title="Work Offline").click_input(); time.sleep(2.5)
        except Exception as e:
            log("login:", e)
        win = app.window(title="Asset Manager")
        win.wait("exists visible", timeout=15)
    win.set_focus(); time.sleep(1)

    # clear any pending dialogs first
    handle_dialogs()

    menu = win.menu()
    find_item(menu, "Build").click_input(); time.sleep(1.2)
    ps3 = popups()
    bld = None
    for p in ps3:
        it = find_item(p.menu(), "Build")
        if it: bld = it; break
    log("build item:", bld)
    bld.click_input()

    for i in range(40):
        time.sleep(1.0)
        n = handle_dialogs()
        s = status(win)
        if i % 3 == 0:
            log(f"  t={i}s {s} dialogs={n}")
    log("final:", status(win))
    log("done")

if __name__ == "__main__":
    main()
