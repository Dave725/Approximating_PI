import math

def binomial_coefficient (n, k):
    ans = math.factorial(n) / (math.factorial(k) * math.factorial(n - k))
    return ans

def binomial_expansions (x, y, n):
    result = []
    for i in range(0, n + 1):
        val = binomial_coefficient(n, i) * pow(x, (n - i)) * pow(y, i)
        result.append(val)
    return result

def driver():
    x,y = math.pi,3
    for n in range (1,10):
        arr = binomial_expansions(x,y,n)

