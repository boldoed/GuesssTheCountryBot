from hashlib import new
import pprint
import os
from random import choice


# check = 'йцукенгшщзхъфывапролджэячсмитьбюЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ-ё '
# with open('iso.txt', encoding='utf-8') as f:
#     file = f.readlines()
# country_dict = {}
# for i in file:
#     i = i[20:-35].split('</th><td>')
#     code = i[1].lower()
#     name = i[0]
#     new_name = ''
#     for i in name:
#         if i in check:
#             new_name += i
#     country_dict[new_name] = code

def qw():
    files = os.listdir('data')
    spisok = []
    for i in files:
        spisok.append(i[:-4])
    return spisok
print(qw())
# print(choice(qw))
# for i in spisok:
#     if i not in country_dict.values() and i != 'im' and i != 'ss' and i != 'xk':
#         print(i)


