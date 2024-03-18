# TODO: Логика задачи верна, только её необходимо решить
#  используя встроенные методы строк

while True:
    ALPHABET: str = ("АЕЁИОУЫЭЮЯAEIOU"
                     "аеёиоуыэюяaeiou"
                     "БВГДЖЗЙКЛМНПРСТФХЦЧШЩЪЬBCD"
                     "FGHJKLMNPQRSTVWXYZбвгджзйклмн"
                     "прстфхцчшщъьbcdfghjklmnpqrstvwxyz")
    NUMBERS: str = "0987654321"

    user_line = input()
    laught = len(user_line)

    if laught < 8:
        print("Пароль должен быть минимум 8 символов")

    elif laught > 255:
        print("Пароль не может быть больше 255 символов")

    elif user_line[1] == NUMBERS:
        print("Пароль не может начинаться с цифры")
        break

    elif user_line[laught - 1] == NUMBERS or user_line[laught - 1] == ALPHABET:
        print("Пароль должен заканчиваться буквой или цифрой")
        break

    # TODO: Ниже цикл нужно убрать, задача решается с помощью одного цикла
    count_num = 0
    count_alp = 0
    i = 0
    while i < laught:
        if ALPHABET in user_line[i]:
            count_alp += 1
        else:
            NUMBERS in user_line[i]
            count_num += 1
        i += 1

        if count_alp == laught:
            print("Пароль не должен состоять только из буквенных символов")
            break
        elif count_num == laught:
            print("Пароль не должен состоять только из цифр")
            break
        if count_alp + count_num == laught:
            print("Хотите добавить специальные символы?")
            answer = input()
            match answer:
                case "N":
                    print("Пароль принят!")
                case "y":
                    continue
