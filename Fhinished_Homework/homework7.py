year = int(input('Введіть рік, котрий ви бажаєте перевірити.\n'))
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print("Це високосний рік.")
else:
    print("Цей рік не високосний.")