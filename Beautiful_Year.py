enter_number = int(input())

for i in range(enter_number+1, 90000):
    if len(list(set(str(i)))) == 4:
        print(i)
        break