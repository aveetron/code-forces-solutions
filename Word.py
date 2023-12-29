name: str = input()

total_upper = 0
total_lower = 0

for w in name:
    if w.isupper():
        total_upper = total_upper + 1
    else:
        total_lower = total_lower + 1

if total_upper > total_lower:
    print(name.upper())
elif total_upper < total_lower:
    print(name.lower())
elif total_upper == total_lower:
    print(name.lower())
