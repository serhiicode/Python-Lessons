'''
            *
          * * *
        * * * * *
      * * * * * * *
    * * * * * * * * *
  * * * * * * * * * * *
* * * * * * * * * * * * *
  *                   * 
    *               *
      *           *
        *       *
          *   *
            *

розбити іф ще на 1 іф котрий буде перевіряти рядки, якщо з першого по 8й то одне а якщо після то інше
'''

height = int(input('Яка висота ромба?\n'))
if height % 2 == 0:
  width = height + 1
else:
  width = height

for row in range(height):
  for cols in range(width):
    if 0 <= row <= height/2:
      if row == 0 and cols == height/2 or height/2-row <= cols <= height/2+row or row == height/2:
        print('* ', end=' ')
      else:
        print('  ', end=' ')
    else:
      if row == height-1 and cols == height/2 or cols==height-row:
        print('* ', end=' ')
      else:
        print('  ', end=' ')

  print()