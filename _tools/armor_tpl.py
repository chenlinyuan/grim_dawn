import os, re

# 1. Armor.tpl 字段
p = r'H:\SteamLibrary\steamapps\common\Grim Dawn\Working\database\templates\TemplateBase\Armor.tpl'
t = open(p, encoding='utf-8', errors='replace').read()
print('=== Armor.tpl includes ===')
for m in re.finditer('defaultValue\\s*=\\s*"([^"]*[Tt]emplate[^"]*)"', t):
    print(' ', m.group(1))
print()
print('=== Armor.tpl 所有字段 ===')
for m in re.finditer('name\\s*=\\s*"([^"]+)"', t):
    print(' ', m.group(1))

# 2. 搜 itemequipment.tpl 里可能的"限制"字段
p2 = r'H:\SteamLibrary\steamapps\common\Grim Dawn\Working\database\templates\TemplateBase\ItemEquipment.tpl'
t2 = open(p2, encoding='utf-8', errors='replace').read()
print()
print('=== ItemEquipment.tpl 所有字段 ===')
for m in re.finditer('name\\s*=\\s*"([^"]+)"', t2):
    print(' ', m.group(1))
