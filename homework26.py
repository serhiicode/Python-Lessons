'''
Написать функцию is_year_leap, принимающую 1 аргумент — номер года, и возвращающую True, если год високосный, и False иначе.
'''

year = int(input('Введіть рік, котрий ви бажаєте перевірити.\n'))
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print("Це високосний рік.")
else:
    print("Цей рік не високосний.")