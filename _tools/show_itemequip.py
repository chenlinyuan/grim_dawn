import os, re

p = r'H:\SteamLibrary\steamapps\common\Grim Dawn\Working\database\templates\TemplateBase\ItemEquipment.tpl'
t = open(p, encoding='utf-8', errors='replace').read()
print('len', len(t))
print('=== all variable names ===')
for m in re.finditer('name\\s*=\\s*"([^"]+)"', t):
    print(' ', m.group(1))
print()
print('=== attributeScalePercent context ===')
i = t.find('attributeScalePercent')
print(t[max(0, i - 200):i + 300])
