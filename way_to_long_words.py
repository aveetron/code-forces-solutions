repeat_numbers = int(input())

for i in range(0, repeat_numbers):
    line = input()
    if len(line) > 10:
        print(str(line[0])+str(len(line[1:len(line)-1]))+str(line[len(line)-1]))
    else:
        print(line)