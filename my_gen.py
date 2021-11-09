#python lesson4 task 6(a)
from itertools import count


def my_gen():
    start_nubber = int(input('add start nuber:'))
    new_list = []

    for element in count(start_nubber):
        if element > start_nubber + 15:
            break
        new_list.append(element)
    
    return new_list