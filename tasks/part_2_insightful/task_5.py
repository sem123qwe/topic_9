# TODO: Неверное решение, используйте методы str.maketrans() и str.translate()
#  В теории есть ссылка на эти методы, почитайте про них
VOWELS: str = "АЕЁИОУЫЭЮЯAEIOUаеёиоуыэюяaeiou"

user_input = input()
correct_line = ""


lenght = len(user_input)
i = 0
while i < lenght:
    if user_input[i] not in VOWELS:
        correct_line += user_input[i]
    else:
        user_input[i] in VOWELS
        correct_line += "?"
    i += 1
print(correct_line)
