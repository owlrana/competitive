# https://www.hackerrank.com/challenges/class-1-dealing-with-complex-numbers/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

inp1 = input()
inp2 = input()

#splitting the inputs into two parts, real [1] and imaginary [2] as a list
split1 = inp1.split()
split2 = inp2.split()

#assigning values of real [1] and imaginary [2] parts into float variables
real1 = split1[0]
real2 = split2[0]
imaginary1 = float(split1[1])
imaginary2 = float(split2[1])

#sanity check to see if the code is working
#print(real1,'+',imaginary1,'i')
#print(real2,'+',imaginary2,'i')