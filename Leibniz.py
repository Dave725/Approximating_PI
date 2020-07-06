import time
import math

def Leibniz (iteration):
    x = 1
    for i in range(0, iteration):
        denominator = 2 * i + 3
        if i % 2 == 0:
            x -= (1 / denominator)
        else:
            x += (1 / denominator)
    pi = x * 4
    return pi

def createPerror ():
    perrorl = []
    runtimel = []

    def func (i):
        start = time.time()
        iteration = i
        pi = Leibniz(iteration)
        perror = abs(pi - math.pi) / math.pi
        perrorl.append(float('{:.5f}'.format(perror * 100)))
        runtimel.append(float('{:.5f}'.format(time.time() - start)))

    l1 = [10 ** i for i in range(1, 7)]
    l2 = [i // 2 for i in l1]
    l3 = [i // 2 for i in l2]
    l4 = [i // 2 for i in l3]
    lis = sorted(l1 + l2 + l3 + l4)
    list = [i for i in lis if i >= 10]

    for i in list:
        func(i)

    return perrorl

perrorl = createPerror()

def display (i):
    start = time.time()
    pi = Leibniz(1000000)
    print("After {} iterations: {}".format(i - 1, Leibniz(i)))
    perror = abs(pi - math.pi) / math.pi
    print('Actual value of pi: {}'.format(math.pi))
    print("After {} iterations: {}".format(1000000, pi))
    print('Percentage error: {:.10f}%'.format(perror * 100))
    print("time elapsed: {:.10f}s".format(time.time() - start))
