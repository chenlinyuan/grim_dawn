import os, re

mod = r'H:\SteamLibrary\steamapps\common\Grim Dawn\mods\StarterGodWeapon'
rp = os.path.join(mod, 'database', 'Records', 'Items', 'GearAccessories', 'Rings', 'soul_ring.dbr')
lines = open(rp, encoding='ascii').read().splitlines()

has = any(l.startswith('characterDodgePercent,') for l in lines)
out = []
for l in lines:
    if l.startswith('characterDodgePercent,'):
        out.append('characterDodgePercent,20.000000,')
    else:
        out.append(l)
if not has:
    final = []
    for l in out:
        final.append(l)
        if l.startswith('characterDefensiveAbilityModifier,'):
            final.append('characterDodgePercent,20.000000,')
    out = final

open(rp, 'w', encoding='ascii', newline='\n').write('\n'.join(out) + '\n')
print('characterDodgePercent = 20')
for l in out:
    if l.startswith('characterDodgePercent'):
        print(' ', l)
