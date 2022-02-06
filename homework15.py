from random import randint

count = 0
lst = [randint(0, 100) for _ in range(0, 10)]

print(f'Згенерований список: \n{lst}\n')

for i in lst[1:9]:
  x = lst.index(i)
  if lst[x-1] < i > lst[x+1]:
    count += 1
    print(i, end=' ')
    
print(f'\nКількість чисел які більше сусідів:\n{count}\n')