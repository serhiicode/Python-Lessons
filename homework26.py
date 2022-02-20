year_input = int(input('Введіть рік, котрий ви бажаєте перевірити.\n'))

def is_year_leap(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    else:
        return False

if is_year_leap(year_input) == True:
    print("Це високосний рік.")
else:
    print("Цей рік не високосний.")