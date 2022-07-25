import json
with open('json_text.json', 'r',) as f:
    data = json.load(f)
for txt in data:
    print(txt)
