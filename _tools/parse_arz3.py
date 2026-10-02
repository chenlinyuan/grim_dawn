import struct

d = open(r'H:\SteamLibrary\steamapps\common\Grim Dawn\mods\StarterGodWeapon\database\StarterGodWeapon.arz', 'rb').read()
ver, off1, c1, c2, off2, sz2, flags, x = struct.unpack_from('<IIIIIIII', d, 0)

# 记录数据区: off2..off2+sz2
# 格式: [记录名][字段名块][值块] 循环, 但需要确定块边界
# 观察: 每个字符串前有 4 字节长度. 记录名后紧跟 templateName 字段名...
# 尝试: 记录 = 名 + (字段名,值) 交替, 但值块在末尾
# 从 dump 看: 名, 然后 templateName, <值>, FileDescription, <值>... 是交替的!
# 但 attributeScalePercent 后跟 baseTexture -> 说明 attributeScalePercent 的值是空/省略

# 用交替解析
p = off2
records = []
for rec_i in range(c2):
    ln = struct.unpack_from('<I', d, p)[0]; p += 4
    name = d[p:p+ln].decode('latin1'); p += ln
    fields = {}
    # 交替读取, 直到遇到下一个记录名 (以 .dbr 结尾且看起来像记录)
    while p < off2 + sz2:
        if p + 4 > len(d):
            break
        fl = struct.unpack_from('<I', d, p)[0]
        if fl == 0 or fl > 500:
            break
        p += 4
        fname = d[p:p+fl].decode('latin1'); p += fl
        # 读值
        vl = struct.unpack_from('<I', d, p)[0]; p += 4
        if vl == 0xFFFFFFFF:
            val = None
        else:
            val = d[p:p+vl].decode('latin1'); p += vl
        fields[fname] = val
        # 检测下一记录名
        if fname.endswith('.dbr') and vl > 0:
            pass
    records.append((name, fields))
    if rec_i > 10:
        break

for name, fields in records:
    if 'startergodsword' in name or 'heavenstrike' in name:
        print('===', name, '===')
        for k in ['attributeScalePercent', 'bitmap', 'itemNameTag', 'characterLife',
                  'characterDexterityModifier', 'offensiveLightningModifier', 'conversionPercentage',
                  'skillTargetRadius', 'skillCooldownTime', 'skillMaxLevel', 'skillDisplayName']:
            if k in fields:
                print('   %-34s = %s' % (k, fields[k]))
