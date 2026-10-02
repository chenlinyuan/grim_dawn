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

# Show the new loot table record
for i, e in enumerate(entries):
    if 'chestloot_sgw_corpse' in e and e.endswith('.dbr'):
        print("=== chestloot_sgw_corpse record ===")
        for j in range(i, min(i + 12, len(entries))):
            print(f'  [{j}] {entries[j]}')
        break

# Show the corpse override
for i, e in enumerate(entries):
    if 'a01_chestcorpse01_lowercrossing' in e and e.endswith('.dbr'):
        print("=== corpse record ===")
        for j in range(i, min(i + 30, len(entries))):
            if entries[j] == 'lootTable':
                print(f'  [{j}] lootTable -> {entries[j+1]}')
        break
