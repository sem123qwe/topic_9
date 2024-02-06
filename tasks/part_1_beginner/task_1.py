user_input = input()
right_line = []
num = 0
while num < len(user_input):
    if user_input[num] == user_input[num - 1]:
        right_line.append(user_input[num])
    else:
        continue
    num += 1
print(right_line)
