#14.2json2csv.py
import json
fr = open("price2016.json", "r")
ls = json.load(fr)
data = [ list(ls[0].keys()) ]
for item in ls:
    data.append(list(item.values()))
fr.close()
fw = open("price2016_from_json.csv", "w")
for item in data:
    fw.write(",".join(item) + "\n")
fw.close()
# import json
#
# data = {
#     'name' : 'ACME',
#     'shares' : 100,
#     'price' : 542.23
# }
#
# json_str = json.dumps(data)
# data1 = json.loads(json_str)
# print(json_str)
# print(data1)

