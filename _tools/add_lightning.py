import os

mod = r'H:\SteamLibrary\steamapps\common\Grim Dawn\mods\StarterGodWeapon'
p = os.path.join(mod, 'database', 'Records', 'Items', 'GearWeapons', 'Swords1h', 'item_startergodsword.dbr')
lines = open(p, encoding='ascii').read().splitlines()

updates = {
    # 闪电伤害（配合天击雷霆主题）
    'offensiveLightningMin': '120.000000',
    'offensiveLightningMax': '220.000000',
    'offensiveLightningModifier': '80.000000',
    'offensiveSlowLightningModifier': '80.000000',
    # 物理 -> 闪电 转化 25%
    'conversionInType': 'Physical',
    'conversionOutType': 'Lightning',
    'conversionPercentage': '25.000000',
    # 闪电剑拖尾
    'weaponTrail': 'records/fx/fxtrails/swordlightning_fxtrail.dbr',
}

out = []
updated = set()
for ln in lines:
    k = ln.split(',')[0]
    if k in updates:
        out.append(k + ',' + updates[k] + ',')
        updated.add(k)
    else:
        out.append(ln)

# 补上缺失的字段（conversion* 原文件没有）：插在 weaponTrail 之前
missing = [k for k in updates if k not in updated]
if missing:
    final = []
    for ln in out:
        if ln.startswith('weaponTrail,') and 'weaponTrail' in missing:
            final.append('conversionInType,' + updates['conversionInType'] + ',')
            final.append('conversionOutType,' + updates['conversionOutType'] + ',')
            final.append('conversionPercentage,' + updates['conversionPercentage'] + ',')
            missing = [m for m in missing if not m.startswith('conversion')]
            final.append(ln)
        else:
            final.append(ln)
    out = final

open(p, 'w', encoding='ascii', newline='\n').write('\n'.join(out) + '\n')
print('updated existing:', sorted(updated))
print('inserted new:', missing)
print()
for ln in out:
    k = ln.split(',')[0]
    if k in updates:
        print(' ', ln)
