#Практическое задание ко второму уроку Python

#Задание 1:

types_list = [1, '1', 2.1, [1,2,'231'], tuple(2,3), {'Name':'Pavel'}, True, complex(11,21), set('3131',31), frozenset(2,1,2)]

for types in types_list:
    print(f'{types} представлен типом - {type(types)}')
    
    
#Задание 2:

replace_list = list(input('Введите значения:'))

if len(replace_list) % 2 == 0:
    for item in range(0, len(replace_list), 2):
        replace_list[item],  replace_list[item + 1] = replace_list[item + 1], replace_list[item]
else:
    for item in range(0, len(replace_list)-1, 2):
        replace_list[item],  replace_list[item + 1] = replace_list[item + 1], replace_list[item]

replace_list

#Задание 3:

years_list = ['Январь', 'Февраль', 'Март', 'Апрель', 
              'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь',
              'Октябрь', 'Ноябрь', 'Декабрь']
years_dict = dict(zip([1,2,3,4,5,6,7,8,9,10,11], years_list))

month = int(input("Input month number:"))

try:
    print(years_list[month-1], years_dict[month])
except:
    print("Number of thr month not in the list")

#Задание 4:

users_str = input('Input smt like "abra kada bra":')
str_to_lst = users_str.split(' ')

for word in str_to_lst:
    if len(word) > 10:
        print(f'Строка № {str_to_lst.index(word)}, {word[:10]}')
    else:    
        print(f'Строка № {str_to_lst.index(word)}, {word}')


#Задание 5:

ratio_list = [11,9,7,7,7,7,7,7,3,1,1,1,0]

while True:
    new_value = int(input('Add new value as "int":'))
    ratio_list.append(new_value)
    ratio_list.sort(reverse = True)
    print(ratio_list)

#Задание 6:

count_of_goods = int(input('Количестоведениц товара "int":'))
goods_list =[]

for goods in range(count_of_goods):
    print('-*'*30)
    temp = (goods + 1, {'Название':input('Название товара:'),
                         'Цена':float(input('Цена:')),
                         'Количество':int(input('Количество')),
                         'Еденица':input('Еденица измерения')})
    print(temp)
    goods_list.append(temp)

print(goods_list)

goods_dict = {}

for goods in goods_list:
    for key, value in goods[1].items():  # d.items() in Python 3+
        goods_dict.setdefault(key, []).append(value)

print(goods_dict)