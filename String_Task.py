task = input()

vowel_list = ["a","e","i","o","u","y"]
non_vowel_list = [item for item in task.lower() if item not in vowel_list]

string_task = ""

for item in non_vowel_list:
    string_task+="."+item

print(string_task)