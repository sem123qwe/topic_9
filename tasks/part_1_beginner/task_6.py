user_line: str = input()
num: int = 0

even: str = ""
odd: str = ""
while num < len(user_line):
    if num % 2 == 0:
        even += user_line[num]
    else:
        odd += user_line[num]
    num += 1
print(even)
print(odd)


# --------------- Option 2

print(user_line[::2], user_line[1::2], sep="\n")
