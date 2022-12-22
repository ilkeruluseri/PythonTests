# SOLVE EFFICIENCY ISSUE //SOLVED
"""
string = "BANANA"

vowels = ["A", "E", "O", "I", "U"]

str_list = [x for x in string]
all_sub = []
for i in range(len(str_list) + 1):
    for j in range(1, len(str_list) - i + 1):
        all_sub.append(str_list[i:j+i])
print(all_sub)


new_all_sub = []
for i in all_sub:
    temp = ""
    new_all_sub.append(temp.join(i))

print(new_all_sub)

stuart = 0
kevin = 0
for i in new_all_sub:
    if i[0] in vowels:
        kevin += 1
    else:
        stuart += 1

print("kevin:", kevin, "stuart:", stuart)
"""
# EFFICIENT WAY
string = "BANANA"
length = len(string)

vowels = ["A", "E", "O", "I", "U"]

stuart = 0
kevin = 0
count = 0
for i in string:
    if i in vowels:
        kevin += length - count
    else:
        stuart += length - count
    count += 1

print(f"Kevin: {kevin}, Stuart: {stuart}")