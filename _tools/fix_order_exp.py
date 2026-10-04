import os, re

mod = r'H:\SteamLibrary\steamapps\common\Grim Dawn\mods\StarterGodWeapon'
p = os.path.join(mod, 'database', 'Records', 'Items', 'GearWeapons', 'Swords1h', 'item_startergodsword.dbr')
lines = open(p, encoding='ascii').read().splitlines()

# 1. 移除 attributeScalePercent（稍后按正确位置重新插入）
out = [l for l in lines if not l.startswith('attributeScalePercent,')]

# 2. 在 allowTransparency 之后插入 attributeScalePercent（原版顺序）
final = []
for l in out:
    final.append(l)
    if l.startswith('allowTransparency,'):
        final.append('attributeScalePercent,0.000000,')
out = final

# 3. 加 characterIncreasedExperience,100（按字母序：characterIntelligenceModifier 之后 / characterLife 之前）
#    原版顺序: characterIntelligenceModifier -> characterLife -> characterLifeModifier -> ...
#    characterIncreasedExperience 按字母序在 characterIntelligence 之后
final = []
inserted = False
for l in out:
    k = l.split(',')[0]
    # 在 characterLife 之前插入（字母序 characterIncreasedExperience < characterLife）
    if not inserted and k.startswith('characterLife,') or (not inserted and k.startswith('characterLightRadius,')):
        final.append('characterIncreasedExperience,100.000000,')
        inserted = True
    final.append(l)
if not inserted:
    # 兜底：在 castsShadows 后插入
    final = []
    for l in out:
        final.append(l)
        if l.startswith('castsShadows,'):
            final.append('characterIncreasedExperience,100.000000,')
            inserted = True
out = final

open(p, 'w', encoding='ascii', newline='\n').write('\n'.join(out) + '\n')
print('attributeScalePercent inserted after allowTransparency:', any(l.startswith('attributeScalePercent') for l in out))
print('characterIncreasedExperience inserted:', any(l.startswith('characterIncreasedExperience') for l in out))
print()
print('=== 前 30 行 ===')
for i, l in enumerate(out[:30]):
    print(' ', i, l)
