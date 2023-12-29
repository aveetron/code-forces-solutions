n, k = map(int, input().split())
final_result = 0

for i in range(k):
    if n % 10 == 0:
        n = n / 10
    else:
        n = n - 1

print(int(n))