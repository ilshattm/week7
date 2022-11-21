def get_sum(list):
    if list == []:
        return 0
    else:
        get_result = get_sum(list[1:])
        summ = get_result + list[0]
        print(summ)
        return summ

print(get_sum([1, 2, 3, 5]))

# f = [1, 2, 3, 5]
# print(f[::-len(f)])
# phibonachi

#json

import json
with open("test.json", "r") as file:
   new_dict = json.load(file)
print(new_dict)

new_dict["name"] = "meta"
new_dict["yaer"] = 2
new_dict["is_own"] = False

with open("test.json", "w") as file:
    text_json = json.dumps(new_dict)
    print(new_dict)
    file.write(text_json)