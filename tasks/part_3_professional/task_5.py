results: list[str] = []
max_width: int = 0

while True:
    fio: str = input().strip()

    if fio.lower() == 'end':
        break

    surname, name, patronymic = fio.title().split()
    # surname, name, patronymic = ['Ф', 'И', 'О']
    surname_length: int = len(surname)

    if surname_length > max_width:
        max_width = surname_length

    results.append(f'{surname} {name[0]}.{patronymic[0]}.')

print(f'{"№":^3} {"ФИО":^{max_width}}')
# for i in range(len(results)):
# print(f'{i + 1:0>2} | {results[i]}')
for index, elem in enumerate(results, start=1):
    print(f'{index:0>2} | {elem}')

# https://pythonchik.ru/osnovy/cikl-for-v-python
