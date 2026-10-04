import os, re

mod = r'H:\SteamLibrary\steamapps\common\Grim Dawn\mods\StarterGodWeapon'
rp = os.path.join(mod, 'database', 'Records', 'Items', 'GearAccessories', 'Rings', 'soul_ring.dbr')
lines = open(rp, encoding='ascii').read().splitlines()

# 检查是否已有 skillCooldownReduction
has = any(l.startswith('skillCooldownReduction,') for l in lines)
out = []
for l in lines:
    if l.startswith('skillCooldownReduction,'):
        out.append('skillCooldownReduction,50.000000,')
    else:
        out.append(l)
# 若没有，按字母序插入（skillCooldownReduction 在 skillMaxLevel 之前，或 castsShadows 之后）
if not has:
    final = []
    for l in out:
        final.append(l)
        if l.startswith('castsShadows,'):
            final.append('skillCooldownReduction,50.000000,')
    out = final

open(rp, 'w', encoding='ascii', newline='\n').write('\n'.join(out) + '\n')
print('skillCooldownReduction set to 50%')
for l in out:
    if l.startswith('skillCooldownReduction'):
        print(' ', l)
