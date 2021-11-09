#python lesson 4 task 1
"""функция принимает значения:
имя сотрудника  - name
часовая ставка - hourly_payment
отработаные часы - works_time
премия - bonus
возвращает З/П сотрудника"""
from sys import argv

sn, name, hourly_payment, works_time, bonus = argv

def empl_sallary():

    return f'INFO: Сотрудник {name} за отчетный период получил {(float(hourly_payment) * float(works_time)) + float(bonus)}'
