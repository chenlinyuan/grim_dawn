import os, re

mod = r'H:\SteamLibrary\steamapps\common\Grim Dawn\mods\StarterGodWeapon'
ex = r'c:\Users\Administrator\Desktop\工作项目\Work\Grim Dawn\_gd_extract\db\records\skills\itemskills\legendary\item_lightningbolt.dbr'

# 以原版传说天击为模板
t = open(ex, encoding='utf-8', errors='replace').read()
lines = t.splitlines()

updates = {
    'FileDescription': 'Heaven Strike (sky lightning bolt)',
    'skillDisplayName': 'tagItemSkillHeavenStrikeName',
    'skillBaseDescription': 'tagItemSkillHeavenStrikeDesc',
    'skillTargetRadius': '4.000000',       # 4 米范围
    'skillCooldownTime': '1.000000',       # 冷却 1 秒
    'weaponDamagePct': '200.000000',       # 200% 武器伤害（与力量绑定）
    'lightningName': 'records/fx/skillsother/rangeddirect/lightning1.dbr',  # 天降雷霆
    'targetFxPakName': 'records/fx/skillsother/rangeddirect/lightningbolt1_impact01_fxpak.dbr',  # 雷电击中
    'distanceProfile': 'Maximum',
    'Sword': '0', 'Axe': '0', 'Mace': '0', 'Dagger': '0', 'Scepter': '0',
    'Sword2h': '0', 'Axe2h': '0', 'Mace2h': '0', 'Staff': '0', 'Gun': '0',
    'Gun2h': '0', 'Crossbow': '0', 'Shield': '0', 'Offhand': '0', 'Spear': '0',
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
print('created Heaven Strike from item_lightningbolt, lines:', len(out))
print()
for ln in out:
    k = ln.split(',')[0]
    if k in ('templateName', 'Class', 'FileDescription', 'skillDisplayName', 'skillTargetRadius',
             'skillCooldownTime', 'weaponDamagePct', 'lightningName', 'targetFxPakName',
             'distanceProfile', 'skillMaxLevel'):
        print(' ', ln)
