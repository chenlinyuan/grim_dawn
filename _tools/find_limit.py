import os, re

# 看 itemset.tpl 的完整字段，找"唯一/限制"相关
p = r'H:\SteamLibrary\steamapps\common\Grim Dawn\Working\database\templates\itemset.tpl'
t = open(p, encoding='utf-8', errors='replace').read()
print('=== itemset.tpl 字段 ===')
for m in re.finditer('name\\s*=\\s*"([^"]+)"', t):
    print(' ', m.group(1))

# 搜原版有没有"只能装备一个"的物品（equipLimit / unique 等）
print()
print('=== 搜索装备限制字段 ===')
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
            if any(x in ln for x in ['equiplimit', 'maxequip', 'onlyone', 'stacklimit', 'equippedcount']):
                if n not in seen:
                    seen.add(n)
                    print('  %-40s %s' % (n, os.path.relpath(os.path.join(root, f), base)))
print('(none found)' if not seen else '')
