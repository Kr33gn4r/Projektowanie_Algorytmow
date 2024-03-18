from math import floor, sqrt
from itertools import compress

def sito(n):
    if n < 2: return False
    tab = [True for i in range(n+1)]
    tab[0] = False
    tab[1] = False
    for i in range(2, floor(sqrt(n))+1):
        if tab[i] == True:
            mult = 2
            while mult * i <= n:
                tab[mult * i] = False
                mult += 1
    return tab

if __name__ == '__main__':
    liczba = int(input("Podaj liczbę: "))
    wynik = sito(liczba)
    print(list(compress(range(len(wynik)), wynik)))