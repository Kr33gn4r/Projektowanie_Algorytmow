from timeit import Timer
from random import randint

class Gen:
    def __init__(self, size):
        self.size = size

    def genList(self):
        return [randint(-self.size, self.size) for i in range(self.size)]

    def genMatrix(self):
        return [[randint(-self.size, self.size) for i in range(self.size)] for j in range(self.size)]

def t(func, l1, l2=[]):
    if func == "mnozenie":
        return Timer(f"{func}({l1},{l2})", "from zad2 import mnozenie").timeit(1)
    else:
        return Timer(f"{func}({l1})", "from zad1 import najwiekszy, druginajwiekszy, srednia; from zad3 import graycode").timeit(1)

if __name__ == '__main__':
    #print(t('najwiekszy', Gen(1000000).genList()))
    #print(t('druginajwiekszy', Gen(1000000).genList()))
    #print(t('srednia', Gen(1000000).genList()))
    #print(t('mnozenie', Gen(100).genMatrix(), Gen(100).genMatrix()))
    print(t('graycode', Gen(20).genList()))
