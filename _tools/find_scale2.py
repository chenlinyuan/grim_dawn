import os, re

base = r'H:\SteamLibrary\steamapps\common\Grim Dawn\Working\database\templates'
for root, dirs, files in os.walk(base):
    for f in files:
        if not f.endswith('.tpl'):
            continue
        try:
            t = open(os.path.join(root, f), encoding='utf-8', errors='replace').read()
        except Exception:
            continue
        for m in re.finditer('name\\s*=\\s*"([^"]+)"', t):
            n = m.group(1)
            if 'scale' in n.lower():
                print('%-42s %s' % (n, os.path.relpath(os.path.join(root, f), base)))
