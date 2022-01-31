n = int(input('Введіть число: \n'))

count = 0
sum = 0
min = n
max = 0
chetnoe = 0
nechetnoe = 0

while n != 0:
  count += 1
  sum += n 
  if max < n:
    max = n
  if n <= min:
    min = n
  if n % 2 == 0:
    chetnoe += 1
  else:
    nechetnoe += 1
  n = int(input('Введіть число: \n'))

print(f"Усього введено: {count} чисел", 
      f"Їх сумма дорвінює {sum}", 
      f"Середнє арифметичне: {sum / count}", 
      f"Максимальне значення - {max}, мінімальне - {min}", 
      f"Кількість парних - {chetnoe}, кількість непарних - {nechetnoe}", sep="\n")
