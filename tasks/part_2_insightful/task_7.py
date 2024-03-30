ALPHABET: str = """АЕЁИОУЫЭЮЯAEIOU
                     аеёиоуыэюяaeiou
                     БВГДЖЗЙКЛМНПРСТФХЦЧШЩЪЬ
                     BCDFGHJKLMNPQRSTVWXYZ
                     бвгджзйклмнпрстфхцчшщъь
                     bcdfghjklmnpqrstvwxyz"""
NUMBERS = "0987654321"

while True:   
    message = input()
    laught = len(message)
    
    if message.isalnum() is True:
            print("Хотите добавить специальные символы?(y/N):")
            answer = input()
            match answer:
                case "y" | "Y":
                    continue
                case "n" | "N":
                    print("Пароль принят!")
                    break
    elif laught < 8:
        print("Пароль должен быть минимум 8 символов")
        continue
    elif laught > 255:
        print("Пароль не может быть больше 255 символов")
        continue
    elif message.isalpha():
        print("Пароль не должен состоять только из буквенных символов")
        continue
    elif message.isdecimal():
        print("Пароль не может начинаться с цифры")
        continue
    
    elif message[::1] is not ALPHABET or message[::1] is not NUMBERS:
        print("Пароль должен заканчиваться буквой или цифрой")
        continue

    
    


