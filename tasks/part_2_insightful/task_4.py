user_input = input().title()

# TODO: Используйте встроенные методы для решения этой задачи
line_1 = "case" 
line_2 = "Pascal" 
line_3 = "snake_"

for i in range(len(user_input)):
    if user_input[i] == " ":
        line_1 += ""
    else:
        line_1 += user_input[i]


for i in  range(len(user_input)):
    if user_input[i] == " ":
        line_2 += ""
    else:
        line_2 += user_input[i]

correct_line = ""
for i in range(len(user_input)):
    if user_input[i] != user_input[i - 1]:
        correct_line += user_input[i]
for i in range(len(correct_line) - 1):
    if correct_line[i] == " ":
        line_3 += "_"
    else:
        line_3 += correct_line[i]   


print(line_1)
print(line_2)
print(line_3.lower())