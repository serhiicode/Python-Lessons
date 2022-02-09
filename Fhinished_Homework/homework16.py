lst = [input(f"Додайте елемент в список (ще {10-n}): \n") for n in range(0, 10)]
k = int(input('Введіть індекс для видалення елементу (0-9): \n'))

for i in range(k+1, len(lst)):
  lst[i-1] = lst[i]
lst.pop()

print(f'Ваш новий список: \n {lst}')