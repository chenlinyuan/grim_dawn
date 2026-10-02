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

# 只显示"有意义"的属性（排除模板噪声/路径/0 值）
SKIP_PREFIX = ('templateName', 'Class', 'FileDescription', 'mesh', 'bitmap', 'baseTexture',
               'bumpTexture', 'actor', 'allowTransparency', 'cannotPickUp', 'castsShadows',
               'physics', 'outline', 'scale', 'shadow', 'unloaded', 'maxTransparency',
               'placement', 'quest', 'itemCostName', 'itemNameTag', 'itemQualityTag',
               'itemStyleTag', 'itemStyleTag', 'itemSetName', 'itemClassification',
               'itemLevel', 'levelRequirement', 'itemCost', 'itemSkillLevelEq',
               'itemSkillName', 'itemSkillAutoController', 'characterBaseAttackSpeedTag')

for rel in ['gearweapons\\melee2h\\d007_sword2h.dbr',
            'gearweapons\\swords1h\\d008_sword.dbr']:
    p = os.path.join(ex, rel)
    print('\n' + '=' * 72)
    t = open(p, encoding='utf-8', errors='replace').read()
    tag = re.search(r'itemNameTag,([^,\r\n]+),', t)
    name = texts.get(tag.group(1), '?') if tag else '?'
    lvl = re.search(r'itemLevel,(\d+),', t)
    print('NAME:', name, '| itemLevel:', lvl.group(1) if lvl else '?')
    print('=' * 72)
    for ln in t.splitlines():
        k, _, v = ln.partition(',')
        if any(k.startswith(s) for s in SKIP_PREFIX):
            continue
        v = v.rstrip(',')
        if v in ('', '0', '0.000000'):
            continue
        print('  %-42s %s' % (k, v))
