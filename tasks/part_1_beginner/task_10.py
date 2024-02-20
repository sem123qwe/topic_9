
en_vowels = "АЕЁИОУЫЭЮЯAEIOU"
en_consonants = "БВГДЖЗЙКЛМНПРСТФХЦЧШЩЪЬBCDFGHJKLMNPQRSTVWXYZ"

chat: str = input("").upper()
num = 0
counter_vowels = ""
counter_consonants = ""
while num < len(chat):
    if chat[num] in en_consonants:
        counter_vowels += chat[num]
    elif chat[num] in en_vowels:
        counter_consonants += chat[num]
    num += 1

print(len(counter_consonants))
print(len(counter_vowels))
