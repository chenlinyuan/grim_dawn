import os, shutil

mod = r'H:\SteamLibrary\steamapps\common\Grim Dawn\mods\StarterGodWeapon'
rec = os.path.join(mod, 'database', 'Records')

# 1. 删除旧的剑记录
sword = os.path.join(rec, 'Items', 'GearWeapons', 'Swords1h', 'item_startergodsword.dbr')
if os.path.exists(sword):
    os.remove(sword)
    print('removed old sword')
# 删除空的 GearWeapons 目录
gw = os.path.join(rec, 'Items', 'GearWeapons')
if os.path.exists(gw):
    shutil.rmtree(gw)
    print('removed GearWeapons dir')

# 2. 更新掉落表：把 item_startergodsword 换成 soul_ring
lcd = os.path.join(rec, 'Items', 'LootChests', 'ChestLootTables')
for name in ['chestloot_all_a01_lowercrossinga01', 'chestloot_all_a01_lowercrossingmelee',
             'chestloot_rackweapon_b01']:
    fp = os.path.join(lcd, name + '.dbr')
    if not os.path.exists(fp):
        continue
    t = open(fp, encoding='ascii').read()
    t2 = t.replace('records/items/gearweapons/swords1h/item_startergodsword.dbr',
                   'records/items/gearaccessories/rings/soul_ring.dbr')
    open(fp, 'w', encoding='ascii', newline='\n').write(t2)
    print('updated', name)

# intropotions 在 QuestChests
fp = os.path.join(rec, 'Items', 'LootChests', 'QuestChests', 'QuestChestLootTables', 'chestloot_intropotions.dbr')
if os.path.exists(fp):
    t = open(fp, encoding='ascii').read()
    t2 = t.replace('records/items/gearweapons/swords1h/item_startergodsword.dbr',
                   'records/items/gearaccessories/rings/soul_ring.dbr')
    open(fp, 'w', encoding='ascii', newline='\n').write(t2)
    print('updated chestloot_intropotions')

# 3. master table
fp = os.path.join(rec, 'Items', 'LootTables', 'MasterTables', 'mt_gearweapons_a01.dbr')
if os.path.exists(fp):
    t = open(fp, encoding='ascii').read()
    t2 = t.replace('records/items/gearweapons/swords1h/item_startergodsword.dbr',
                   'records/items/gearaccessories/rings/soul_ring.dbr')
    open(fp, 'w', encoding='ascii', newline='\n').write(t2)
    print('updated mt_gearweapons_a01')

print()
print('=== final records ===')
for root, dirs, files in os.walk(rec):
    for f in sorted(files):
        print(' ', os.path.relpath(os.path.join(root, f), rec))
