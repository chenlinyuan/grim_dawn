import json
p = r'c:\Users\Administrator\AppData\Roaming\Code\User\workspaceStorage\8ac41c2438d711a510d7bd3f488d1c6b\GitHub.copilot-chat\transcripts\1bf9f2d0-2cbf-4a8b-91c8-eb581a969a71.jsonl'
lines = open(p, encoding='utf-8').read().splitlines()
# 在成功("这次有了" line 2992)之前找对这3个文件的修改
for j in range(2500, 2992):
    try:
        o = json.loads(lines[j])
    except Exception:
        continue
    s = json.dumps(o, ensure_ascii=False)
    for kw in ['chestloot_rackweapon_b01', 'chestloot_intropotions', 'mt_gearweapons_a01']:
        if kw in s and ('replace' in s or 'create_file' in s or 'Set-Content' in s or 'WriteAllText' in s):
            # 打印包含修改内容的片段
            idx = s.find(kw)
            print('=== line', j, o.get('type'), 'kw:', kw, '===')
            print(s[max(0, idx - 700):idx + 700])
            print()
            break
