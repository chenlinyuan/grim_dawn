import struct

d = open(r'H:\SteamLibrary\steamapps\common\Grim Dawn\mods\StarterGodWeapon\database\StarterGodWeapon.arz', 'rb').read()
ver, off1, c1, c2, off2, sz2, flags, x = struct.unpack_from('<IIIIIIII', d, 0)

# 数据区: off2 开始，记录序列
p = off2
for rec_i in range(c2):
    ln = struct.unpack_from('<I', d, p)[0]; p += 4
    name = d[p:p+ln].decode('latin1'); p += ln
    # 记录体: 字段数
    nfields = struct.unpack_from('<I', d, p)[0]; p += 4
    print('=== [%d] %s (%d fields) ===' % (rec_i, name, nfields))
    for fi in range(nfields):
        fl = struct.unpack_from('<I', d, p)[0]; p += 4
        fname = d[p:p+fl].decode('latin1'); p += fl
        vl = struct.unpack_from('<I', d, p)[0]; p += 4
        if vl == 0xFFFFFFFF:
            val = '<null>'
        else:
            val = d[p:p+vl].decode('latin1'); p += vl
        if name.endswith('item_startergodsword.dbr') and fname in (
                'attributeScalePercent', 'bitmap', 'itemNameTag', 'characterLife',
                'characterDexterityModifier', 'offensiveLightningModifier', 'conversionPercentage'):
            print('   %-34s = %s' % (fname, val))
        if name.endswith('item_heavenstrike.dbr') and fname in (
                'skillTargetRadius', 'skillCooldownTime', 'skillDisplayName', 'skillMaxLevel'):
            print('   %-34s = %s' % (fname, val))
    if rec_i > 12:
        break
