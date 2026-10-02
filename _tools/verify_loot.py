import struct

d = open(r'H:\SteamLibrary\steamapps\common\Grim Dawn\mods\StarterGodWeapon\database\StarterGodWeapon.arz', 'rb').read()
ver, off1, c1, c2, off2, sz2, flags, x = struct.unpack_from('<IIIIIIII', d, 0)
print(f'size={len(d)} strings={c1} files={c2}')
p = off2
cnt = struct.unpack_from('<I', d, p)[0]; p += 4
entries = []
for k in range(cnt):
    ln = struct.unpack_from('<I', d, p)[0]; p += 4
    s = d[p:p+ln].decode('latin1'); p += ln
    entries.append(s)

print()
print('loot-related records:')
for e in entries:
    if 'lootchest' in e or 'lt_startergodsword' in e or 'lowercrossing' in e:
        print('  ', e)

print()
print('loot4Name sequence:')
for i, e in enumerate(entries):
    if e in ('loot4Name1', 'loot4Name2'):
        nxt = entries[i+1] if i+1 < len(entries) else '?'
        print('  [%d] %s -> %s' % (i, e, nxt))
