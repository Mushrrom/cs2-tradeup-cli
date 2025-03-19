import json

with open('json/skins-bad.json', 'r', encoding='utf-8') as f:
    b = json.loads(f.read())

out = {}

for i in b:
    out[i['name']] = i

with open('json/skins.json', 'w') as f:
    f.write(json.dumps(out))