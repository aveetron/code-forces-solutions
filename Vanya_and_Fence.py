import math

n, h = map(int, input().split())
numbers = list(map(int, input().strip().split(' ')))
result = 0

for number in numbers:
    if h > number:
        result = result + 1
    else:
        result = result + int(math.ceil(number / h))

print(result)