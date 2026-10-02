import os, re

ex = r'c:\Users\Administrator\Desktop\工作项目\Work\Grim Dawn\_gd_extract\db\records\items'
texts = {}
for base in [r'c:\Users\Administrator\Desktop\工作项目\Work\Grim Dawn\_gd_extract\text_en',
             r'c:\Users\Administrator\Desktop\工作项目\Work\Grim Dawn\_gd_extract\text_zh']:
    if not os.path.exists(base):
        continue
    for root, dirs, files in os.walk(base):
        for f in files:
            if not f.endswith('.txt'): continue
            try:
                for ln in open(os.path.join(root, f), encoding='utf-8', errors='replace'):
                    if '=' in ln:
                        k, v = ln.split('=', 1)
                        texts.setdefault(k.strip(), v.strip())
            except Exception:
                pass
print('loaded', len(texts), 'localization tags')

# 关键属性字段
STAT_KEYS = ['itemLevel', 'levelRequirement', 'itemClassification', 'itemStyleTag',
             'offensivePhysicalMin', 'offensivePhysicalMax', 'offensivePhysicalModifier',
             'characterOffensiveAbilityModifier', 'characterDefensiveAbilityModifier',
             'characterLife', 'characterLifeModifier', 'characterLifeRegenModifier',
             'characterManaModifier', 'characterAttackSpeedModifier', 'characterRunSpeedModifier',
             'characterStrengthModifier', 'characterDexterityModifier', 'characterIntelligenceModifier',
             'defensiveAllResistance', 'itemSkillName', 'itemSkillAutoController', 'itemSkillLevelEq']

for rel in ['gearweapons\\swords1h\\d008_sword.dbr',
            'gearweapons\\melee2h\\d007_sword2h.dbr']:
    p = os.path.join(ex, rel)
    print('\n' + '=' * 70)
    print(rel)
    print('=' * 70)
    if not os.path.exists(p):
        print('MISSING'); continue
    t = open(p, encoding='utf-8', errors='replace').read()
    tag = re.search(r'itemNameTag,([^,\r\n]+),', t)
    if tag:
        name = texts.get(tag.group(1), '?')
        print('NAME:', name, '(', tag.group(1), ')')
    for k in STAT_KEYS:
        m = re.search('^' + k + ',(.*)$', t, re.M)
        if m and m.group(1).strip() not in ('0.000000', '0', ''):
            print('  %-40s %s' % (k, m.group(1)))
