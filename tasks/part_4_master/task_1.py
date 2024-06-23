waitresses_order: str = input()

MENY: list[str] = (
    'Burger Fries Chicken Pizza Sandwich Onionrings Milkshake Coke'
).lower().split()

resalt = ''
for i in MENY:
    counter: int = waitresses_order.count(i)
    resalt += (i.capitalize() + ' ') * counter

print(resalt)

# №2

order: str = input()
MENU: list[str] = [
    'Burger',
    'Fries',
    'Chicken',
    'Pizza',
    'Sandwich',
    'Onionrings',
    'Milkshake',
    'Coke'
]

result: list[str] = []
for item in MENU:
    while item.lower() in order:
        result.append(item)
        order = order.replace(item.lower(), '', 1)

print(' '.join(result))
