#SQUARE ROOT CALCULATOR FOR COMPLEX NUMBER

import cmath

num = eval(input('Enter a number: '))

num_sqrt = cmath.sqrt(num)

print('The square root of {} is {:0.3f}+{:0.3f}j'.format(num,num_sqrt.real,num_sqrt.imag))