import os, re

base = r'H:\SteamLibrary\steamapps\common\Grim Dawn\Working\database\templates'
print('=== 范围/新星类技能模板 ===')
for root, dirs, files in os.walk(base):
    for f in files:
        if not f.endswith('.tpl'):
            continue
        ln = f.lower()
        if any(x in ln for x in ['radius', 'nova', 'spin', 'wave', 'burst', 'ring', 'circle', 'explos']):
            print('  ', os.path.relpath(os.path.join(root, f), base))

# 原版有哪些"新星"技能（找 skill_attackradius* 的技能记录）
print()
print('=== 原版 skill_attackradius* 技能记录 ===')
ex = r'c:\Users\Administrator\Desktop\工作项目\Work\Grim Dawn\_gd_extract\db\records\skills'
for root, dirs, files in os.walk(ex):
    for f in files:
        if not f.endswith('.dbr'):
            continue
        p = os.path.join(root, f)
        try:
            t = open(p, encoding='utf-8', errors='replace').read()
        except Exception:
            continue
        m = re.search(r'^templateName,(.*)$', t, re.M)
        if m and 'skill_attackradius' in m.group(1):
            print('  %-55s %s' % (os.path.relpath(p, ex), m.group(1)))
