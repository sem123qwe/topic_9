VOWELS: str = "АЕЁИОУЫЭЮЯAEIOU"
CONSONANTS: str = ("БВГДЖЗЙКЛМНПРСТФХЦЧШЩЪЬBCDFGHJKLMNPQRSTVWXYZ"
                   "бвгджзйклмнпрстфхцчшщъьbcdfghjklmnpqrstvwxyz")

chat: str = input()

num: int = 0
counter_vowels: int = 0
counter_consonants: int = 0
while num < len(chat):
    if chat[num] in CONSONANTS:
        counter_vowels += 1
    elif chat[num] in VOWELS:
        counter_consonants += 1
    num += 1

print(counter_consonants)
print(counter_vowels)
