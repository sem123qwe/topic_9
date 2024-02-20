user_line: str = input()
# while num < len(user_line):
#     while user_line[::num]
if user_line[::1] == user_line[::-1]:
    print(True)
else:
    print(False)
