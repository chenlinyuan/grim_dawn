import os, re

mod = r'H:\SteamLibrary\steamapps\common\Grim Dawn\mods\StarterGodWeapon'
ex = r'c:\Users\Administrator\Desktop\工作项目\Work\Grim Dawn\_gd_extract\db\records\items\gearaccessories\rings\d000_ring.dbr'

# 读原版传说戒指作为模板
t = open(ex, encoding='utf-8', errors='replace').read()
lines = t.splitlines()

# 需要修改/添加的字段
updates = {
    'itemNameTag': 'tagSoulRing',
    'itemClassification': 'Legendary',
    'itemLevel': '1',
    'levelRequirement': '1',
    'itemStyleTag': 'tagStyleUniqueTier3',
    'itemCostName': 'records/game/itemcostformulas_legend.dbr',
    'attributeScalePercent': '0.000000',
    # 3 条核心属性
    'characterAttackSpeedModifier': '100.000000',
    'characterRunSpeedModifier': '100.000000',
    'characterIncreasedExperience': '100.000000',
    # 技能
    'itemSkillName': 'records/skills/itemskills/legendary/item_heavenstrike.dbr',
    'itemSkillAutoController': 'records/controllers/itemskills/cast_@enemyonanyhit_100%.dbr',
    'itemSkillLevelEq': '1',
}

present = set(l.split(',')[0] for l in lines)
out = []
for ln in lines:
    k = ln.split(',')[0]
    if k in updates:
        out.append(k + ',' + updates[k] + ',')
    else:
        out.append(ln)

# 补上原版没有的字段（characterIncreasedExperience / itemSkillName 等）
for k, v in updates.items():
    if k not in present:
        out.append(k + ',' + v + ',')

dst = os.path.join(mod, 'database', 'Records', 'Items', 'GearAccessories', 'Rings', 'soul_ring.dbr')
os.makedirs(os.path.dirname(dst), exist_ok=True)
open(dst, 'w', encoding='ascii', newline='\n').write('\n'.join(out) + '\n')
print('created soul_ring.dbr, lines:', len(out))
print()
for ln in out:
    k = ln.split(',')[0]
    if k in updates or k in ('templateName', 'Class', 'mesh', 'bitmap', 'baseTexture'):
        print(' ', ln)
