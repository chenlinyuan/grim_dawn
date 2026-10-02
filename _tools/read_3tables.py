import os, re
ex = r'c:\Users\Administrator\Desktop\工作项目\Work\Grim Dawn\_gd_extract\db\records'
for rel in ['items\\lootchests\\chestloottables\\chestloot_rackweapon_b01.dbr',
            'items\\lootchests\\questchests\\questchestloottables\\chestloot_intropotions.dbr',
            'items\\loottables\\mastertables\\mt_gearweapons_a01.dbr']:
    p = os.path.join(ex, rel)
    print('=' * 20, rel, '=' * 20)
    if os.path.exists(p):
        print(open(p, encoding='utf-8', errors='replace').read())
    else:
        print('MISSING')
    print()
