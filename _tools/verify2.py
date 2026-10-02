import struct

d = open(r'H:\SteamLibrary\steamapps\common\Grim Dawn\mods\StarterGodWeapon\database\StarterGodWeapon.arz', 'rb').read()
ver, off1, c1, c2, off2, sz2, flags, x = struct.unpack_from('<IIIIIIII', d, 0)
p = off2
cnt = struct.unpack_from('<I', d, p)[0]; p += 4
entries = []
for k in range(cnt):
    ln = struct.unpack_from('<I', d, p)[0]; p += 4
    s = d[p:p+ln].decode('latin1'); p += ln
    entries.append(s)

markers = ['skill_attackradiuslightning.tpl', 'AttackEnemy', 'HitByEnemy',
           'tagItemSkillHeavenStrikeName', 'item_heavenstrike.dbr', 'Skill_AttackRadiusLightning']
for m in markers:
    idx = [i for i, e in enumerate(entries) if m in e]
    status = ('FOUND ' + str(idx)) if idx else 'NOT FOUND'
    print(m, '->', status)
