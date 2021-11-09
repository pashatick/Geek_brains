#Python lessons 4


#Task 1:
from empl_sallary import empl_sallary as es

empl_info = es()
print(empl_info)


#Task 2:
print('--'*40)
samp_arr = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_arr = [i for i in samp_arr if i > samp_arr[samp_arr.index(i)-1]]
print(f'Ответ ко второму заданию - {new_arr}')


#Task 3:
print('--'*40)
list_ = [i for i in range(20, 240) if i % 20 == 0 or i % 21 == 0]
print(f'Ответ к третьему заданию {list_}')


#Task 4:
print('--'*40)
smth_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

uniq_list = [i for i in smth_list]
print('  ')


#Task 5:
print('--'*40)
from functools import reduce
comp = reduce(lambda x,y: x * y , [i for i in range(100, 1001) if i % 2 == 0])
print(f'Произведение четных чисел массива =  {comp}')


#Task 6:
print('--'*40)
import my_gen
import my_iter

solv_g = my_gen.my_gen()
print(f'Ответ к заданию 6а - {solv_g}')

solv_i = my_iter.my_iter()
print(f'Ответ к заданию 6b - {solv_i}')


#Task 7:
print('--'*40)
print(f'Ответ к заданию 7')

from math import factorial as fct

numbers = int(input('add some number to factorial:')) 

def gen():
    
    for el in range(1, numbers + 1):
        yield el

ex_g = gen()

for el in ex_g:
    print(f'Факториал числа {el} = {fct(el)}')

