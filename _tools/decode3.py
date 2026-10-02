import struct

path = r'H:\SteamLibrary\steamapps\common\Grim Dawn\mods\StarterGodWeapon\database\StarterGodWeapon.arz'
d = open(path, 'rb').read()
ver, off1, c1, c2, off2, sz2, flags, x = struct.unpack_from('<IIIIIIII', d, 0)
print(f'ver=0x{ver:X} off1={off1} c1={c1} c2={c2} off2={off2} sz2={sz2} flags=0x{flags:X} size={len(d)}')

# String table is at off1. Format: sequence of (u32 len, bytes) OR (u32 count, then...)
# From earlier: at off1 we saw "46 26 00 00" = 0x2646 = 9798 -> looks like a length.
# Let's just try: u32 len then bytes, repeated.
p = off1
strings = []
ok = True
for i in range(c1):
    if p + 4 > len(d):
        ok = False; break
    ln = struct.unpack_from('<I', d, p)[0]; p += 4
    if ln > 5000 or p + ln > len(d):
        ok = False
        print(f'  string[{i}] bad len={ln} at {p}')
        break
    s = d[p:p+ln].decode('latin1'); p += ln
    strings.append(s)
print(f'string table parse ok={ok}, got {len(strings)} strings, end at {p}')

if ok:
    # find indices of key strings
    def idx(s):
        try:
            return strings.index(s)
        except ValueError:
            return None
    for s in ['chestloot_all_b01.dbr', 'lt_startergodsword.dbr', 'mt_hu_miscrare_a01.dbr', 'loot2Name2', 'loot2Name1']:
        print(f'  "{s}" -> index {idx(s)}')
