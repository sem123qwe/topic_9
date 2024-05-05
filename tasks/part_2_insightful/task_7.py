while True:
    users_password: str = input()

    if len(users_password) < 8:
        print("Пароль должен быть минимум 8 символов")
    elif len(users_password) > 255:
        print("Пароль не может быть больше 255 символов")
    elif users_password.isalpha():
        print("Пароль не должен состоять только из буквенных символов.")
    # elif users_password[-1].isalnum() == False:
    elif not users_password[-1].isalnum():
        print("Пароль должен заканчиваться буквой или цифрой.")
    elif users_password.isdigit():
        print("Пароль не должен состоять только из цифр.")
    elif users_password[0].isdigit():
        print("Пароль не может начинаться с цифры.")
    elif users_password.isalnum():
        print("ПРЕДУПРЕЖДЕНИЕ: Ваш пароль состоит только из букв и цифр")
        user_answer = input(
            "Хотите добавить специальные символы? (y/n):"
        ).lower
        if user_answer == "n":
            break

print("Пароль принят!")
