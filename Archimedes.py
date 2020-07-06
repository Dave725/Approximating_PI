import math
import time

start = time.time()

def calcNewSide (s):
    hs = s / 2.0
    a = math.sqrt(1 - hs ** 2)
    b = 1 - a
    snew = math.sqrt(b ** 2 + hs ** 2)
    return a, snew

def archimedes (ran):
    s = 1.0
    n = 6
    for i in range(0, ran):
        n *= 2
        a, snew = calcNewSide(s)
        s = snew
    return snew, n, a

def createPerror ():
    perrorl = []
    runtimel = []

    for i in range(2, 11):
        snew, n, a = archimedes(i)
        pi_in = (snew * n) / 2
        pi_out = pi_in * (1 / a)
        runtimel.append(float('{:.5f}'.format(time.time() - start)))
        perror = abs(pi_in - math.pi) / math.pi
        perror2 = abs(pi_out - math.pi) / math.pi
        perro = (perror + perror2) / 2
        perrorl.append(float('{:.5f}'.format(perro * 100)))

    return perrorl

perrorl = createPerror()

def display (snew, n, a):
    pi_in = (snew * n) / 2
    pi_out = pi_in * (1 / a)
    print('Actual value of pi: {}'.format(math.pi))
    print('After  iterations: {} < pi < {}'.format(pi_in, pi_out))
    perror = abs(pi_in - math.pi) / math.pi
    perror2 = abs(pi_out - math.pi) / math.pi
    print('Percentage error: between {:.10f}% and {:.10f}%'.format(perror * 100, perror2 * 100))
    print("time elapsed: {:.3f}s".format(time.time() - start))
