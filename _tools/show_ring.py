import os, re

ex = r'c:\Users\Administrator\Desktop\工作项目\Work\Grim Dawn\_gd_extract\db\records\items\gearaccessories\rings'
# 找一个 Legendary 戒指
for f in sorted(os.listdir(ex)):
    if not f.endswith('.dbr'):
        continue
    p = os.path.join(ex, f)
    t = open(p, encoding='utf-8', errors='replace').read()
    if 'itemClassification,Legendary' in t:
        print('=== 传说戒指:', f, '===')
        for ln in t.splitlines():
            k, _, v = ln.partition(',')
            v = v.rstrip(',')
            if v in ('', '0', '0.000000'):
                continue
            if any(x in k for x in ['templateName', 'Class', 'itemName', 'itemLevel', 'levelReq',
                                     'itemClass', 'itemStyle', 'characterAttackSpeed', 'characterRunSpeed',
                                     'characterIncreasedExp', 'itemSkill', 'mesh', 'bitmap', 'baseTexture',
                                     'attributeScale', 'itemCost', 'only', 'unique', 'equip', 'slot']):
                print('  %-38s %s' % (k, v[:70]))
        break
