import os, re

# 我们武器记录的字段顺序
p = r'H:\SteamLibrary\steamapps\common\Grim Dawn\mods\StarterGodWeapon\database\Records\Items\GearWeapons\Swords1h\item_startergodsword.dbr'
lines = open(p, encoding='ascii').read().splitlines()
print('=== 我们武器记录字段顺序（前 30）===')
for i, l in enumerate(lines[:30]):
    print(' ', i, l.split(',')[0])

# 原版 a02_sword001 的字段顺序（作为正确参考）
ex = r'c:\Users\Administrator\Desktop\工作项目\Work\Grim Dawn\_gd_extract\db\records\items\gearweapons\swords1h\a02_sword001.dbr'
van = open(ex, encoding='utf-8', errors='replace').read().splitlines()
print()
print('=== 原版 a02_sword001 字段顺序（前 30）===')
for i, l in enumerate(van[:30]):
    print(' ', i, l.split(',')[0])
