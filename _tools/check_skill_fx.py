import os, re

# 1. skill_attackweaponradius.tpl 支持的特效字段
p = r'H:\SteamLibrary\steamapps\common\Grim Dawn\Working\database\templates\skill_attackweaponradius.tpl'
t = open(p, encoding='utf-8', errors='replace').read()
print('=== skill_attackweaponradius.tpl includes ===')
for m in re.finditer('defaultValue\\s*=\\s*"([^"]*[Tt]emplate[^"]*)"', t):
    print(' ', m.group(1))
print()
print('=== 该模板所有字段 ===')
for m in re.finditer('name\\s*=\\s*"([^"]+)"', t):
    print(' ', m.group(1))

# 2. 找原版"天降雷霆"特效资源
print()
print('=== 雷电相关 FX 资源 ===')
for base in [r'c:\Users\Administrator\Desktop\工作项目\Work\Grim Dawn\_gd_extract\db\records\fx\skillsother',
             r'c:\Users\Administrator\Desktop\工作项目\Work\Grim Dawn\_gd_extract\db\records\fx\skillsother\rangeddirect']:
    if os.path.exists(base):
        for f in sorted(os.listdir(base)):
            if 'lightning' in f.lower() or 'bolt' in f.lower() or 'thunder' in f.lower():
                print(' ', os.path.relpath(os.path.join(base, f), base))
