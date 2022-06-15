# karatsuba is an optimized solution
# in multiplicatin of numbers,poly ....
# based on the divided and conquer approch
"""
x=a*10^(n/2)+b
y=c*10^(n/2)+d
x*y=(a*10^(n/2)+b)*(c*10^(n/2)+d)
=a*c*10^(n)+(ad+bc)*10^(n/2)+bd
we have four muliplication not good yet
we need to reduce the number of multplication
to three ,and these is by convert ad+bc = (a+b)(c+d)-ac-bd
=
O(n^1.5)=O(n^(log3)) < O(n^2)
"""
from sys import getsizeof

def karatsuba(x, y):
    """Function to multiply 2 numbers in a more efficient manner than the grade school algorithm"""
    if len(str(x)) == 1 or len(str(y)) == 1:
        return x * y
    else:
        n = max(len(str(x)), len(str(y)))
        nby2 = n // 2

        a = x // 10 ** (nby2)
        b = x % 10 ** (nby2)
        c = y // 10 ** (nby2)
        d = y % 10 ** (nby2)

        ac = karatsuba(a, c)
        bd = karatsuba(b, d)
        ad_plus_bc = karatsuba(a + b, c + d) - ac - bd

        # this little trick, writing n as 2*nby2 takes care of both even and odd n
        prod = ac * 10 ** (2 * nby2) + (ad_plus_bc * 10 ** nby2) + bd

        return prod
print(karatsuba(124521454645646456456456456456456464565464564565545645645, 52525686686884568798978978998954485))

