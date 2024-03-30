# TODO: 1. Неверное решение, используйте встроенные методы строк.
#  Рекомендую использовать цикл for вместо while,
#  тогда получится компактный код

user_line = input().title()
correct_line = ""
for i in range(len(user_line)):
    if user_line[i] == "*":
        correct_line += "\n"
    else:
        correct_line += user_line[i]

print(correct_line)