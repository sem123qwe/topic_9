user_input = input()
count = 0

num = 0
size_line = len(user_input)
while num < size_line:
    if user_input[num] == " ":
        count += 1
    else:
        pass
    num += 1
print(count + 1)
