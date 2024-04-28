# TODO: 1. Неверное решение, используйте встроенные методы строк.
#  Рекомендую использовать цикл for вместо while,
#  тогда получится компактный код

user_line: str = input().split("*")

for i in user_line:
    print(i.capitalize())
