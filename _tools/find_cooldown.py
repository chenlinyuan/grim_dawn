import os, re

# 1. 找"技能冷却缩减"字段
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
            if ('cooldown' in ln or 'recharge' in ln or 'recovery' in ln) and n not in seen:
                seen.add(n)
                print('%-42s %s' % (n, os.path.relpath(os.path.join(root, f), base)))

# 2. 原版装备用这些字段的例子
print()
print('=== 原版装备用 cooldown 字段的例子 ===')
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
        for m in re.finditer(r'^([a-zA-Z]*[Cc]ooldown[a-zA-Z]*),([^,\r\n]+),', t, re.M):
            val = m.group(2).strip()
            if val not in ('0', '0.000000', ''):
                print('  %-50s %s = %s' % (os.path.relpath(p, ex), m.group(1), val))
                cnt += 1
                break
    if cnt > 20:
        break
