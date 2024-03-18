import matplotlib.pyplot as plt
import matplotlib.style
from math import sqrt
from timeit import Timer
from zad1 import rozklad
matplotlib.style.use('ggplot')

def RNWD(a, b):
    atab = rozklad(a)
    btab = rozklad(b)
    rnwd = 1
    for x in atab:
        if x in btab:
            btab.remove(x)
            rnwd *= x
    return rnwd

def ENWD(a, b):
    if a % b == 0: return b
    else: return ENWD(b, a%b)

def time(n, m):
    rnwd, enwd, ql = [], [], []
    for q in range(n+1, m+1):
        ql.append(q)
        rnwd.append((Timer(f"RNWD({n},{q})", "from zad3 import RNWD").timeit(1)))
        enwd.append((Timer(f"ENWD({n},{q})", "from zad3 import ENWD").timeit(1)))
    plt.plot(ql, rnwd, label='RNWD', color='tab:orange')
    plt.plot(ql, enwd, label='ENWD', color='tab:blue')
    plt.title(f"Czas działania algorytmów RNWD i ENWD\ndla n = {n} i m = {m}")
    plt.legend()
    plt.show()

if __name__ == "__main__":
    n = int(input("Podaj n: "))
    m = int(input("Podaj m: "))
    time(n, m)
    #print(RNWD(n, m), ENWD(n, m))