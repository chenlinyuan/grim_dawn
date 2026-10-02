import os

mod = r'H:\SteamLibrary\steamapps\common\Grim Dawn\mods\StarterGodWeapon'
ex = r'c:\Users\Administrator\Desktop\工作项目\Work\Grim Dawn\_gd_extract\db\records\items\gearweapons\melee2h'

lines = open(os.path.join(ex, 'b013a_sword2h.dbr'), encoding='utf-8', errors='replace').read().splitlines()

# 要删除的原版字段
skip = ('itemNameTag', 'itemLevel,', 'levelRequirement', 'itemClassification',
        'itemQualityTag', 'FileDescription', 'itemSkill', 'itemCostName')
out = [l for l in lines if not any(l.startswith(p) for p in skip)]

# 我们的自定义字段
custom = [
    'FileDescription,Starter Godsword,',
    'itemClassification,Legendary,',
    'itemLevel,1,',
    'levelRequirement,1,',
    'itemNameTag,tagStarterGodSword,',
    'itemStyleTag,tagStyleUniqueTier3,',
    'itemCostName,records/items/itemcostformulas/itemcostformulas_legend.dbr,',
    'offensivePhysicalMin,150.000000,',
    'offensivePhysicalMax,250.000000,',
    'itemSkillName,records/skills/itemskills/legendary/item_heavenstrike.dbr,',
    'itemSkillAutoController,records/controllers/itemskills/cast_@enemyonanyhit_100%.dbr,',
    'itemSkillLevelEq,1,',
]

idx = next(i for i, l in enumerate(out) if l.startswith('Class,'))
out = out[:idx + 1] + custom + out[idx + 1:]

dst = os.path.join(mod, 'database', 'Records', 'Items', 'GearWeapons', 'Melee2h')
os.makedirs(dst, exist_ok=True)
# LF 换行！
open(os.path.join(dst, 'b013a_sword2h.dbr'), 'w', encoding='ascii', newline='\n').write('\n'.join(out) + '\n')
print('written b013a_sword2h.dbr override, lines:', len(out))
