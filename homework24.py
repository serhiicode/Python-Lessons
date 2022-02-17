a, b, c = int(input('Введіть число 1:\n')), int(input('Введіть число 2:\n')), input('Математична операція(+ - * /):\n')

def arithmetic(n1, n2, m):
  if m == '+':
    return(n1+n2)
  elif m == '-':
    return(n1-n2)
  elif m == '*':
    return(n1*n2)
  elif m == '/':
    return(n1/n2)
  else:
    print('Невідома операція')

print(f'{a} {c} {b} = {arithmetic(a, b, c)}')