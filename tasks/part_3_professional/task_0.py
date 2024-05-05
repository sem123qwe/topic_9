VOWELS: str = 'АЕЁИОУЫЭЮЯAEIOUаеёиоуыэюяaeiou'

masseg: str = input()

counter_vowels: int = 0
for letter in masseg:
    if letter.lower() in VOWELS:
        counter_vowels += 1

resalt: float = (counter_vowels / len(masseg)) * 100
print(f'Отношение гласных: {resalt:0>5.2f}%')
