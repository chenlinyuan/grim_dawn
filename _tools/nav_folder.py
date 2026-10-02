"""Navigate the Select Game Folder tree dialog."""
import time
from pywinauto import Desktop
from pywinauto.keyboard import send_keys

def log(*a): print(*a, flush=True)

def find_dlg():
    for w in Desktop(backend="win32").windows():
        try:
            if w.is_visible() and w.window_text() == "浏览文件夹":
                return w
        except Exception:
            pass
    return None

def main():
    w = find_dlg()
    if not w:
        log("no folder dialog")
        return
    tv = [c for c in w.descendants() if c.class_name() == "SysTreeView32"][0]
    log("tree rect:", tv.rectangle())
    tv.set_focus(); time.sleep(0.6)
    # Type the full path into the tree (shell dialogs support this)
    send_keys("H", pause=0.05); time.sleep(1.2)
    send_keys("{ENTER}", pause=0.05); time.sleep(1.5)
    log("after H+Enter, dialog still open:", find_dlg() is not None)
    # If still open, try typing the rest
    w2 = find_dlg()
    if w2:
        tv2 = [c for c in w2.descendants() if c.class_name() == "SysTreeView32"][0]
        tv2.set_focus(); time.sleep(0.5)
        send_keys("SteamLibrary", pause=0.03); time.sleep(1.0)
        send_keys("{ENTER}", pause=0.05); time.sleep(1.2)
        log("after SteamLibrary:", find_dlg() is not None)

if __name__ == "__main__":
    main()
