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

print("total entries:", len(entries))
print("--- fields after index 759 (the b01 record) ---")
for i in range(759, len(entries)):
    if entries[i] in ('loot2Name1', 'loot2Name2', 'loot2Chance', 'loot1Name1', 'loot1Name2'):
        nxt = entries[i+1] if i+1 < len(entries) else '?'
        print('[%d] %s -> %s' % (i, entries[i], nxt))
