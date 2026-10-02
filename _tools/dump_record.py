import struct

d = open(r'H:\SteamLibrary\steamapps\common\Grim Dawn\mods\StarterGodWeapon\database\StarterGodWeapon.arz', 'rb').read()
ver, off1, c1, c2, off2, sz2, flags, x = struct.unpack_from('<IIIIIIII', d, 0)
p = off2
cnt = struct.unpack_from('<I', d, p)[0]; p += 4
entries = []
for k in range(cnt):
    ln = struct.unpack_from('<I', d, p)[0]; p += 4
    s = d[p:p+ln].decode('latin1'); p += ln
    entries.append(s)

# Find the chestloot_all_b01 record's field block
idx = None
for i, e in enumerate(entries):
    if e.endswith('chestloot_all_b01.dbr'):
        idx = i
        break
print("chestloot_all_b01 at index", idx)
if idx is not None:
    print("--- context around it ---")
    for j in range(max(0, idx-2), min(len(entries), idx+80)):
        print(f'[{j}] {entries[j]}')
