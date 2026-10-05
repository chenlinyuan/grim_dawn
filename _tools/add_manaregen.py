import os

mod = r'H:\SteamLibrary\steamapps\common\Grim Dawn\mods\StarterGodWeapon'

# 1. 戒指加 characterManaRegen=50
rp = os.path.join(mod, 'database', 'Records', 'Items', 'GearAccessories', 'Rings', 'soul_ring.dbr')
lines = open(rp, encoding='ascii').read().splitlines()
has = any(l.startswith('characterManaRegen,') for l in lines)
out = []
for l in lines:
    if l.startswith('characterManaRegen,'):
        out.append('characterManaRegen,50.000000,')
    else:
        out.append(l)
if not has:
    final = []
    for l in out:
        final.append(l)
        if l.startswith('characterManaModifier,'):
            final.append('characterManaRegen,50.000000,')
    out = final
open(rp, 'w', encoding='ascii', newline='\n').write('\n'.join(out) + '\n')
print('=== ring ===')
for l in out:
    if l.startswith('characterManaRegen') or l.startswith('characterManaModifier'):
        print(' ', l)

# 2. 技能冷却 0.5 秒
sp = os.path.join(mod, 'database', 'Records', 'Skills', 'ItemSkills', 'Legendary', 'item_heavenstrike.dbr')
lines = open(sp, encoding='ascii').read().splitlines()
out = ['skillCooldownTime,0.500000,' if l.startswith('skillCooldownTime,') else l for l in lines]
open(sp, 'w', encoding='ascii', newline='\n').write('\n'.join(out) + '\n')
print('=== skill ===')
for l in out:
    if l.startswith('skillCooldownTime'):
        print(' ', l)
