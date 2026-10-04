import os

mod = r'H:\SteamLibrary\steamapps\common\Grim Dawn\mods\StarterGodWeapon'
rp = os.path.join(mod, 'database', 'Records', 'Items', 'GearAccessories', 'Rings', 'soul_ring.dbr')
lines = open(rp, encoding='ascii').read().splitlines()

updates = {
    'characterAttackSpeedModifier': '50.000000',
    'characterRunSpeedModifier': '50.000000',
    'skillCooldownReduction': '20.000000',
}

out = []
for l in lines:
    k = l.split(',')[0]
    if k in updates:
        out.append(k + ',' + updates[k] + ',')
    else:
        out.append(l)

open(rp, 'w', encoding='ascii', newline='\n').write('\n'.join(out) + '\n')
print('updated:')
for l in out:
    k = l.split(',')[0]
    if k in updates:
        print(' ', l)
