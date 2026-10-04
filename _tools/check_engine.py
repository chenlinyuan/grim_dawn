import os, re

p = r'H:\SteamLibrary\steamapps\common\Grim Dawn\Working\database\templates\gameengine.tpl'
print('exists:', os.path.exists(p))
if os.path.exists(p):
    t = open(p, encoding='utf-8', errors='replace').read()
    print('len', len(t))
    for m in re.finditer('name\\s*=\\s*"([^"]+)"', t):
        n = m.group(1)
        if any(x in n.lower() for x in ['scale', 'random', 'loot', 'item']):
            print(' ', n)
