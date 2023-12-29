a, b = map(int, input().split())
total_round = None

def get_calcu(a: int, b: int, call_count=1):
    if (a*3) > (b*2):
        return call_count
    else:
        return get_calcu(a*3, b*2, call_count+1)

print(get_calcu(a, b))