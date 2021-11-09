#python lesson4 task 6(b)

from itertools import cycle

some_row = 'SOME row 1234567'

def my_iter():
    iter_list = []
    itter = 0
    for i in cycle(some_row):
        if itter > 20:
            break
        
        iter_list.append(i)
        itter += 1
    return iter_list