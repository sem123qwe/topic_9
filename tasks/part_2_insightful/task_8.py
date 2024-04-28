VOWELS: str = "аеёиоуыэюя"

names: list[str] = input().split()

max_vowels: int = 0
result: list[str] = []
for name in names:

    temp_vowels = 0
    for let in name.lower():
        if let in VOWELS:
            temp_vowels += 1

    if temp_vowels > max_vowels:
        result.clear()
        result.append(name)
        max_vowels = temp_vowels
    elif temp_vowels == max_vowels:
        result.append(name)

for item in result:
    print(item.capitalize())
