"""Import records via Database->Import Record, then build."""
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

def dialogs():
    return [w for w in Desktop(backend="win32").windows() if w.is_visible() and w.class_name() == "#32770"]

def main():
    app = Application(backend="win32").connect(title="Asset Manager")
    win = app.window(title="Asset Manager")
    win.set_focus(); time.sleep(1.0)

    # ensure mod selected
    menu = win.menu()
    find_item(menu, "Mod").click_input(); time.sleep(1.2)
    ps = popups()
    find_item(ps[0].menu(), "Select").click_input(); time.sleep(1.5)
    ps2 = popups()
    tgt = None
    for p in ps2:
        it = find_item(p.menu(), MOD)
        if it: tgt = it; break
    if tgt:
        tgt.click_input(); time.sleep(2.5)
        log("selected mod")
    else:
        log("mod not in select list")

    # Database -> Import Record
    win.set_focus(); time.sleep(0.8)
    menu = win.menu()
    find_item(menu, "Database").click_input(); time.sleep(1.5)
    ps = popups()
    log("db popups:", len(ps))
    if not ps:
        log("db menu did not open")
        return
    for it in ps[0].menu().items():
        log("   db item:", it)
    ir = find_item(ps[0].menu(), "Import Record")
    if ir is None:
        log("no Import Record")
        return
    ir.click_input(); time.sleep(3)
    ds = dialogs()
    log("dialogs after import:", [d.window_text() for d in ds])
    for d in ds:
        for c in d.descendants():
            if c.window_text():
                log("   ", c.class_name(), repr(c.window_text()))

if __name__ == "__main__":
    main()
