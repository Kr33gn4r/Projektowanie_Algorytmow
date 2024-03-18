import matplotlib.style
from matplotlib import pyplot as plt
from random import randint
from timeit import Timer
matplotlib.style.use('ggplot')

def plot_times(n : int):
    t_naive, t_FFT, t = [], [], []
    timeit_howmany = 1
    i = 1
    j = lambda x: 2**(x-1) #zamień na 2**(x-1) aby mieć co potęgi 2 albo x aby mieć każdy
    while j(i) <= n:
        p1 = [randint(-j(i), j(i)) for _ in range(j(i))]
        p2 = [randint(-j(i), j(i)) for _ in range(j(i))]

        t.append(j(i))
        print(j(i))
        t_naive.append(Timer(f"naive_polynomial_multiplication({p1},{p2})", "from zad1 import naive_polynomial_multiplication").timeit(timeit_howmany))
        t_FFT.append(Timer(f"FFT_polynomial_multiplication({p1},{p2})", "from zad3 import FFT_polynomial_multiplication").timeit(timeit_howmany))
        i += 1

    plt.plot(t, t_naive, color="tab:blue", label="Naiwne mnożenie")
    plt.plot(t, t_FFT, color="tab:orange", label="Mnożenie FFT")
    plt.xlabel("Rozmiar wielomianu")
    plt.ylabel(f"Czas działania działania algorytmu {timeit_howmany} razy")
    plt.title("Porównanie czasów działania algorytmów mnożenia wielomianów")
    plt.legend()
    plt.show()

if __name__ == "__main__":
    n = int(input("Do jakiego rozmiaru wielomianu? : "))
    plot_times(n)

