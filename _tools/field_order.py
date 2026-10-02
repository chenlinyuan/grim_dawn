import os, re

# 1. attributeScalePercent 在 ItemEquipment.tpl 的顺序
p1 = r'H:\SteamLibrary\steamapps\common\Grim Dawn\Working\database\templates\TemplateBase\ItemEquipment.tpl'
t1 = open(p1, encoding='utf-8', errors='replace').read()
names1 = re.findall('name\\s*=\\s*"([^"]+)"', t1)
print('=== ItemEquipment.tpl 字段顺序 ===')
for i, n in enumerate(names1):
    print(' ', i, n)

# 2. skillTargetRadius 在 skill_attackradiuslightning.tpl 相关模板的顺序
print()
print('=== 查找 skillTargetRadius 所在模板 ===')
base = r'H:\SteamLibrary\steamapps\common\Grim Dawn\Working\database\templates'
for root, dirs, files in os.walk(base):
    for f in files:
        if not f.endswith('.tpl'):
            continue
        try:
            t = open(os.path.join(root, f), encoding='utf-8', errors='replace').read()
        except Exception:
            continue
        if 'skillTargetRadius' in t:
            names = re.findall('name\\s*=\\s*"([^"]+)"', t)
            print('  ', os.path.relpath(os.path.join(root, f), base))
