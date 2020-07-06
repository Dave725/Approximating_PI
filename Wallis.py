import math
import time

def Wallis_product (iteration):
    product = 1.0
    for n in range(1, iteration):
        product *= (4 * n ** 2) / (4 * n ** 2 - 1)
    return 2 * product

def createPerror():
    perrorl = []
    runtimel = []

    def func (i):
        start = time.time()
        pi = Wallis_product(i)
        perror = abs(pi - math.pi) / math.pi
        perrorl.append('{:.5f}'.format(perror * 100))
        runtimel.append('{:.5f}'.format(time.time() - start))

    l1 = [10**i for i in range(1,7)]
    l2 = [i//2 for i in l1]
    l3 = [i//2 for i in l2]
    l4 = [i//2 for i in l3]
    lis = sorted(l1+l2+l3+l4)
    list = [i for i in lis if i >= 10]

    for i in list:
        func(i)
    return perrorl

perrorl = createPerror()


def display():
    start = time.time()
    iteration = 1000000
    print('Actual value of pi: {}'.format(math.pi))
    pi = Wallis_product(iteration)
    print("After {} iterations: {}".format(iteration, pi))
    print("time elapsed: {:.10f}s".format(time.time() - start))
    perror = abs(pi - math.pi) / math.pi
    print('Percentage error: {:.10f}%'.format(perror * 100))

display()