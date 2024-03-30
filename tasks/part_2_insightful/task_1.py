user_line = input()

# TODO: 1. Программа для третьего теста выдает некорректный вывод
# TODO: 2. Вам не нужно писать так много кода,
#  просто используйте строковый метод

# print(user_line.count(' ') + 1)
if user_line == "":
    print(False)
else:
    print(user_line.count(' ') + 1)