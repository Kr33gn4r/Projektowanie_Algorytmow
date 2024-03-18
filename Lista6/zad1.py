from math import sqrt, floor
def rozklad(liczba, dz_list=[], dzielnik=2):
    f = True
    for d in range(dzielnik, floor(sqrt(liczba)) + 1):
        if liczba % d == 0:
            dz_list.append(d)
            f = False
            rozklad(liczba//d, dz_list, d)
            break
    if f:
        dz_list.append(liczba)
    return dz_list

if __name__ == '__main__':
    liczba = int(input("Podaj liczbę do rozkładu: "))
    print(rozklad(liczba))