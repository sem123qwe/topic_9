text = 'some text!'

for i in text:
    # for i in 'some text!':
    print(i)

for i in range(len(text)):
    # for i in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
    print(text[i], i)

# list

fruits = ['яблоко', 'ананас', 'ЯблОкО', 'апельсин', 'киви', 'яблоко']
print(fruits)

# result = []
# for i in fruits:
# # for fruit in fruits:
#     if i.lower() == 'яблоко':
#         result.append('apple')
#     else:
#         result.append(i)

for i in range(len(fruits)):
    if fruits[i].lower() == 'яблоко':
        fruits[i] = 'apple'

print(fruits)

# operators

first = [1, 2, 3]
second = [1, 2, 3]

# print(first == second)
# print(first is second)


third = [6, 7, 8]
four = third

print(third == four)
print(third is four)

print(id(first))
print(id(second))
print(id(third))
print(id(four))
