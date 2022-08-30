import json
import csv
with open('json_text.json', 'r',) as f:
    data = json.load(f)
for txt in data:
    print(txt)
with open('json_test_01.csv', 'w',) as f:
    fieldnames = txt[].keys()
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writerow()
    for name in names:
        writer.writerow(name)