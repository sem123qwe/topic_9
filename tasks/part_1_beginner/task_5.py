user_line: str = input()
user_symbls: str = input()

# if user_symbls == "":
if not user_symbls:
    user_symbls = "-"

correct_line: str = ""
length: int = len(user_line)

num: int = 0
while num < length:
    if user_line[num] != user_symbls and num != (length - 1):
        correct_line += user_line[num] + user_symbls
    num += 1

print(correct_line)
