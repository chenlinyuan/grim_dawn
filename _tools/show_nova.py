import os, re

ex = r'c:\Users\Administrator\Desktop\工作项目\Work\Grim Dawn\_gd_extract\db\records\skills\itemskills'
for rel in ['item_defenselightningnova_01.dbr', 'comp_lightningnova_01.dbr', 'item_chaosnova.dbr']:
    p = os.path.join(ex, rel)
    print('=' * 70)
    print(rel, 'exists:', os.path.exists(p))
    print('=' * 70)
    if not os.path.exists(p):
        continue
    t = open(p, encoding='utf-8', errors='replace').read()
    keys = ['templateName', 'Class', 'FileDescription', 'skillTargetRadius', 'skillCooldownTime',
            'skillDisplayName', 'skillMaxLevel', 'skillManaCost', 'lightningName', 'radiusEffectName',
            'radiusMagicName', 'offensiveLightningMin', 'offensiveLightningMax', 'skillTargetType',
            'skillProjectileNumber', 'skillProjectileName', 'Sword', 'skillActiveDuration',
            'skillTargetNumber', 'skillTargetRadiusEquation']
    for k in keys:
        m = re.search('^' + k + ',(.*)$', t, re.M)
        if m and m.group(1).strip() not in ('0.000000', '0', ''):
            print('  %-32s %s' % (k, m.group(1)))
    print()
