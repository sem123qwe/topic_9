user_line: str = input()

if user_line == user_line[::-1]:
    print(True)
else:
    print(False)


# ----------- Option 2

print(user_line == user_line[::-1])
