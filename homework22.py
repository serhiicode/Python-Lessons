'''
            *
          * * *
        * * * * *
      * * * * * * *
    * * * * * * * * *
  * * * * * * * * * * *
* * * * * * * * * * * * *
  *         *         * 
    *       *       *
      *     *     *
        *   *   *
          * * *
            *

'''
height = int(input('Яка висота ромба?\n'))

for row in range(height):
  for cols in range(height):
    if 0 <= row <= height//2:
      if row == 0 and cols == height//2:
        print('* ', end=' ')
      else:
        print('  ', end=' ')
    #else:
      #if cols == row-height+1 or cols == height+row:
        #print('* ', end=' ')
      #else:
        #print('  ', end=' ')

  print()