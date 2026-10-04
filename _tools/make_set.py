import os

mod = r'H:\SteamLibrary\steamapps\common\Grim Dawn\mods\StarterGodWeapon'

# 创建物品套装（只含灵魂暗戒）
set_dir = os.path.join(mod, 'database', 'Records', 'Items', 'LootSets')
os.makedirs(set_dir, exist_ok=True)
set_content = (
    'templateName,database/templates/itemset.tpl,\n'
    'FileDescription,Soul Ring Set,\n'
    'itemLevel,1,\n'
    'setDescription,tagSoulRingSetDesc,\n'
    'setMembers,records/items/gearaccessories/rings/soul_ring.dbr,\n'
    'setName,tagSoulRingSetName,\n'
    'setSize,1,\n'
)
open(os.path.join(set_dir, 'itemset_soulring.dbr'), 'w', encoding='ascii', newline='\n').write(set_content)
print('created itemset_soulring.dbr')

# 让戒指引用套装
rp = os.path.join(mod, 'database', 'Records', 'Items', 'GearAccessories', 'Rings', 'soul_ring.dbr')
lines = open(rp, encoding='ascii').read().splitlines()
out = []
for ln in lines:
    out.append(ln)
    if ln.startswith('itemNameTag,'):
        out.append('itemSetName,records/items/lootsets/itemset_soulring.dbr,')
open(rp, 'w', encoding='ascii', newline='\n').write('\n'.join(out) + '\n')
print('added itemSetName to ring')
for l in out:
    if l.startswith(('itemNameTag', 'itemSetName')):
        print(' ', l)
