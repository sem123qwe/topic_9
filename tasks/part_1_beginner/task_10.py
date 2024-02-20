en_vowels: str = "АЕЁИОУЫЭЮЯAEIOU"
en_consonants: str = "БВГДЖЗЙКЛМНПРСТФХЦЧШЩЪЬBCDFGHJKLMNPQRSTVWXYZ"

chat: str = input("").upper()
num: int = 0
counter_vowels: str = ""
counter_consonants: str = ""
while num < len(chat):
    if chat[num] in en_consonants:
        counter_vowels += chat[num]
    elif chat[num] in en_vowels:
        counter_consonants += chat[num]
    num += 1

print(len(counter_consonants))
print(len(counter_vowels))
