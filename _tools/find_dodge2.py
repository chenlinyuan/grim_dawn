import os, re

# 直接搜原版装备的闪避字段（defensiveDodge / characterDodge / dodgeChance 等）
ex = r'c:\Users\Administrator\Desktop\工作项目\Work\Grim Dawn\_gd_extract\db\records\items'
found = {}
for root, dirs, files in os.walk(ex):
    for f in files:
        if not f.endswith('.dbr'):
            continue
        p = os.path.join(root, f)
        try:
            t = open(p, encoding='utf-8', errors='replace').read()
        except Exception:
            continue
        for m in re.finditer(r'^([a-zA-Z]*[Dd]odge[a-zA-Z]*),([^,\r\n]+),', t, re.M):
            k = m.group(1)
            v = m.group(2).strip()
            if v not in ('0', '0.000000', '') and k not in found:
                found[k] = (os.path.relpath(p, ex), v)

print('=== 原版装备的 dodge 字段 ===')
for k, (path, v) in found.items():
    print('  %-40s = %-12s (%s)' % (k, v, path))

# 也搜 characterDodge / defensiveDodge 在模板里
print()
print('=== 模板里的 dodge 字段 ===')
base = r'H:\SteamLibrary\steamapps\common\Grim Dawn\Working\database\templates'
seen = set()
for root, dirs, files in os.walk(base):
    for f in files:
        if not f.endswith('.tpl'):
            continue
        try:
            t = open(os.path.join(root, f), encoding='utf-8', errors='replace').read()
        except Exception:
            continue
        for m in re.finditer('name\\s*=\\s*"([^"]*[Dd]odge[^"]*)"', t):
            n = m.group(1)
            if n not in seen:
                seen.add(n)
                print('  %-40s %s' % (n, os.path.relpath(os.path.join(root, f), base)))
