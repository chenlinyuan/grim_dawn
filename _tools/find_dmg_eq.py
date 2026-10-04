import os, re

base = r'H:\SteamLibrary\steamapps\common\Grim Dawn\Working\database\templates'
# 找伤害公式/属性绑定字段
seen = set()
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
            ln = n.lower()
            if any(x in ln for x in ['equation', 'damage', 'strength', 'attribute', 'scaling', 'scale']):
                if n not in seen:
                    seen.add(n)
                    print('%-42s %s' % (n, os.path.relpath(os.path.join(root, f), base)))
