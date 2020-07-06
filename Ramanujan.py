import math
import time
import decimal as d

start = time.time()

def Ramanujan (iteration):
    pi = 0
    for n in range(0, iteration):
        x = 4 * n
        pi += (math.factorial(x) * (1103 + 26390 * n)) / ((math.factorial(n) ** 4) * (396 ** x))
    pi *= (2 * math.sqrt(2)) / 9801
    return d.Decimal(1 / pi)

def display ():
    print('Actual value of pi: {}'.format(d.Decimal(math.pi)))
    iteration = 3
    pi = Ramanujan(iteration)
    print("After {} iterations: {}".format(iteration, pi))
    perror = abs(pi - d.Decimal(math.pi)) / d.Decimal(math.pi)
    print('Percentage error: {:.10f}%'.format(perror * 100))
    print("time elapsed: {:.3f}s".format(time.time() - start))

def createPerror ():
    perrorl = []
    for i in range(2, 11):
        pi = Ramanujan(i)
        perror = abs(pi - d.Decimal(math.pi)) / d.Decimal(math.pi)
        perrorl.append(float('{:.25f}'.format(perror * 100)))
    return perrorl

display()
