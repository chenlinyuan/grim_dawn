import os, re

# 查 skill_attackradiuslightning.tpl 和 skill_attack.tpl 的字段，找"属性绑定"
for tpl in ['skill_attackradiuslightning.tpl', 'templatebase\\skill_attack.tpl',
            'templatebase\\skill_base.tpl', 'templatebase\\parameters_offensive.tpl']:
    p = os.path.join(r'H:\SteamLibrary\steamapps\common\Grim Dawn\Working\database\templates', tpl)
    print('=' * 60)
    print(tpl, 'exists:', os.path.exists(p))
    print('=' * 60)
    if not os.path.exists(p):
        continue
    t = open(p, encoding='utf-8', errors='replace').read()
    for m in re.finditer('name\\s*=\\s*"([^"]+)"', t):
        n = m.group(1)
        ln = n.lower()
        if any(x in ln for x in ['equation', 'strength', 'dexterity', 'intelligence',
                                  'attributemodifier', 'scaling', 'weapondamage', 'percentweapon']):
            print('  ', n)
    print()
