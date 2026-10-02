import os, re

mod = r'H:\SteamLibrary\steamapps\common\Grim Dawn\mods\StarterGodWeapon'
p = os.path.join(mod, 'database', 'Records', 'Items', 'GearWeapons', 'Swords1h', 'item_startergodsword.dbr')
lines = open(p, encoding='ascii').read().splitlines()

# 固定数值（attributeScalePercent=0 消除随机浮动）
updates = {
    'attributeScalePercent': '0.000000',          # 关键：消除浮动范围

    # --- 用户指定 ---
    'characterManaModifier': '100.000000',        # 能量 +100
    'characterLife': '100.000000',                # 生命 +100
    'characterAttackSpeedModifier': '20.000000',  # 攻速 +20%
    'characterRunSpeedModifier': '20.000000',     # 移速 +20%
    'characterStrengthModifier': '10.000000',     # 力量 +10
    'characterDexterityModifier': '10.000000',    # 敏捷 +10
    'characterIntelligenceModifier': '10.000000', # 智力 +10
    'offensiveLightningModifier': '50.000000',    # 闪电加成 +50%
    'offensivePhysicalModifier': '50.000000',     # 物理加成 +50%
    'characterLifeModifier': '0.000000',          # 生命百分比 0%

    # --- 下调过强属性（开荒适配）---
    'offensivePhysicalMin': '60.000000',
    'offensivePhysicalMax': '90.000000',
    'offensiveLightningMin': '40.000000',
    'offensiveLightningMax': '70.000000',
    'offensiveSlowLightningModifier': '0.000000', # 去掉电击减速加成
    'characterOffensiveAbilityModifier': '30.000000',   # OA +30
    'characterDefensiveAbilityModifier': '20.000000',   # DA +20
    'characterLifeRegenModifier': '5.000000',     # 生命恢复 +5%
    'defensiveAllResistance': '10.000000',        # 全抗 +10
    'conversionPercentage': '15.000000',          # 物理->闪电 15%
}

out = []
for ln in lines:
    k = ln.split(',')[0]
    if k in updates:
        out.append(k + ',' + updates[k] + ',')
    else:
        out.append(ln)

open(p, 'w', encoding='ascii', newline='\n').write('\n'.join(out) + '\n')
print('applied', len(updates), 'fixed values')
print()
for ln in out:
    k = ln.split(',')[0]
    if k in updates:
        print('  %-38s %s' % (k, ln.split(',')[1]))
