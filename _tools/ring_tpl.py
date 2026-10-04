import os, re

# 1. jewelry_ring.tpl 字段
p = r'H:\SteamLibrary\steamapps\common\Grim Dawn\Working\database\templates\jewelry_ring.tpl'
t = open(p, encoding='utf-8', errors='replace').read()
print('=== jewelry_ring.tpl ===')
print(t[:800])
print('...')
# 找 include
for m in re.finditer('defaultValue\\s*=\\s*"([^"]*[Tt]emplate[^"]*)"', t):
    print('include:', m.group(1))

# 2. 找"只能带一枚"的字段（uniqueEquip / equipLimit 等）
print()
print('=== 搜索 unique/equip limit 字段 ===')
base = r'H:\SteamLibrary\steamapps\common\Grim Dawn\Working\database\templates'
seen = set()
for root, dirs, files in os.walk(base):
    for f in files:
        if not f.endswith('.tpl'):
            continue
        try:
            tt = open(os.path.join(root, f), encoding='utf-8', errors='replace').read()
        except Exception:
            continue
        for m in re.finditer('name\\s*=\\s*"([^"]+)"', tt):
            n = m.group(1)
            ln = n.lower()
            if ('unique' in ln or 'limit' in ln or 'equipped' in ln) and n not in seen:
                seen.add(n)
                print('  %-40s %s' % (n, os.path.relpath(os.path.join(root, f), base)))
