import os, re

p = r'H:\SteamLibrary\steamapps\common\Grim Dawn\Working\database\templates\TemplateBase\Weapon.tpl'
print('exists:', os.path.exists(p))
if os.path.exists(p):
    t = open(p, encoding='utf-8', errors='replace').read()
    print('len', len(t))
    for kw in ['weaponTrail', 'glowTexture', 'itemMesh', 'mesh', 'bitmap',
               'baseTexture', 'bumpTexture', 'itemStyleTag']:
        found = re.search('name\\s*=\\s*"' + kw + '"', t)
        print('%-16s -> %s' % (kw, 'FOUND' if found else 'NOT in Weapon.tpl'))
    # 打印所有变量名
    print()
    print('=== all variable names in Weapon.tpl ===')
    for m in re.finditer('name\\s*=\\s*"([^"]+)"', t):
        print(' ', m.group(1))
