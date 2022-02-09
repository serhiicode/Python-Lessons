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
'''

height = int(input('Яка висота трикутника?\n'))

for row in range(height):
  for cols in range(height*2-1):
    if row == 0 and cols == height-1 or height-row-1 <= cols <= height+row-1 or row == height-1:
      print('* ', end=' ')
    else:
      print('  ', end=' ')
  print()