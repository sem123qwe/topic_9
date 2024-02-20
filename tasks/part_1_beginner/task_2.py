user_line = input()
char = input()

if char not in user_line:
    print('-1')
else:
    num: int = 0
    count: int = 0
    while char in user_line:
        if char == user_line[num]:
            continue
        else:
            count += 1  # Используйте цикл
print(count)
