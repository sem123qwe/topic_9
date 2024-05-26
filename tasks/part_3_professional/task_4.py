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

a: tuple[str] = (
    'Дети до 2-х лет', 'Дети от 3-х до 12 лет', 'Взрослые', 'Пенсионеры'
    )

b: str = '{:<20} {:<25} {:<20} {:<20}' 

c = f'{youngs}{teenagers}{adults}{olds}'


print(b.format(*a))
print(b.format(*c))
