import matplotlib.pyplot as plt
import Wallis, Basel, Leibniz
import Ramanujan, Machin, Archimedes

def level2 ():
    l1 = [10 ** i for i in range(1, 7)]
    l2 = [i // 2 for i in l1]
    l3 = [i // 2 for i in l2]
    l4 = [i // 2 for i in l3]
    lis = sorted(l1 + l2 + l3 + l4)
    xvals = [i for i in lis if i >= 10]
    basel = [float(i) for i in Basel.perrorl]
    wallis = [float(i) for i in Wallis.perrorl]
    leibniz = [float(i) for i in Leibniz.perrorl]

    plt.figure(figsize = (10, 8))
    ax = plt.subplot()
    plt.plot(xvals, basel, label = 'Basel problem')
    plt.plot(xvals, wallis, label = 'Wallis product')
    plt.plot(xvals, leibniz, label = 'Leibniz')
    plt.title('% error comparison for level 2 algorithm')
    plt.xlabel('iteration')
    plt.ylabel('% error')
    plt.xscale('log')
    plt.legend()
    # plt.ylim(0, 0.01)
    # plt.xlim(10**3, 10**6)
    plt.show()

def level3 ():
    xvals = range(2, 11)
    plt.figure(figsize = (10, 8))
    ax1 = plt.subplot()
    # plt.plot(xvals, Archimedes.perrorl,label='Archimedes')
    plt.plot(xvals, Machin.perrorHl, label = 'Hwang')
    # plt.plot(xvals, Machin.perrorMl, label = 'Machin')
    plt.plot(xvals, Ramanujan.perrorl, label = 'Ramanujan')
    plt.title('% error comparison for level 3 algorithm')
    plt.xlabel('iteration')
    plt.ylabel('% error')
    # plt.ylim(0,.0000000000001)
    plt.legend()
    plt.show()

# level2()
# level3()
