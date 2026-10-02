import os

mod = r'H:\SteamLibrary\steamapps\common\Grim Dawn\mods\StarterGodWeapon'
rec = os.path.join(mod, 'database', 'Records')

# 1. 删除中间表（AssetManager 串行 bug：A 表引用 B 表时会把 A 的内容写进 B）
p = os.path.join(rec, 'Items', 'LootTables', 'Weapons', 'lt_starterlegendaries.dbr')
if os.path.exists(p):
    os.remove(p)
    print('removed lt_starterlegendaries.dbr')

# 2. 两张尸体表：直接引用原版暗金物品（原版路径 -> 能编译）
d = os.path.join(rec, 'Items', 'LootChests', 'ChestLootTables')
for name in ['chestloot_all_a01_lowercrossinga01', 'chestloot_all_a01_lowercrossingmelee']:
    p = os.path.join(d, name + '.dbr')
    lines = open(p, encoding='ascii').read().splitlines()
    out = []
    for ln in lines:
        if ln.startswith('loot1Name2,'):
            out.append('loot1Name2,records/items/gearweapons/melee2h/d000_axe2h.dbr,')
        elif ln.startswith('loot2Chance,'):
            out.append('loot2Chance,1000.000000;1000.000000;1000.000000;1000.000000;1000.000000;1000.000000;1000.000000;1000.000000;1000.000000,')
        elif ln.startswith('loot2Name2,'):
            out.append('loot2Name2,records/items/gearweapons/melee2h/d000_blunt2h.dbr,')
        elif ln.startswith('loot2Weight2,'):
            out.append('loot2Weight2,100,')
        elif ln.startswith('loot3Chance,'):
            out.append('loot3Chance,1000.000000;1000.000000;1000.000000;1000.000000;1000.000000;1000.000000;1000.000000;1000.000000;1000.000000,')
        elif ln.startswith('loot3Name2,'):
            out.append('loot3Name2,records/items/gearweapons/melee2h/d000_sword2h.dbr,')
        elif ln.startswith('loot3Weight2,'):
            out.append('loot3Weight2,100,')
        else:
            out.append(ln)
    open(p, 'w', encoding='ascii', newline='\n').write('\n'.join(out) + '\n')
    print('updated', name)

# 清理空目录
for root, dirs, files in os.walk(rec, topdown=False):
    if not os.listdir(root):
        os.rmdir(root)

print()
print('=== records ===')
for root, dirs, files in os.walk(rec):
    for f in sorted(files):
        print(' ', os.path.relpath(os.path.join(root, f), rec))
