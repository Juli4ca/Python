# 1. Напишите программу, удаляющую из текста все слова, содержащие "абв". В тексте используется разделитель пробел.
# # in
# # Number of words: 10
# #
# # out
# # авб абв бав абв вба бав вба абв абв абв
# # авб бав вба бав вба

from random import choices, sample


def new_str(count: int):
    if count < 1:
        return 'Error'
    list_abv = []
    for i in range(count):
        value = choices(['абв', 'авб', 'бва', 'ваб', 'бав', 'бва'], k=1)
        list_abv.append(''.join(value))
    str_abv = ' '.join(list_abv)

    return str_abv


def deletes_words(str_original: str):
    words = str_original.split(' ')
    new_words = []
    for word in words:
        if word != 'абв':
            new_words.append(word)
    del_str = ' '.join(new_words)

    return del_str


str1 = new_str(int(input('Enter a count: ')))
print(str1)
print(deletes_words(str1))
