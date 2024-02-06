user_input = input("")
number = len(user_input)
num = 1
while num < number + 1:
    peramid = user_input[:num:]
    print(peramid)
    num += 1
