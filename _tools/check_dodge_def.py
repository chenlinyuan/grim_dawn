import os, re

p = r'H:\SteamLibrary\steamapps\common\Grim Dawn\Working\database\templates\backup\parameters_character.tpl'
t = open(p, encoding='utf-8', errors='replace').read()
i = t.find('characterDodgePercent')
print('=== characterDodgePercent 定义 ===')
print(t[max(0, i - 120):i + 320])
print()
print('=== 所有 dodge/deflect 字段 ===')
for m in re.finditer('name\\s*=\\s*"([^"]+)"', t):
    n = m.group(1)
    if 'dodge' in n.lower() or 'deflect' in n.lower():
        print(' ', n)
