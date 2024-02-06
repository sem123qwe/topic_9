user_line = input("")
num = 0
chot = ""
nechot = ""
while num < len(user_line):
    if num % 2 == 0:
        chot + user_line[num]
    else:
        nechot + user_line[num]
    num += 1
print(chot)
print(nechot)
