import json

with open('json/skinlist.json', 'r') as f:
    d = json.loads(f.read())

o = []

for i in d:
    if not i.startswith('\u2605'):
        o.append(i)

with open('json/skinlist2.json', 'w') as f:
    f.write(json.dumps(o))