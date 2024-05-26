ages: list[str] = input(
    'Введите возрасты посетителей через пробел: '
).split()

PRICE_TEENAGERS: int = 1055
PRICE_ADULTS: int = 2099
PRICE_OLDS: int = 1449

youngs: int = 0
teenagers: int = 0
adults: int = 0
olds: int = 0

for age in ages:
    age = int(age)
    if 0 < age <= 2:
        youngs += 1
    elif 3 <= age <= 12:
        teenagers += 1
    elif 12 < age < 65:
        adults += 1
    elif age >= 65:
        olds += 1

out_table: str = '{:<20} {:<25} {:<20} {:<20}'
columns: tuple[str, ...] = ('Дети до 2-х лет',
                            'Дети от 3-х до 12 лет',
                            'Взрослые',
                            'Пенсионеры')
result: float = (teenagers * PRICE_TEENAGERS
                 + adults * PRICE_ADULTS
                 + PRICE_OLDS * olds)

print(out_table.format(*columns))
print(out_table.format(youngs, teenagers, adults, olds))
print(f'\nОбщая стоимость билетов: {result:>,d}₽')
