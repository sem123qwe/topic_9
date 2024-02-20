user_line: str = input()
char: str = input()

length: int = len(user_line)
if char not in user_line:
    print(-1)
else:
    i: int = 0
    while i < length: 
        if user_line[i] == char:
            print(i)
            break

# --------------------- Option 2

user_line: str = input()
char: str = input()

if char not in user_line:
    print(-1)
else:
    for i in range(len(user_line)):
        if user_line[i] == char:
            print(i)
            break
            
