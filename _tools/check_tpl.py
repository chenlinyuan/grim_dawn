p = r'H:\SteamLibrary\steamapps\common\Grim Dawn\Working\database\templates\fixeditemcontainer.tpl'
lines = open(p, encoding='latin1').read().split('\n')
for i, l in enumerate(lines):
    if 'lootTable' in l:
        print('--- at', i, '---')
        for j in range(max(0, i - 1), min(i + 6, len(lines))):
            print(f'  {j}: {lines[j]}')
