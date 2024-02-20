user_line: str = input()
user_symbls: str = input()
correct_line: str = ""

count: int = len(user_line)
num: int = 0


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
