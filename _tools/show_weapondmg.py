import os, re

# 1. weaponDamagePct 定义
p = r'H:\SteamLibrary\steamapps\common\Grim Dawn\Working\database\templates\TemplateBase\skill_base.tpl'
t = open(p, encoding='utf-8', errors='replace').read()
i = t.find('weaponDamagePct')
print('=== weaponDamagePct 定义 ===')
print(t[max(0, i - 150):i + 250])

# 2. 原版用 weaponDamagePct 的技能（尤其新星/范围）
print()
print('=== 原版用 weaponDamagePct 的技能（示例）===')
ex = r'c:\Users\Administrator\Desktop\工作项目\Work\Grim Dawn\_gd_extract\db\records\skills'
cnt = 0
for root, dirs, files in os.walk(ex):
    for f in files:
        if not f.endswith('.dbr'):
            continue
        p2 = os.path.join(root, f)
        try:
            tt = open(p2, encoding='utf-8', errors='replace').read()
        except Exception:
            continue
        m = re.search(r'^weaponDamagePct,(.*)$', tt, re.M)
        if m and m.group(1).strip() not in ('', '0', '0.000000'):
            print('  %-55s weaponDamagePct=%s' % (os.path.relpath(p2, ex), m.group(1)))
            cnt += 1
            if cnt > 20:
                break
    if cnt > 20:
        break
