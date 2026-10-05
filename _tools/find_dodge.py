import os, re

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
        for m in re.finditer('name\\s*=\\s*"([^"]+)"', t):
            n = m.group(1)
            ln = n.lower()
            if any(x in ln for x in ['dodge', 'evade', 'evasion', 'deflect', 'chance', 'avoid']):
                if n not in seen:
                    seen.add(n)
                    print('%-42s %s' % (n, os.path.relpath(os.path.join(root, f), base)))

# 原版装备用闪避字段的例子
print()
print('=== 原版装备用 dodge/evade 字段 ===')
ex = r'c:\Users\Administrator\Desktop\工作项目\Work\Grim Dawn\_gd_extract\db\records\items'
cnt = 0
for root, dirs, files in os.walk(ex):
    for f in files:
        if not f.endswith('.dbr'):
            continue
        p = os.path.join(root, f)
        try:
            t = open(p, encoding='utf-8', errors='replace').read()
        except Exception:
            continue
        for m in re.finditer(r'^([a-zA-Z]*(?:[Dd]odge|[Ee]vade|[Ee]vasion)[a-zA-Z]*),([^,\r\n]+),', t, re.M):
            v = m.group(2).strip()
            if v not in ('0', '0.000000', ''):
                print('  %-50s %s = %s' % (os.path.relpath(p, ex), m.group(1), v))
                cnt += 1
                break
    if cnt > 15:
        break
