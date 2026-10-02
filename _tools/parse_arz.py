import struct, sys, os

def parse(path):
    with open(path, 'rb') as f:
        data = f.read()
    print(f"File: {path}  size={len(data)}")
    off = 0
    ver = struct.unpack_from('<I', data, 0)[0]
    print(f"  version field: 0x{ver:08X}")
    # Try to interpret as: u32 version, u32 dataOffset, u32 numRecords, u32 numFiles
    a = struct.unpack_from('<IIII', data, 0)
    print(f"  u32[0..3]: {[hex(x) for x in a]}")
    b = struct.unpack_from('<IIIIIIII', data, 0)
    print(f"  u32[0..7]: {[hex(x) for x in b]}")
    # print first 96 bytes
    print("  first 96 bytes hex:")
    for i in range(0, min(96, len(data)), 16):
        chunk = data[i:i+16]
        print(f"    {i:04X}: " + ' '.join(f'{c:02X}' for c in chunk) + "  " + ''.join(chr(c) if 32<=c<127 else '.' for c in chunk))

for p in sys.argv[1:]:
    parse(p)
    print()
