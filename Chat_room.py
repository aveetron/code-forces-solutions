PREDEFINED_VALUE = "hello"

greetings = input()
result = False

greetings_list = [g for g in greetings]

for i, g in enumerate(greetings_list):
    if g == greetings_list[i]:
        greetings_list.pop(i)
    else:
        pass

for i, g in enumerate(greetings_list):
    if g not in ['h','e','l','l','o']:
        greetings_list.pop(i)

c = ''
for g in greetings_list:
    c = c + g

if c == PREDEFINED_VALUE:
    print("YES")
else:
    print("NO")