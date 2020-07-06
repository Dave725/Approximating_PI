import decimal as d
import math
import time

def basel (iteration):
    sum = 0
    for i in range(1, iteration):
        sum += 1.0 / i ** 2
    pi = math.sqrt(6 * sum)
    return pi

def createPerror ():
    perrorl = []
    runtimel = []

    def func (i):
        start = time.time()
        pi = basel(i)
        perror = abs(pi - math.pi) / math.pi
        perrorl.append('{:.5f}'.format(perror * 100))
        runtimel.append('{:.5f}'.format(time.time() - start))

    l1 = [10 ** i for i in range(1, 7)]
    l2 = [i // 2 for i in l1]
    l3 = [i // 2 for i in l2]
    l4 = [i // 2 for i in l3]
    lis = sorted(l1 + l2 + l3 + l4)
    list = [i for i in lis if i >= 10]

    for i in list:
        func(i)

    return perrorl


def display ():
    print('Actual value of pi: {}'.format(math.pi))
    start = time.time()
    iteration = 1000000
    pi = basel(iteration)
    print("After {} iterations: {}".format(iteration, pi))
    print("time elapsed: {:.10f}s".format(time.time() - start))
    perror = abs(pi - math.pi) / math.pi
    print('Percentage error: {:.10f}%'.format(perror * 100))

display()

