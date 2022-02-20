height = int(input('Яка висота ромба?\n'))
if height % 2 == 0:
  height += 1

for row in range(height):
  for cols in range(height):
    if 0 <= row <= height//2:
      if row == 0 and cols == height//2 or height//2-row <= cols <= height//2+row or row == height//2:
        print('* ', end=' ')
      else:
        print('  ', end=' ')
    else:
      if row == height-1 and cols == height//2 or cols==height-row+height//2-1 or cols == cols==row+1-height//2-1:
        print('* ', end=' ')
      else:
        print('  ', end=' ')

  print()