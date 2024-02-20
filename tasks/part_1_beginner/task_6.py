user_line: str = input("")
num: int = 0
chot: str = ""
nechot: str = ""
while num < len(user_line):
    if num % 2 == 0:
        chot += user_line[num]
    else:
        nechot += user_line[num]
    num += 1
print(chot)
print(nechot)
