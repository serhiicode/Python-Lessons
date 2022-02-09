lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f'Список був: \n{lst}\n')
for i in range(len(lst)):
  x = lst.pop()
  lst.insert(i, x)
print(f'Список став: \n{lst}\n')