import os, re

# 1. 确认 characterIncreasedExperience 在正式模板里
base = r'H:\SteamLibrary\steamapps\common\Grim Dawn\Working\database\templates'
print('=== characterIncreasedExperience 所在模板 ===')
for root, dirs, files in os.walk(base):
    for f in files:
        if not f.endswith('.tpl'):
            continue
        try:
            t = open(os.path.join(root, f), encoding='utf-8', errors='replace').read()
        except Exception:
            continue
        if re.search('name\\s*=\\s*"characterIncreasedExperience"', t):
            print('  ', os.path.relpath(os.path.join(root, f), base))

# 2. 原版哪些装备用它
ex = r'c:\Users\Administrator\Desktop\工作项目\Work\Grim Dawn\_gd_extract\db\records\items'
print()
print('=== 原版装备使用 characterIncreasedExperience 的例子 ===')
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
        if 'characterIncreasedExperience' in t:
            m = re.search(r'^characterIncreasedExperience,(.*)$', t, re.M)
            print('  %-55s %s' % (os.path.relpath(p, ex), m.group(1) if m else '?'))
            cnt += 1
            if cnt > 15:
                break
    if cnt > 15:
        break
