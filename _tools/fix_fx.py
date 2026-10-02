import os, re

mod = r'H:\SteamLibrary\steamapps\common\Grim Dawn\mods\StarterGodWeapon'
p = os.path.join(mod, 'database', 'Records', 'Items', 'GearWeapons', 'Swords1h', 'item_startergodsword.dbr')
lines = open(p, encoding='ascii').read().splitlines()

# 用 Ortus (d008_sword) 的模型配置：发光神话剑外观
mesh_updates = {
    'mesh': 'items/gearweapons/swords1h/sword1h_045a_01.msh',
    'baseTexture': 'items/gearweapons/swords1h/sword1h_045a_02_dif.tex',
    'bumpTexture': 'items/gearweapons/swords1h/sword1h_045a_02_nml.tex',
    'bitmap': 'items/gearweapons/swords1h/bitmaps/d008_sword.tex',
}

out = []
has_glow = False
for ln in lines:
    k = ln.split(',')[0]
    if k in mesh_updates:
        out.append(k + ',' + mesh_updates[k] + ',')
    else:
        out.append(ln)
        if k == 'bumpTexture':
            out.append('glowTexture,items/gearweapons/swords1h/sword1h_045a_02_glo.tex,')
            has_glow = True

# 若 bumpTexture 后没插（顺序问题），在 mesh 后插
if not has_glow:
    final = []
    for ln in out:
        final.append(ln)
        if ln.startswith('mesh,'):
            final.append('glowTexture,items/gearweapons/swords1h/sword1h_045a_02_glo.tex,')
    out = final

open(p, 'w', encoding='ascii', newline='\n').write('\n'.join(out) + '\n')
print('glowTexture added:', has_glow or True)
for ln in out:
    k = ln.split(',')[0]
    if any(x in k.lower() for x in ['mesh', 'texture', 'glow', 'trail', 'bitmap']):
        print(' ', ln)
