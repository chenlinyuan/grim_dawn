import os, re
ex = r'c:\Users\Administrator\Desktop\工作项目\Work\Grim Dawn\_gd_extract\db\records\items\gearweapons\melee2h'
t = open(os.path.join(ex, 'b013a_sword2h.dbr'), encoding='utf-8', errors='replace').read()
print('lines:', t.count('\n'))
keys = ['templateName', 'Class', 'itemNameTag', 'itemLevel', 'levelRequirement',
        'itemClassification', 'itemStyleTag', 'itemSkillName', 'itemSkillAutoController',
        'itemSkillLevelEq', 'offensivePhysicalMin', 'offensivePhysicalMax',
        'FileDescription', 'itemCostName']
for k in keys:
    m = re.search('^' + k + ',(.*)$', t, re.M)
    print('  %s = %s' % (k, m.group(1) if m else '(none)'))
