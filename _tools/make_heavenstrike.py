import os, re

mod = r'H:\SteamLibrary\steamapps\common\Grim Dawn\mods\StarterGodWeapon'
ex = r'c:\Users\Administrator\Desktop\工作项目\Work\Grim Dawn\_gd_extract\db\records\skills\base_template skills\skill_attackweaponradius.dbr'

# 以武器伤害范围技能为模板
t = open(ex, encoding='utf-8', errors='replace').read()
lines = t.splitlines()

updates = {
    'FileDescription': 'Heaven Strike (weapon-damage lightning radius)',
    'skillDisplayName': 'tagItemSkillHeavenStrikeName',
    'skillBaseDescription': 'tagItemSkillHeavenStrikeDesc',
    'skillTargetRadius': '4.000000',       # 4 米范围
    'skillCooldownTime': '1.500000',       # 冷却 1.5 秒
    'weaponDamagePct': '100.000000',       # 100% 武器伤害（受力量加成）
    'lightningName': 'records/fx/skillsother/rangeddirect/lightning1.dbr',  # 天降雷霆特效
    'Sword': '1',                          # 剑可用
}

present = set(l.split(',')[0] for l in lines)
out = []
for ln in lines:
    k = ln.split(',')[0]
    if k in updates:
        out.append(k + ',' + updates[k] + ',')
    else:
        out.append(ln)
# 补缺失字段
for k, v in updates.items():
    if k not in present:
        out.append(k + ',' + v + ',')

dst = os.path.join(mod, 'database', 'Records', 'Skills', 'ItemSkills', 'Legendary', 'item_heavenstrike.dbr')
open(dst, 'w', encoding='ascii', newline='\n').write('\n'.join(out) + '\n')
print('created Heaven Strike (weapon-damage radius), lines:', len(out))
print()
for ln in out:
    k = ln.split(',')[0]
    if k in ('templateName', 'Class', 'FileDescription', 'skillDisplayName', 'skillTargetRadius',
             'skillCooldownTime', 'weaponDamagePct', 'lightningName', 'Sword', 'skillMaxLevel'):
        print(' ', ln)
