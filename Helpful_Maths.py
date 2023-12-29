helpful_math = input()

if len(helpful_math) > 1:
    splited_helpful_math = helpful_math.split('+')
    int_splited_helpful_math = [int(i) for i in splited_helpful_math]
    final_output = ""
    for i, math in enumerate(sorted(int_splited_helpful_math)):
        if i == len(int_splited_helpful_math)-1:
            final_output += str(math)
        else:
            final_output += str(math)+"+"
    
    print(final_output)
else:
    print(helpful_math)

