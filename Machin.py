import decimal as d
import math
import time

start = time.time()

def arctan (x):  # Maclaurin series expansion for arctan
    res = x
    for i in range(0, iteration):
        odd = 2 * i + 3
        if i % 2 == 0:
            res -= (x ** odd) / odd
        else:
            res += (x ** odd) / odd
    return res

def Simplest ():
    pi = 4 * (arctan(1 / 2) + arctan(1 / 3))
    return d.Decimal(pi)

def Machin ():
    pi = 4 * (4 * arctan(1 / 5) - arctan(1 / 239))
    return d.Decimal(pi)

def Hwang ():
    pi = 4 * (183 * (arctan(1 / 239)) + 32 * arctan(1 / 1023) - 68 * (arctan(1 / 5832)) + 12 * (arctan(1 / 113021)) -
              100 * (arctan(1 / 6826318)) - 12 * (arctan(1 / 33366019650)) + 12 * (arctan(1 / 43599522992503626068)))
    return d.Decimal(pi)

def dis(iteration):
    print('Actual value of pi: {}'.format(math.pi))
    pi = Machin()
    print("After {} iterations: {}".format(iteration, pi))
    perror = abs(pi - d.Decimal(math.pi)) / d.Decimal(math.pi)
    print('Percentage error: {:.20f}%'.format(perror * 100))
    print("time elapsed: {:.10f}s".format(time.time() - start))

def createPerror():
    perrorMl = []
    perrorHl = []
    for i in range(2, 11):
        global iteration
        iteration = i
        pim = Machin()
        pih = Hwang()
        perrorM = abs(pim - d.Decimal(math.pi)) / d.Decimal(math.pi)
        perrorH = abs(pih - d.Decimal(math.pi)) / d.Decimal(math.pi)
        perrorMl.append(float('{:.25f}'.format(perrorM*100)))
        perrorHl.append(float('{:.25f}'.format(perrorH*100)))
    return perrorMl, perrorHl

perrorMl, perrorHl = createPerror()
