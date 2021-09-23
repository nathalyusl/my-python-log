import
print("hello world")

name_list = ["diana", "moe", "tarzan"]

last_name_list = ["gog", "win", "gat"]

full_name_list = []

for i in range(3):
    name = name_list[i]
    last_name = last_name_list[i]
    full_name = name + " " + last_name
    full_name_list.append(full_name)

for name in full_name_list:
    print(name)

casa = ((7 * 3 // 2 * 4))

print(casa)
