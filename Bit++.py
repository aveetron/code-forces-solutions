numbers: int = int(input())
command_list: list = []

for number in range(numbers):
    command_list.append(input())

postive_list = ["x++", "++x", "X++", "++X"]
negative_list = ["x--", "--x", "X--", "--X"]

result = 0

for command in command_list:
    if command in postive_list:
        result = result + 1
    elif command in negative_list:
        result = result - 1


print(result)