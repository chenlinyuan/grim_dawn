import os

mod = r'H:\SteamLibrary\steamapps\common\Grim Dawn\mods\StarterGodWeapon'
p = os.path.join(mod, 'database', 'Records', 'Items', 'GearWeapons', 'Swords1h', 'item_startergodsword.dbr')

lines = open(p, encoding='ascii').read().splitlines()

# 神话级属性值（字段已存在 -> 直接改值）
updates = {
    'offensivePhysicalMin': '250.000000',
    'offensivePhysicalMax': '450.000000',
    'offensivePhysicalModifier': '120.000000',
    'characterOffensiveAbilityModifier': '60.000000',
    'characterDefensiveAbilityModifier': '40.000000',
    'characterLife': '250.000000',
    'characterLifeModifier': '8.000000',
    'characterLifeRegenModifier': '12.000000',
    'characterManaModifier': '150.000000',
    'characterAttackSpeedModifier': '18.000000',
    'characterRunSpeedModifier': '8.000000',
    'characterStrengthModifier': '25.000000',
    'characterDexterityModifier': '25.000000',
    'characterIntelligenceModifier': '25.000000',
}

out = []
updated = set()
for ln in lines:
    key = ln.split(',')[0]
    if key in updates:
        out.append(key + ',' + updates[key] + ',')
        updated.add(key)
    else:
        out.append(ln)

# 新增 defensiveAllResistance（全部抗性，神话标志属性），按字母序插在 defensiveAether 之后
new_field = 'defensiveAllResistance,20.000000,'
inserted = False
final = []
for ln in out:
    final.append(ln)
    if ln.startswith('defensiveAether,') and not inserted:
        final.append(new_field)
        inserted = True
out = final

open(p, 'w', encoding='ascii', newline='\n').write('\n'.join(out) + '\n')
print('updated fields:', len(updated), '->', sorted(updated))
print('defensiveAllResistance inserted:', inserted)

# 打印验证
for ln in out:
    k = ln.split(',')[0]
    if k in updates or k == 'defensiveAllResistance':
        print(' ', ln)
