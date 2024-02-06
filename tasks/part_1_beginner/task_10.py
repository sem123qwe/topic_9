
en_vowels = "АЕЁИОУЫЭЮЯAEIOU"
en_consonants = "БВГДЖЗЙКЛМНПРСТФХЦЧШЩЪЬBCDFGHJKLMNPQRSTVWXYZ"

chat: str = input("").upper()
num = 0
counter_vowels = []
counter_consonants = []
while num < len(chat):
    if chat[num] in en_consonants:
        counter_vowels.append(chat[num])
    elif chat[num] in en_vowels:
        counter_consonants.append(chat[num])
    num += 1
print(len(counter_vowels))
print(len(counter_consonants))
# TODO мне не нравитсся, можно проще!(Ну, это я так думаю)
