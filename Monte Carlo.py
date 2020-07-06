import random
import time
import math

def monte_carlo (ran):
    inside, total = 0.0, 0.0
    for i in range(0, ran):
        x = random.uniform(-1.0, 1.0)
        y = random.uniform(-1.0, 1.0)
        total += 1
        if x * x + y * y <= abs(1):
            inside += 1
        ratio = inside / total
    return 4 * ratio

start = time.time()
iteration = 100000000
pi = monte_carlo(iteration)
print("After {} iterations: {}".format(iteration, pi))
perror = abs(pi - math.pi) / math.pi
print('Percentage error: {:.10f}%'.format(perror * 100))
print("time elapsed: {:.10f}s".format(time.time() - start))
