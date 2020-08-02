# https://www.hackerrank.com/challenges/class-1-dealing-with-complex-numbers/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
# install numpy manually using pip3, if using python3 

import numpy

inp1 = input()
inp2 = input()

#assigning values of real [1] and imaginary [2] parts into float variables
real1 = float(inp1.split()[0])
real2 = float(inp2.split()[0])
imag1 = float(inp1.split()[1])*1j
imag2 = float(inp2.split()[1])*1j

num1 = real1 + imag1
num2 = real2 + imag2

#sanity check to see if the code is working
#print(num1)
#print(num2)

def complex_print(a):
    if a.imag >=0:
        sign = '+'
    elif a.imag < 0:
        sign = '-'
    print(a.real, sign, abs(a.imag), '\bi')

complex_print(num1+num2)
complex_print(num1-num2)
complex_print(numpy.around(num1*num2, 2))
complex_print(numpy.around(num1/num2, 2))
complex_print(numpy.around(abs(num1), 2))
complex_print(numpy.around(abs(num2), 2))