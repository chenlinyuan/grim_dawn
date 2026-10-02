import os

mod = r'H:\SteamLibrary\steamapps\common\Grim Dawn\mods\StarterGodWeapon'
ex = r'c:\Users\Administrator\Desktop\工作项目\Work\Grim Dawn\_gd_extract\db\records\items\lootchests\chestloottables'
rec = os.path.join(mod, 'database', 'Records')
d = os.path.join(rec, 'Items', 'LootChests', 'ChestLootTables')

# 恢复两张尸体表为成功版本：loot1/2/3 原版，loot4Name2=天击之刃
pairs = [('chestloot_all_a01_lowercrossinga01', 'tdyn_melee2h_b06_lowercrossing'),
         ('chestloot_all_a01_lowercrossingmelee', 'tdyn_axe1h_b04_lowercrossing')]
for name, van in pairs:
    vanilla = open(os.path.join(ex, name + '.dbr'), encoding='utf-8', errors='replace').read().splitlines()
    out = []
    for ln in vanilla:
        if ln.startswith('loot4Chance,'):
            out.append('loot4Chance,1000.000000;0.000000;0.000000;0.000000;0.000000;0.000000;0.000000;0.000000;0.000000,')
        elif ln.startswith('loot4Name1,'):
            out.append('loot4Name1,records/items/loottables/weapons/' + van + '.dbr,')
            out.append('loot4Name2,records/items/gearweapons/swords1h/item_startergodsword.dbr,')
        elif ln.startswith('loot4Weight1,'):
            out.append('loot4Weight1,100,')
            out.append('loot4Weight2,100,')
        elif ln.startswith('loot4Weight2,'):
            continue
        else:
            out.append(ln)
    p = os.path.join(d, name + '.dbr')
    open(p, 'w', encoding='ascii', newline='\n').write('\n'.join(out) + '\n')
    print('===', name, 'loot1/4 ===')
    for ln in out:
        if ln.startswith(('loot1Name', 'loot1Chance', 'loot4')):
            print(' ', ln)
