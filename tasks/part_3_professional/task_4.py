age: list[int] = input('Введите возрасты посетителей' 
                       'через пробел: ').split()

youngs: int = 0
teenagers: int = 0
adults: int = 0
olds: int = 0

for i in range(len(age)):
    blap = int(age[i])
    if blap <= 2: 
        youngs += 1
    elif blap > 3 and blap <= 12: 
        teenagers += 1
    elif blap > 18: 
        adults += 1
    else:
        olds += 1

a = 'Дети до 2-х лет'
b = 'Дети от 3-х до 12 лет'
c = 'Взрослые'
d = 'Пенсионеры '
print(f'{a:<20} ' + f'{b:<25}' + f'{c:<20}' + f'{d:<20}')

print(f'{youngs:<21}' + f'{teenagers:<25}' 
      + f'{adults:<20}' + f'{olds:<20}') 


print('Общая стоимость билетов: ' + f'{teenagers * 1055 + adults * 1499 + 2099 * olds:>3f}')