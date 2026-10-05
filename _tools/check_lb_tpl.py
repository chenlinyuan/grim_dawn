import os, re

p = r'H:\SteamLibrary\steamapps\common\Grim Dawn\Working\database\templates\skill_attackradiuslightning.tpl'
t = open(p, encoding='utf-8', errors='replace').read()
print('=== includes ===')
for m in re.finditer('defaultValue\\s*=\\s*"([^"]*[Tt]emplate[^"]*)"', t):
    print(' ', m.group(1))
print()
print('=== all fields ===')
for m in re.finditer('name\\s*=\\s*"([^"]+)"', t):
    print(' ', m.group(1))
