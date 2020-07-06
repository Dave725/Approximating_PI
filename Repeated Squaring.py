import math
import decimal
import fractions

def squaring (a, b):
    new_a = a ** 2 + b ** 2
    new_b = a * 2 * b
    return new_a, new_b

irra = math.pi
def driver ():
    a = math.pi
    print("Initial irrational: {}".format(decimal.Decimal(irra)))
    b = math.floor(a)
    for i in range(1, 7):
        a, b = squaring(a, b)
        num, den = round(b), round(a / irra)
        approx = decimal.Decimal(num / den)
        print("After {} iterations: {} \n   equal to {}/{}".format(i, approx,num,den))

driver()
