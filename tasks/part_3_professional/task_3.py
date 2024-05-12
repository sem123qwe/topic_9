
user_discount: int = int(input())
cost: list[str] = input().split()

# if user_discount >= 100 and user_discount <= 0: 
#     print('Размер скидки должен быть больше 0' 
#           'и не должен превышать 100')
    
a = 'Название'
b = 'Цена'
c = 'Сумма скидки'
d = 'Новаяцена'
print(f'{a:<15} ' + f'{b:<10}' + f'{c:<15}' + f'{d:<10}')
# TODO 'это наверное можно упростить, как только придумаю, сразу сделаю'
for i in range(len(cost)):
    amounth_discaunt: float = int(cost[i]) * (user_discount / 100)
    resalt: float = int(cost[i]) - amounth_discaunt
    print('Товар ' + f'{i + 1:<10}' + f'{int(cost[i]):<10.2f}' 
          + f'{amounth_discaunt:<15.2f}' 
          + f'{resalt:<10.2f}')
    
