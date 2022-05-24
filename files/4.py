import csv
import json

with open('data.json') as f:
    data = json.load(f)
print(data)
with open('data.csv', "w") as f:
    fieldnames = 'id', 'name', 'age', "tel"
    writer = csv.writer(f)
    writer.writerow(fieldnames)

    for key in data:
        f.write(key+",")
        for j in data[key]:
            f.write(j+",")
        f.write("\n")
