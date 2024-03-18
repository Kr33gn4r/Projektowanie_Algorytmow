import matplotlib.pyplot as plt
from zad4 import t, Gen

def listgen(step, func):
    lst = []
    for i in range(1, 11):
        if func == 'mnozenie':
            lst.append(t(func, Gen(i*step).genMatrix(), Gen(i*step).genMatrix()))
        else:
            lst.append(t(func, Gen(i*step).genList()))
    return lst

n = int(input("Krok: "))
nlist = [i * n for i in range(1, 11)]

plt.plot(nlist, listgen(n, 'najwiekszy'), color="red", label="najwiekszy")
plt.plot(nlist, listgen(n, 'druginajwiekszy'), color="orange", label="druginajwiekszy")
plt.plot(nlist, listgen(n, 'srednia'), color="green", label="srednia")
#plt.plot(nlist, listgen(n, 'mnozenie'), color="blue", label="mnozenie")
#plt.plot(nlist, listgen(n, 'graycode'), color="purple", label="graycode")
plt.legend()
plt.show()