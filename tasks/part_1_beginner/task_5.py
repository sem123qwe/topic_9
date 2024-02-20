user_line = input()
user_symbls = input()
correct_line = ""

count = len(user_line)
num = 0


while num < count:
    if user_symbls == "":
        correct_line += user_line[num] + "-"

    elif user_line[num] != user_symbls:
        correct_line += user_line[num] + user_symbls
    else:
        user_line[num] == user_symbls
        pass
    num += 1
print(correct_line[:-1:])
