import os, re

mod = r'H:\SteamLibrary\steamapps\common\Grim Dawn\mods\StarterGodWeapon'
ex = r'c:\Users\Administrator\Desktop\工作项目\Work\Grim Dawn\_gd_extract\db\records\skills\itemskills\item_defenselightningnova_01.dbr'

# 读原版闪电新星作为模板
t = open(ex, encoding='utf-8', errors='replace').read()
lines = t.splitlines()

out = []
for ln in lines:
    k = ln.split(',')[0]
    # 改名字标签为我们的
    if k == 'skillDisplayName':
        out.append('skillDisplayName,tagItemSkillHeavenStrikeName,')
    elif k == 'skillBaseDescription':
        out.append('skillBaseDescription,tagItemSkillHeavenStrikeDesc,')
    elif k == 'FileDescription':
        out.append('FileDescription,Heaven Strike (Lightning Nova),')
    # 只允许剑使用（Sword=1）
    elif k == 'Sword':
        out.append('Sword,1,')
    # 冷却改为 1.0（新星频率高）
    elif k == 'skillCooldownTime':
        out.append('skillCooldownTime,1.000000,')
    # 范围固定 4 米
    elif k == 'skillTargetRadius':
        out.append('skillTargetRadius,4.000000,')
    else:
        out.append(ln)

dst = os.path.join(mod, 'database', 'Records', 'Skills', 'ItemSkills', 'Legendary', 'item_heavenstrike.dbr')
open(dst, 'w', encoding='ascii', newline='\n').write('\n'.join(out) + '\n')
print('created lightning nova skill, lines:', len(out))
print()
for ln in out:
    k = ln.split(',')[0]
    if k in ('templateName', 'Class', 'FileDescription', 'skillDisplayName', 'skillBaseDescription',
             'skillTargetRadius', 'skillCooldownTime', 'skillMaxLevel', 'radiusEffectName', 'Sword'):
        print(' ', ln)
