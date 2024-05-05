VOWELS: str = 'АЕЁИОУЫЭЮЯAEIOUаеёиоуыэюяaeiou'

masseg: str = input()
counter_vowels: int = 0
len(masseg)

for letter in masseg:
    for i in letter.lower():
        if i in VOWELS:
            counter_vowels += 1

resalt: float = (counter_vowels / len(masseg)) * 100
print(f'Отношение гласных: {resalt:.2f}%')
