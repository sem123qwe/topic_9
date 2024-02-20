user_input = input()
right_line = ""
num = 0
calculate = len(user_input)
while num < calculate:
    if user_input[num] == user_input[num - 1]:
        right_line + user_input[num]
    else:
        continue
    num += 1
print(right_line)
