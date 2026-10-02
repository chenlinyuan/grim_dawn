import os, re

base = r'H:\SteamLibrary\steamapps\common\Grim Dawn\Working\database\templates'
targets = ['glowTexture', 'mesh', 'bitmap', 'baseTexture', 'bumpTexture', 'itemStyleTag', 'attackEffect']
hits = {k: [] for k in targets}
for root, dirs, files in os.walk(base):
    for f in files:
        if not f.endswith('.tpl'):
            continue
        p = os.path.join(root, f)
        try:
            t = open(p, encoding='utf-8', errors='replace').read()
        except Exception:
            continue
        for k in targets:
            if re.search('name\\s*=\\s*"' + k + '"', t):
                hits[k].append(os.path.relpath(p, base))

for k, v in hits.items():
    print('===', k, '===')
    for x in v:
        print('  ', x)
