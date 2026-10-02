import struct

path = r'H:\SteamLibrary\steamapps\common\Grim Dawn\mods\StarterGodWeapon\database\StarterGodWeapon.arz'
d = open(path, 'rb').read()
ver, off1, c1, c2, off2, sz2, flags, x = struct.unpack_from('<IIIIIIII', d, 0)

# The file list section (off2) contains: for each record, the record path then its
# field names and values as strings. Let's parse it and find the b01 block.
p = off2
cnt = struct.unpack_from('<I', d, p)[0]; p += 4
entries = []
for k in range(cnt):
    ln = struct.unpack_from('<I', d, p)[0]; p += 4
    s = d[p:p+ln].decode('latin1'); p += ln
    entries.append(s)

# Find the b01 record and print everything until the next record path
start = None
for i, e in enumerate(entries):
    if e.endswith('chestloot_all_b01.dbr'):
        start = i
        break
print("b01 record block starts at", start)
if start is not None:
    for j in range(start, min(start + 60, len(entries))):
        e = entries[j]
        # mark record paths
        tag = ' <-- RECORD' if e.endswith('.dbr') else ''
        print(f'[{j}] {e}{tag}')
