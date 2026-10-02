import os, re

p = r'H:\SteamLibrary\steamapps\common\Grim Dawn\Working\database\templates\TemplateBase\skill_radius.tpl'
t = open(p, encoding='utf-8', errors='replace').read()
names = re.findall('name\\s*=\\s*"([^"]+)"', t)
print('=== skill_radius.tpl 字段顺序 ===')
for i, n in enumerate(names):
    print(' ', i, n)

# 我们的技能记录字段顺序
sp = r'H:\SteamLibrary\steamapps\common\Grim Dawn\mods\StarterGodWeapon\database\Records\Skills\ItemSkills\Legendary\item_heavenstrike.dbr'
sl = open(sp, encoding='ascii').read().splitlines()
print()
print('=== 我们技能记录的字段顺序（前 40）===')
for i, l in enumerate(sl[:40]):
    print(' ', i, l.split(',')[0])
print('...')
# skillTargetRadius 的位置
for i, l in enumerate(sl):
    if l.startswith('skillTargetRadius') or l.startswith('skillCooldownTime') or l.startswith('skillDisplayName'):
        print('  [%d] %s' % (i, l))
