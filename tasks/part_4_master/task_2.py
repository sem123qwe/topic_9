ip_address: list[str] = input().split('.')
resalt: str = ''
for octet in ip_address:
    bits: str = bin(int(octet))[2:].zfill(8)
    resalt += bits

print(int(resalt, 2))
