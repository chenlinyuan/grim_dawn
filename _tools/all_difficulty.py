import os

mod = r'H:\SteamLibrary\steamapps\common\Grim Dawn\mods\StarterGodWeapon'
lcd = os.path.join(mod, 'database', 'Records', 'Items', 'LootChests', 'ChestLootTables')

# 所有难度 1000%（9 个值）
all_difficulty = 'loot4Chance,' + ';'.join(['1000.000000'] * 9) + ','

for name in ['chestloot_all_a01_lowercrossinga01', 'chestloot_all_a01_lowercrossingmelee']:
    p = os.path.join(lcd, name + '.dbr')
    lines = open(p, encoding='ascii').read().splitlines()
    out = [all_difficulty if l.startswith('loot4Chance,') else l for l in lines]
    open(p, 'w', encoding='ascii', newline='\n').write('\n'.join(out) + '\n')
    print('===', name, '===')
    for l in out:
        if l.startswith('loot4Chance'):
            print(' ', l)
