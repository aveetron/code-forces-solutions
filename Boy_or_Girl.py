name = input()

# if number if distict char in name is odd then male
if len(list(set(name))) % 2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")