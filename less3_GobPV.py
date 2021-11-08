#Python lessons 3

# 1 task:

def to_division(first_num, second_num):
    
    """The function takes two positional 
    arguments and produces a division"""
    
    if second_num != 0:
        return first_num/second_num 

    return f'Деление на ноль запрещено!' 

que = int(input('add 1st num'))
divs = int(input('add 2nd num'))


to_division(que, divs)

# 2 task:

def users_info(name = str(), 
               second_name = str(), 
               b_date = str(), 
               city = str(), 
               email = str(),
              phone_number = str()):
    
    """The function takes six named 
    arguments - info about user and return 
    information on kne row"""
    
    users_data = {'First name':name,
                 'Second name': second_name,
                 'Birthday':b_date,
                 'City':city,
                 'Email':email,
                 'Phone number':phone_number}
    
    return f'Users data is {users_data}'

# 3 task:

def my_func(*args):
    
    """The function takes positional 
    arguments and returns summ two of max"""

    temp = [*args]
    temp.sort(reverse=True)
    
    return temp[0] + temp[1] 

# 4 task:

def my_func_(x, y):
    
    """
    Функция принимает 2 позиционных аргумента, 
    один из которых - действительное положительное число x, 
    второй -  целое отрицательное число y. 
    и вовращает степень двумя способами.
    """
    answ1 = x**y
    answ2 = 1
    
    for i in range(abs(y)):
        answ2 *= x
    
    return f'Результат при выполнении x**y - {answ1}, результат при реализации цикла - {1/answ2}'

# 5 task:

def summarizd():
    """
    Прогррамма принимает строку из чисел
    Возвращает сумму чисел в строке
    """
    answ = 0
    
    while True:
        numbers = input('Введи строку чисел разделенных пробелом (1 2 3 4 5 ...), для выхода "!":')
        
        Flag = '!'
        
        if numbers != Flag:
            numb = numbers.split(' ')
            
            if numb[-1] == Flag:
                
                for i in range(len(numb)-1):
                    answ += int(numb[i])
                return f'Программа завершена, ответ - {answ}'
                break
            
            for i in range(len(numb)-1):
                answ += int(numb[i])
            
            print(f'Результат суммирования строки - {answ}')
        
        else:
            return f'Программа завершена, ответ - {answ}'
            break
    
# 6 task:

def int_func(text):
    
    return text.title()