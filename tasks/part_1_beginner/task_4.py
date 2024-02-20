user_input = input("")
colecton = "0987654321"
num = 0
count = len(user_input)
while num < count:
    if user_input[num] in colecton:
        print(user_input[num], end="$ ")
    num += 1
