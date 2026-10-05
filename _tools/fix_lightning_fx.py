import os

mod = r'H:\SteamLibrary\steamapps\common\Grim Dawn\mods\StarterGodWeapon'
sp = os.path.join(mod, 'database', 'Records', 'Skills', 'ItemSkills', 'Legendary', 'item_heavenstrike.dbr')
lines = open(sp, encoding='ascii').read().splitlines()

# 删除野性打击特效，保留天降雷霆
remove = ('particleEffectName1', 'particleEffectAttachPoint1', 'particleEffectName2',
          'particleEffectAttachPoint2', 'targetFxPakName', 'targetFxFirstOnly')
out = []
for l in lines:
    k = l.split(',')[0]
    if k in remove:
        continue
    if k == 'skillCooldownTime':
        out.append('skillCooldownTime,1.000000,')
    elif k == 'lightningName':
        out.append('lightningName,records/fx/skillsother/rangeddirect/lightning1.dbr,')
    else:
        out.append(l)

open(sp, 'w', encoding='ascii', newline='\n').write('\n'.join(out) + '\n')
print('removed wild-strike FX, kept sky lightning; cooldown=1s')
print()
for l in out:
    k = l.split(',')[0]
    if any(x in k.lower() for x in ['lightning', 'particle', 'targetfx', 'cooldown', 'radius']):
        print(' ', l)
