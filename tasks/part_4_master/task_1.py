waitresses_order: str = input()

MENY: list[str] = (
    'Burger Fries Chicken Pizza Sandwich Onionrings Milkshake Coke'
    ).lower().split()

resalt = ''

for i in MENY:
    counter: int = waitresses_order.count(i)
    resalt += (i.capitalize() + ' ') * counter

print(resalt)
