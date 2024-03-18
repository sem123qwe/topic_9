VOWELS: str = "АЕЁИОУЫЭЮЯAEIOUаеёиоуыэюяaeiou"
CONSONANTS: str = ("БВГДЖЗЙКЛМНПРСТФХЦЧШЩЪЬBCDFGHJKLMNPQRSTVWXYZ"
                   "бвгджзйклмнпрстфхцчшщъьbcdfghjklmnpqrstvwxyz")

chat: str = input()

num: int = 0
counter_vowels: int = 0
counter_consonants: int = 0
length: int = len(chat)
while num < length:
    if chat[num] in CONSONANTS:
        counter_vowels += 1
    elif chat[num] in VOWELS:
        counter_consonants += 1
    num += 1

print(counter_consonants)
print(counter_vowels)
