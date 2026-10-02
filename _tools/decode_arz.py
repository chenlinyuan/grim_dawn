import struct

d = open(r'H:\SteamLibrary\steamapps\common\Grim Dawn\mods\StarterGodWeapon\database\StarterGodWeapon.arz', 'rb').read()
ver, off1, c1, c2, off2, sz2, flags, x = struct.unpack_from('<IIIIIIII', d, 0)
print(f'ver=0x{ver:X} off1={off1} c1={c1} c2={c2} off2={off2} sz2={sz2} flags=0x{flags:X} x={x}')
print(f'file size={len(d)}')

# The file list starts at off2. Let's parse it properly.
p = off2
cnt = struct.unpack_from('<I', d, p)[0]; p += 4
print(f'\nfile list count = {cnt}')
files = []
for k in range(cnt):
    ln = struct.unpack_from('<I', d, p)[0]; p += 4
    s = d[p:p+ln].decode('latin1'); p += ln
    files.append(s)
print(f'parsed {len(files)} files, consumed up to offset {p}')

print('\n--- files (first 30) ---')
for i, f in enumerate(files[:30]):
    print(f'  [{i}] {f}')

print('\n--- files containing loot/chest ---')
for i, f in enumerate(files):
    if 'lootchest' in f or 'loottable' in f:
        print(f'  [{i}] {f}')
