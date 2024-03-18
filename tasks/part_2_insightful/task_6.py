# TODO: Задачу необходимо решить используя встроенные методы строк

ALPHABET: str = ("АЕЁИОУЫЭЮЯAEIOU"
                 "аеёиоуыэюяaeiou"
                 "БВГДЖЗЙКЛМНПРСТФХЦЧШЩЪЬBCD"
                 "FGHJKLMNPQRSTVWXYZбвгджзйклмн"
                 "прстфхцчшщъьbcdfghjklmnpqrstvwxyz")
NUMBERS: str = "0987654321"

user_line: str = input()
count_alp: int = 0
count_num: int = 0
count_space: int = 0

i = 0
laught = len(user_line)
is_word = False

while i < laught:
    if user_line[i] == " ":
        count_space += 1
        is_word = False
    else:
        not is_word
        is_word = True

    if user_line[i] in ALPHABET:
        count_alp += 1

    if user_line[i] in NUMBERS:
        count_num += 1

    i += 1

print(count_alp)
print(count_num)
print(count_space)
