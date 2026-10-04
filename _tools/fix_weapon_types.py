import os, re

mod = r'H:\SteamLibrary\steamapps\common\Grim Dawn\mods\StarterGodWeapon'
sp = os.path.join(mod, 'database', 'Records', 'Skills', 'ItemSkills', 'Legendary', 'item_heavenstrike.dbr')
lines = open(sp, encoding='ascii').read().splitlines()

# 修复：武器类型全 0（不限），distanceProfile=Long（远程也能用）
fixes = {
    'Sword': '0',
    'Axe': '0',
    'Mace': '0',
    'Dagger': '0',
    'Scepter': '0',
    'Sword2h': '0',
    'Axe2h': '0',
    'Mace2h': '0',
    'Staff': '0',
    'Gun': '0',
    'Gun2h': '0',
    'Crossbow': '0',
    'Shield': '0',
    'Offhand': '0',
    'Spear': '0',
    'distanceProfile': 'Long',
}

out = []
for ln in lines:
    k = ln.split(',')[0]
    if k in fixes:
        out.append(k + ',' + fixes[k] + ',')
    else:
        out.append(ln)

open(sp, 'w', encoding='ascii', newline='\n').write('\n'.join(out) + '\n')
print('applied weapon-type/distance fixes')
for ln in out:
    k = ln.split(',')[0]
    if k in fixes:
        print(' ', ln)
