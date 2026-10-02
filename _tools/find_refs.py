import os, sys

ROOT = r'H:\SteamLibrary\steamapps\common\Grim Dawn\Working\database\records'
needle = sys.argv[1] if len(sys.argv) > 1 else 'lowercrossing'
hits = []
for dp, dn, fn in os.walk(ROOT):
    for f in fn:
        if not f.lower().endswith('.dbr'):
            continue
        p = os.path.join(dp, f)
        try:
            with open(p, 'rb') as fh:
                data = fh.read()
        except Exception:
            continue
        if needle.encode('latin1') in data:
            hits.append(p.replace(ROOT + '\\', ''))
for h in hits[:40]:
    print(h)
print('TOTAL:', len(hits))
