import os, re

mod = r'H:\SteamLibrary\steamapps\common\Grim Dawn\mods\StarterGodWeapon'
p = os.path.join(mod, 'database', 'Records', 'Items', 'GearWeapons', 'Swords1h', 'item_startergodsword.dbr')
lines = open(p, encoding='ascii').read().splitlines()

# --- 1. 去掉这些属性（生命/灵巧/精神/敏捷/力量/能量 加成）---
remove_keys = {
    'characterLife', 'characterLifeModifier', 'characterDexterityModifier',
    'characterIntelligenceModifier', 'characterStrengthModifier', 'characterManaModifier',
}
out = [l for l in lines if l.split(',')[0] not in remove_keys]

# --- 2. 修正 attributeScalePercent 位置：移到 bitmap 之后 ---
# 先移除现有的 attributeScalePercent 行
scale_line = 'attributeScalePercent,0.000000,'
out = [l for l in out if not l.startswith('attributeScalePercent,')]
# 在 bitmap 行后插入
final = []
for l in out:
    final.append(l)
    if l.startswith('bitmap,'):
        final.append(scale_line)
out = final

open(p, 'w', encoding='ascii', newline='\n').write('\n'.join(out) + '\n')
print('=== item record: key fields ===')
for i, l in enumerate(out):
    k = l.split(',')[0]
    if k in ('itemNameTag', 'itemStyleTag', 'bitmap', 'attributeScalePercent', 'itemCostName',
             'characterLife', 'characterDexterityModifier', 'characterIntelligenceModifier',
             'characterStrengthModifier', 'characterManaModifier', 'characterAttackSpeedModifier',
             'characterRunSpeedModifier', 'defensiveAllResistance', 'offensiveLightningModifier',
             'offensivePhysicalModifier', 'conversionPercentage'):
        print(' ', i, l)
print('total lines:', len(out))

# --- 3. 天击技能范围改为 4 米 ---
sp = os.path.join(mod, 'database', 'Records', 'Skills', 'ItemSkills', 'Legendary', 'item_heavenstrike.dbr')
st = open(sp, encoding='ascii').read()
st2 = re.sub(r'^skillTargetRadius,.*$', 'skillTargetRadius,4.000000,', st, flags=re.M)
open(sp, 'w', encoding='ascii', newline='\n').write(st2)
print()
print('=== skill target radius ===')
for l in st2.splitlines():
    if l.startswith('skillTargetRadius'):
        print(' ', l)
