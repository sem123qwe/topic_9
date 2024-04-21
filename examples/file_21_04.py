# Пример кода для 0-й задачи
# text = 'Hello WOrld'.lower()
# target = 'H'.lower()
#
# print(text.count(target))

# ------------------------------------
# Пример кода для 1-й задачи
# text = 'The quick  d  brown fox jumps over the lazy        dog'.split()
# print(text)
#
# text_2 = 'adfsdf-b-dsfsdfc-d-e'.split('-')
# print(text_2)
#
# text_3 = 'The quick  d  brown fox jumps over the lazy        dog'.split(' ')
# print(text_3)
#
# print(len(text))
# print(len(text_3))

# ------------------------------------
# Пример кода для 2-й задачи
# text = 'The*quick*brown*fox*jumps*over*the*lazy*dog'.split('*')
# print(text)
#
# for word in text:
#     print(word.capitalize())

# ------------------------------------
# Пример кода для 3-й задачи
# text = 'Муза, ранясь шилом опыта, ты помолишься на разум'.lower()
#
# # text = text.replace(' ', ''
# #                     ).replace('-', ''
# #                               ).replace(',', '')
#
# chars = ' -,'
# for char in chars:
#     text = text.replace(char, '')
#
# print(text)
# print(text == text[::-1])


# ------------------------------------
# Пример кода для 4-й задачи

# text = 'Point A and B'.lower().split()
text = '     some       case      word       '.lower().split()
print(text)

pascal_case = 'Pascal'
camel_case = 'camel'
snake_case = 'snake_'

res = '_'.join(text)
print(snake_case + res)

# ------------------------------------
# Пример кода для 8-й задачи

# ------------------------------------
# ------------------------------------
# ------------------------------------
