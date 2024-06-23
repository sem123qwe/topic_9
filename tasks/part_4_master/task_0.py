message: list[str] = input().split()
for i in range(len(message)):
    if len(message[i]) >= 5:
        message[i] = message[i][::-1]

print(*message)

# Второй вариант вывода
# result: str = ' '.join(message)
# print(result)
