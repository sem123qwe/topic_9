# TODO: Неверное решение, используйте методы str.maketrans() и str.translate()
#  В теории есть ссылка на эти методы, почитайте про них

user_input: str = input()

x = "АЕЁИОУЫЭЮЯAEIOUаеёиоуыэюяaeiou"
y = "??????????????????????????????"

tbl = user_input.maketrans(x, y)

print(user_input.translate(tbl))

