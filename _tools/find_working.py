import json
p = r'c:\Users\Administrator\AppData\Roaming\Code\User\workspaceStorage\8ac41c2438d711a510d7bd3f488d1c6b\GitHub.copilot-chat\transcripts\1bf9f2d0-2cbf-4a8b-91c8-eb581a969a71.jsonl'
lines = open(p, encoding='utf-8').read().splitlines()
for j in range(2974, 2992):
    try:
        o = json.loads(lines[j])
    except Exception:
        continue
    s = json.dumps(o, ensure_ascii=False)
    print('=== line', j, o.get('type'), 'len', len(s), '===')
    print(s[:1200])
    print()
