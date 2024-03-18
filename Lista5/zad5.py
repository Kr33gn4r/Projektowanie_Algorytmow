import matplotlib.pyplot as plt
import matplotlib.style
from random import randint
from timeit import Timer
matplotlib.style.use('ggplot')
n = int(input("Podaj krok listy: "))
x = [i*n for i in range(1, 101)]

naj, drnaj, sre, marg = [], [], [], []
for i in range(1, 101):
    tab = [randint(-i*n, i*n) for j in range(i*n)]
    naj.append(Timer(f"start_najwiekszy({tab})", "from zad2 import start_najwiekszy").timeit(1))
    drnaj.append(Timer(f"start_druginajwiekszy({tab})", "from zad2 import start_druginajwiekszy").timeit(1))
    sre.append(Timer(f"start_srednia({tab})", "from zad2 import start_srednia").timeit(1))
    marg.append(Timer(f"margesort({tab}, 0, {i*n-1})", "from zad3 import margesort").timeit(1))

plt.plot(x, naj, label='największy', color='red')
plt.plot(x, drnaj, label='drugi największy', color='green')
plt.plot(x, sre, label='średnia', color='blue')
plt.plot(x, marg, label='mergesort', color='black')
plt.title(f"Czas wykonywania funkcji rekurencyjnych dla kroku {n}")
plt.legend()
plt.show()