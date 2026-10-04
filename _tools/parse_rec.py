import struct

d = open(r'H:\SteamLibrary\steamapps\common\Grim Dawn\mods\StarterGodWeapon\database\StarterGodWeapon.arz', 'rb').read()
ver, off1, c1, c2, off2, sz2, flags, x = struct.unpack_from('<IIIIIIII', d, 0)

# 记录数据区 off2..off2+sz2
# 从 dump 看第一个记录: [len][name][len]templateName[len][val]FileDescription[len][val]...
# 即 字段名和值交替！但 attributeScalePercent 后跟 baseTexture -> 值被省略
# 让me完整解析第一个记录，看模式

p = off2
ln = struct.unpack_from('<I', d, p)[0]; p += 4
name = d[p:p+ln].decode('latin1'); p += ln
print('record:', name)
print()
# 尝试交替解析
count = 0
while p < off2 + sz2 and count < 40:
    # 读字段名
    fl = struct.unpack_from('<I', d, p)[0]
    if fl == 0 or fl > 200:
        print('  [stop] fl=%d at %d' % (fl, p))
        break
    p += 4
    fname = d[p:p+fl].decode('latin1'); p += fl
    # 读值长度
    vl = struct.unpack_from('<I', d, p)[0]; p += 4
    if vl == 0xFFFFFFFF or vl > 100000:
        val = '<null/end>'
    else:
        val = d[p:p+vl].decode('latin1'); p += vl
    print('  %-34s = %s' % (fname, val[:50]))
    count += 1
