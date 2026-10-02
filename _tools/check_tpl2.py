import os, re

candidates = [
    r'H:\SteamLibrary\steamapps\common\Grim Dawn\Working\database\templates\weapon_sword.tpl',
    r'H:\SteamLibrary\steamapps\common\Grim Dawn\Working\templates\weapon_sword.tpl',
]
p = next((c for c in candidates if os.path.exists(c)), None)
print('template:', p)
if p:
    t = open(p, encoding='utf-8', errors='replace').read()
    for kw in ['weaponTrail', 'glowTexture', 'itemMesh', 'mesh', 'bitmap']:
        hits = re.findall(r'name\s*=\s*"' + kw + r'".*?(?=name\s*=|\Z)', t, re.S)
        for h in hits[:1]:
            print('---', kw, '---')
            print(h[:260].strip())
