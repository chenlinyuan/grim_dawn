import os, re

ex = r'c:\Users\Administrator\Desktop\工作项目\Work\Grim Dawn\_gd_extract\db\records\items'
cnt = 0
for root, dirs, files in os.walk(ex):
    for f in files:
        if not f.endswith('.dbr'):
            continue
        p = os.path.join(root, f)
        try:
            t = open(p, encoding='utf-8', errors='replace').read()
        except Exception:
            continue
        m = re.search(r'^attributeScalePercent,(.*)$', t, re.M)
        if m and m.group(1).strip() in ('0.000000', '0'):
            print(os.path.relpath(p, ex), '-> attributeScalePercent =', m.group(1))
            cnt += 1
            if cnt > 12:
                break
    if cnt > 12:
        break
print('total found:', cnt)
