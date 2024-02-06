user_input = input("")
colecton = "0987654321"
num = 0
while num < len(user_input):
    if user_input[num] in colecton:

        print(user_input[num], end="$ ")

    num += 1
