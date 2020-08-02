# https://www.hackerrank.com/challenges/class-1-dealing-with-complex-numbers/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

inp1 = input()
inp2 = input()

#assigning values of real [1] and imaginary [2] parts into float variables
real1 = float(inp1.split()[0])
real2 = float(inp2.split()[0])
imag1 = float(inp1.split()[1])
imag2 = float(inp2.split()[1])

#sanity check to see if the code is working
print(real1,'+',imag1,'i')
print(real2,'+',imag2,'i')

#adding the numbers
print(real1+real2, '+', imag1+imag2, 'i')

#subtracting the numbers
print(real1-real2, '-', imag1-imag2, 'i')

#multplying the numbers
print(real1*real2, '*', imag1*imag2, 'i')

#dividing the numbers
print(real1/real2, '/', imag1/imag2, 'i')