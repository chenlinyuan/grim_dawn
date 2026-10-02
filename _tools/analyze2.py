import struct, sys

def analyze(path):
    d = open(path, 'rb').read()
    print(f"=== {path} size={len(d)} ===")
    ver, off1, c1, c2, off2, sz2, flags, x = struct.unpack_from('<IIIIIIII', d, 0)
    print(f"ver=0x{ver:X} off1={off1} c1={c1} c2={c2} off2={off2} sz2={sz2} flags=0x{flags:X} x={x}")
    # string table at off1
    print("--- string table @off1 ---")
    p = off1
    for k in range(6):
        if p + 4 > len(d):
            break
        ln = struct.unpack_from('<I', d, p)[0]
        p += 4
        if ln > 200 or p + ln > len(d):
            print(f"  [{k}] bad len={ln}")
            break
        s = d[p:p+ln]
        p += ln
        print(f"  [{k}] len={ln} {s[:50]!r}")
    print("--- file list @off2 ---")
    p = off2
    cnt = struct.unpack_from('<I', d, p)[0]
    p += 4
    print(f"  count={cnt}")
    for k in range(min(cnt, 4)):
        ln = struct.unpack_from('<I', d, p)[0]
        p += 4
        s = d[p:p+ln]
        p += ln
        print(f"  [{k}] len={ln} {s.decode('latin1')}")
    print(f"  tail bytes: {len(d)-p}")

for p in sys.argv[1:]:
    analyze(p)
