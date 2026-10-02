"""Import the loot table record into AssetManager, then build."""
import os, time
from pywinauto import Application, Desktop

GD = r"H:\SteamLibrary\steamapps\common\Grim Dawn"
MOD = "StarterGodWeapon"
LT = os.path.join(GD, "mods", MOD, "database", "Records", "Items", "LootChests", "ChestLootTables", "chestloot_all_a01_lowercrossinga01.dbr")

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

def open_menu(win, name, retries=5):
    for _ in range(retries):
        win.set_focus(); time.sleep(0.6)
        try:
            menu = win.menu()
            it = find_item(menu, name)
            if it:
                it.click_input(); time.sleep(1.4)
                ps = popups()
                if ps:
                    return ps[0].menu()
        except Exception as e:
            log("menu err:", e)
        time.sleep(0.8)
    return None

def main():
    app = Application(backend="win32").connect(title="Asset Manager")
    win = app.window(title="Asset Manager")
    win.set_focus(); time.sleep(1.2)

    m = open_menu(win, "Database")
    log("db menu:", [str(i) for i in m.items()] if m else None)
    ir = find_item(m, "Import Record")
    log("import item:", ir)
    ir.click_input(); time.sleep(3.5)
    # Select File dialog
    done = False
    for w in Desktop(backend="win32").windows():
        try:
            if w.is_visible() and w.window_text() == "Select File":
                e = [c for c in w.descendants() if c.class_name() == "Edit"][0]
                e.set_edit_text(LT); time.sleep(1.0)
                [c for c in w.descendants() if c.window_text() == "OK"][0].click_input()
                done = True; log("submitted path")
        except Exception as ex:
            log("selectfile err:", ex)
    time.sleep(3)
    for w in Desktop(backend="win32").windows():
        try:
            if w.is_visible() and w.class_name() == "#32770":
                log("dialog:", repr(w.window_text()), [c.window_text() for c in w.descendants() if c.window_text()])
                for c in w.descendants():
                    if c.window_text() in ("确定", "OK"):
                        c.click_input(); break
        except Exception:
            pass
    log("done")

if __name__ == "__main__":
    main()
