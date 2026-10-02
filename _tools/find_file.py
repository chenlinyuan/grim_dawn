import os
ROOT = r'H:\SteamLibrary\steamapps\common\Grim Dawn\Working\database\records'
target = 'chestloot_all_b01.dbr'
for dp, dn, fn in os.walk(ROOT):
    for f in fn:
        if f.lower() == target.lower():
            print(os.path.join(dp, f).replace(ROOT + '\\', ''))
