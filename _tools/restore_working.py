import os

mod = r'H:\SteamLibrary\steamapps\common\Grim Dawn\mods\StarterGodWeapon'
ex = r'c:\Users\Administrator\Desktop\工作项目\Work\Grim Dawn\_gd_extract\db\records'
rec = os.path.join(mod, 'database', 'Records')

# 1. 删除成功版本里没有的：b013a 覆盖、lt_starterlegendaries
for rel in ['Items/GearWeapons/Melee2h/b013a_sword2h.dbr',
            'Items/LootTables/Weapons/lt_starterlegendaries.dbr']:
    p = os.path.join(rec, rel.replace('/', os.sep))
    if os.path.exists(p):
        os.remove(p)
        print('removed', rel)

# 清空目录
for root, dirs, files in os.walk(rec, topdown=False):
    if not os.listdir(root):
        os.rmdir(root)

def write_lf(rel, text):
    p = os.path.join(rec, rel.replace('/', os.sep))
    os.makedirs(os.path.dirname(p), exist_ok=True)
    open(p, 'w', encoding='ascii', newline='\n').write(text)
    print('wrote', rel, len(text), 'bytes')

# 2. chestloot_rackweapon_b01: 原版 + loot2Name2=item + loot2Weight2=100
t = open(os.path.join(ex, 'items', 'lootchests', 'chestloottables', 'chestloot_rackweapon_b01.dbr'),
         encoding='utf-8', errors='replace').read()
lines = t.splitlines()
out = []
for ln in lines:
    if ln.startswith('loot2Name1,'):
        out.append(ln)
        out.append('loot2Name2,records/items/gearweapons/swords1h/item_startergodsword.dbr,')
    elif ln.startswith('loot2Weight1,'):
        out.append('loot2Weight1,100,')
        out.append('loot2Weight2,100,')
    elif ln.startswith('loot2Weight2,'):
        continue
    else:
        out.append(ln)
write_lf('Items/LootChests/ChestLootTables/chestloot_rackweapon_b01.dbr', '\n'.join(out) + '\n')

# 3. chestloot_intropotions: 原版 + loot1Name2=item + loot1Weight2=100
t = open(os.path.join(ex, 'items', 'lootchests', 'questchests', 'questchestloottables',
                       'chestloot_intropotions.dbr'), encoding='utf-8', errors='replace').read()
lines = t.splitlines()
out = []
for ln in lines:
    if ln.startswith('loot1Name1,'):
        out.append(ln)
        out.append('loot1Name2,records/items/gearweapons/swords1h/item_startergodsword.dbr,')
    elif ln.startswith('loot1Weight1,'):
        out.append('loot1Weight1,100,')
        out.append('loot1Weight2,100,')
    elif ln.startswith('loot1Weight2,'):
        continue
    else:
        out.append(ln)
write_lf('Items/LootChests/QuestChests/QuestChestLootTables/chestloot_intropotions.dbr',
         '\n'.join(out) + '\n')

# 4. mt_gearweapons_a01: 原版 + lootName14=item + lootWeight14=20
t = open(os.path.join(ex, 'items', 'loottables', 'mastertables', 'mt_gearweapons_a01.dbr'),
         encoding='utf-8', errors='replace').read()
lines = t.splitlines()
out = []
for ln in lines:
    if ln.startswith('lootName13,'):
        out.append(ln)
        out.append('lootName14,records/items/gearweapons/swords1h/item_startergodsword.dbr,')
    elif ln.startswith('lootWeight13,'):
        out.append(ln)
        out.append('lootWeight14,20,')
    else:
        out.append(ln)
write_lf('Items/LootTables/MasterTables/mt_gearweapons_a01.dbr', '\n'.join(out) + '\n')

print()
print('=== final records ===')
for root, dirs, files in os.walk(rec):
    for f in sorted(files):
        print(' ', os.path.relpath(os.path.join(root, f), rec))
