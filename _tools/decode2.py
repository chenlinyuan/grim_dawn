import struct

path = r'H:\SteamLibrary\steamapps\common\Grim Dawn\mods\StarterGodWeapon\database\StarterGodWeapon.arz'
d = open(path, 'rb').read()
ver, off1, c1, c2, off2, sz2, flags, x = struct.unpack_from('<IIIIIIII', d, 0)
print(f'ver=0x{ver:X} off1={off1} c1={c1} c2={c2} off2={off2} sz2={sz2} flags=0x{flags:X}')

# Build the string table from off1
strings = []
p = off1
for i in range(c1):
    ln = struct.unpack_from('<I', d, p)[0]; p += 4
    s = d[p:p+ln].decode('latin1'); p += ln
    strings.append(s)
print(f'parsed {len(strings)} strings, off1 section ends at {p}')

# Record data section is from 32 to off1
print(f'\nrecord data section: 32 .. {off1} ({off1-32} bytes)')
# Dump first 200 bytes of record data
print('first 200 bytes:')
for i in range(32, min(232, off1), 16):
    chunk = d[i:i+16]
    print(f'  {i:05X}: ' + ' '.join(f'{c:02X}' for c in chunk))
