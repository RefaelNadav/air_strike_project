import json

with open('targets_data.json', 'r') as file:
    targets = json.load(file)

dict_targets = {}
for taget in targets:
    dict_targets[taget["City"]] = {
        'Priority': taget['Priority']}

with open('targets_location.json', 'r') as file:
    targets_location = json.load(file)

print(targets_location)




print(dict_targets)
#
# people.update({"person3": {
#     "name": "shubulu",
#     "money": -100
# }})
# people.update({"person4": [1, 2, 3]})
#
# with open('people.json', 'w') as file:
#     json.dump(people, file)