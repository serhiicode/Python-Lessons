num = int(input("Введіть номер місяця: \n"))

def season(month_number):
  if 1 <= month_number <= 2 or month_number == 12:
    return 'Цей місяць належить до Зими.'
  elif 3 <= month_number <= 5:
    return 'Цей місяць належить до Весни.'
  elif 6 <= month_number <= 8:
    return 'Цей місяць належить до Літа.'
  elif 9 <= month_number <= 11:
    return 'Цей місяць належить до Осени.'

if not 1 <= num <=12:
  print("Треба ввести від 1 до 12!")
else:
  print(season(num))