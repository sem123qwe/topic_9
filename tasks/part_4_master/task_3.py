bits: int = int(input())
convert: str = bin(bits)[2:].zfill(32)

result: list[str] = []
left: int = 0
for i in range(8, 33, 8):
    num = str(int(convert[left:i], 2))
    result.append(num)
    left = i

    # convert[left: i]
    # convert[0:8]
    # left = i
    # convert[8:16]
    #
    # left = i
    # convert[16:24]
    #
    # left = i
    # convert[24:32]

print('.'.join(result))
