import os

mod = r'H:\SteamLibrary\steamapps\common\Grim Dawn\mods\StarterGodWeapon'
sp = os.path.join(mod, 'database', 'Records', 'Skills', 'ItemSkills', 'Legendary', 'item_heavenstrike.dbr')
lines = open(sp, encoding='ascii').read().splitlines()
out = []
for ln in lines:
    if ln.startswith('weaponDamagePct,'):
        out.append('weaponDamagePct,150.000000,')
    else:
        out.append(ln)
open(sp, 'w', encoding='ascii', newline='\n').write('\n'.join(out) + '\n')
print('weaponDamagePct -> 150')
for l in out:
    if l.startswith('weaponDamagePct'):
        print(' ', l)
