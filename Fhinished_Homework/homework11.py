s = input('Введіть строку\n')
sym = input('Введіть символ\n')

index = 0
count = 0

if s.find(sym) != -1:
  while s.rfind(sym)+1 > index:  
    x = s.find(sym, index, len(s))
    index = x + 1
    count += 1  
  print(f'В вашому запиті {count} символів {sym}')

else: 
  print('Тут таких символів немає')