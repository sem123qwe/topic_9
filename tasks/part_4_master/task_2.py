IP_adress: list[str] = input().split('.')
resalt: str = ''
for i in IP_adress:
    a = bin(int(i))
    b = f'{str(a)[2::]:0>8}'
    resalt += b

print(int(resalt, 2))
