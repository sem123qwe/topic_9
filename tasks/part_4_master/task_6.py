line: str = input()

flag: bool = False
length: int = len(line)

for i in range(length):
    for j in range(length):
        if line[i] == line[j] and i != j:
            flag = True
            break
    if flag:
        print(False)
        break
else:
    print(True)
