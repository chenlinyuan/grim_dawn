import os, re

mod = r'H:\SteamLibrary\steamapps\common\Grim Dawn\mods\StarterGodWeapon'
rp = os.path.join(mod, 'database', 'Records', 'Items', 'GearAccessories', 'Rings', 'soul_ring.dbr')
lines = open(rp, encoding='ascii').read().splitlines()

# 删除 characterDodgePercent，加 defensiveAllResistance
has_res = any(l.startswith('defensiveAllResistance,') for l in lines)
out = []
for l in lines:
    if l.startswith('characterDodgePercent,'):
        continue  # 删除闪避
    if l.startswith('defensiveAllResistance,'):
        out.append('defensiveAllResistance,25.000000,')
    else:
        out.append(l)

if not has_res:
    final = []
    for l in out:
        final.append(l)
        if l.startswith('defensiveAether,'):
            final.append('defensiveAllResistance,25.000000,')
    out = final

open(rp, 'w', encoding='ascii', newline='\n').write('\n'.join(out) + '\n')
print('removed dodge, added all-resistance')
for l in out:
    if l.startswith('characterDodgePercent') or l.startswith('defensiveAllResistance'):
        print(' ', l)
