ages: list[str] = input(
    'Введите возрасты посетителей через пробел: '
).split()

youngs: int = 0
teenagers: int = 0
adults: int = 0
olds: int = 0

for age in ages:
    age = int(age)
    if age <= 2:
        youngs += 1
    elif age > 3 and age <= 12:
        teenagers += 1
    elif age > 18:
        adults += 1
    else:
        olds += 1

a = 'Дети до 2-х лет'
b = 'Дети от 3-х до 12 лет'
c = 'Взрослые'
d = 'Пенсионеры '

print(f'{a:<20} {b:<25}{c:<20}{d:<20}')
print(f'{youngs:<21}{teenagers:<25}{adults:<20}{olds:<20}')

print('Общая стоимость билетов: '
      f'{teenagers * 1055 + adults * 1499 + 2099 * olds:>,d}₽')
