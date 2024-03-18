import json
import numpy as np
import matplotlib.pyplot as plt
from random import uniform, randint, choice
from os.path import exists
from timeit import default_timer as timer
from math import sqrt, ceil
class Robot:
    def __init__(self, typ, cena, zasieg, kamera):
        self.typ = typ
        self.cena = cena
        self.zasieg = zasieg
        self.kamera = kamera

class Fabryka:
    def __init__(self):
        self.lista_robotow = []

    def stworzRoboty(self, ilosc):
        self.lista_robotow = [Robot(typ = choice(["AGV", "AFV", "ASV", "AUV"]),
                                    cena = round(uniform(0, 10000), 2),
                                    zasieg = randint(0, 100),
                                    kamera = randint(0, 1))
                              for i in range(ilosc)]
    def przedstawRoboty(self):
        print(f"+{'-' * 5}+{'-' * 14}+{'-' * 8}+{'-' * 8}+")
        print(f"|{' ' * 1}TYP{' ' * 1}|"
              f"{' ' * 5}CENA{' ' * 5}|"
              f"{' ' * 1}ZASIEG{' ' * 1}|"
              f"{' ' * 1}KAMERA{' ' * 1}|")
        for robot in self.lista_robotow:
            x = len(f"{robot.cena : 0.2f}")
            print(f"+{'-' * 5}+{'-' * 14}+{'-' * 8}+{'-' * 8}+")
            print(f"|{' ' * 1}{robot.typ}{' ' * 1}|"
                  f"{' ' * (10 - x)}{robot.cena : 0.2f}{' ' * 1}zł{' ' * 1}|"
                  f"{' ' * (4 - len(str(robot.zasieg)))}{robot.zasieg}{' ' * 1}km{' ' * 1}|"
                  f"{' ' * 2}{'jest' if robot.kamera == 0 else 'brak'}{' ' * 2}|")

    def zapiszRoboty(self, nazwa, sciezka = "/home/rskay/PycharmProjects/PWR/Sem4/Projektowanie Algorytmów/Lista9/"):
        if exists(sciezka + nazwa + ".json"):
            if input("Plik już istnieje, czy chcesz go nadpisać? TAK lub NIE: ").lower() == "nie":
                return 0
        dane = [{"typ" : robot.typ, "cena" : robot.cena, "zasieg" : robot.zasieg,
                "kamera" : robot.kamera} for robot in self.lista_robotow]
        with open(nazwa + ".json", "w") as f:
            json.dump(dane, f, indent=4)

    def wczytajRoboty(self, nazwa, sciezka = "/home/rskay/PycharmProjects/PWR/Sem4/Projektowanie Algorytmów/Lista9/"):
        if not exists(sciezka + nazwa + ".json"):
            print("Plik nie istnieje, także nie da się go wczytać")
        else:
            with open(nazwa + ".json", "r") as f:
                dane = json.load(f)
            self.lista_robotow = [Robot(robot["typ"], robot["cena"], robot["zasieg"], robot["kamera"])
                                  for robot in dane]

# Heapsort z krokami
def stepheapify(arr, n, i, steps):
    pivot = i
    l = 2 * i + 1
    r = 2 * i + 2
    steps.append([steps[-1][0] + 1,
                f"Czy lewo = {l} jest mniejsze niż długośc listy = {n} oraz czy cena "
                f"pivota jest mniejsza niż cena lewa?", steps[-1][2]].copy())
    if l < n and arr[pivot].cena < arr[l].cena:
        pivot = l
        steps.append([steps[-1][0]+1, "Tak, zamień pivota na liczbe l", steps[-1][2]].copy())
    else:
        steps.append([steps[-1][0] + 1, "Nie, przejdź dalej", steps[-1][2]].copy())

    steps.append([steps[-1][0] + 1,
                f"Czy prawo = {r} jest mniejsze niż długośc listy = {n} oraz czy cena "
                f"pivota jest mniejsza niż cena prawa?", steps[-1][2]].copy())
    if r < n and arr[pivot].cena < arr[r].cena:
        pivot = r
        steps.append([steps[-1][0] + 1, "Tak, zamień pivota na liczbe r", steps[-1][2]].copy())
    else:
        steps.append([steps[-1][0] + 1, "Nie, przejdź dalej", steps[-1][2]].copy())


    steps.append([steps[-1][0] + 1, f"Czy pivot się zmienił?", steps[-1][2]].copy())
    if pivot != i:
        arr[i], arr[pivot] = arr[pivot], arr[i]
        temp = steps[-1][2].copy()
        temp[i], temp[pivot] = temp[pivot], temp[i]
        steps.append([steps[-1][0] + 1, f"Tak, zamień je miejscami i ponów kopcowanie", temp])
        stepheapify(arr, n, pivot, steps)
    else: steps.append([steps[-1][0] + 1, f"Nie, zostaw kopiec", steps[-1][2]].copy())

def stepheapsort(arr, steps):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        stepheapify(arr, n, i, steps)
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        temp = steps[-1][2].copy()
        temp[0], temp[i] = temp[i], temp[0]
        steps.append([steps[-1][0] + 1, f"Zamień początek i i-te miejsce = {i}", temp])
        stepheapify(arr, i, 0, steps)

def stepheap(arr):
    w = [a.cena for a in arr]
    x = np.argsort(np.argsort(w))
    y = [[0, "Start", x]]
    stepheapsort(arr, y)
    for el in y:
        print(f"{el[0]}. {el[1]}")
        print(f"{el[2]}")

# Heapsort bez kroków
def heapify(arr, n, i):
    pivot = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[pivot].cena < arr[l].cena:
        pivot = l

    if r < n and arr[pivot].cena < arr[r].cena:
        pivot = r

    if pivot != i:
        arr[i], arr[pivot] = arr[pivot], arr[i]
        heapify(arr, n, pivot)

def heapsort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)

# Quicksort z krokami

def steppartition(arr, l, r, steps):
    pivot = arr[r].cena
    x = l - 1
    for y in range(l, r):
        steps.append(
            [steps[-1][0] + 1, f"Czy idąc po pętli {arr[y].cena} jest niewiększa niż piwot = {pivot}?", steps[-1][2].copy()])
        if arr[y].cena <= pivot:
            x += 1
            arr[x], arr[y] = arr[y], arr[x]
            temp = steps[-1][2].copy()
            temp[x], temp[y] = temp[y], temp[x]
            steps.append(
                [steps[-1][0] + 1, f"Tak, zwiększ indeks niski o jeden oraz zamień wartości jego oraz"
                                   f"wartości indeksu z pętli", temp])
        else:
            steps.append(
                [steps[-1][0] + 1, f"Nie, przejdź dalej", steps[-1][2].copy()])

    arr[x+1], arr[r] = arr[r], arr[x+1]
    temp = steps[-1][2].copy()
    temp[x+1], temp[r] = temp[r], temp[x+1]
    steps.append(
        [steps[-1][0] + 1, f"Zamień miejscami wartości z indeksem niskim + 1 i wysokim i zwróć indeks niski + 1", temp])
    return x+1

def stepquicksort(arr, l, r, steps):
    steps.append([steps[-1][0] + 1, f"Czy wartość niska = {l} jest mniejsza niż wysoka = {r}?", steps[-1][2].copy()])
    if l < r:
        steps.append(
            [steps[-1][0] + 1, f"Tak, znajdujemy pozycję partycji", steps[-1][2].copy()])
        p = steppartition(arr, l, r, steps)
        stepquicksort(arr, l, p-1, steps)
        stepquicksort(arr, p+1, r, steps)
    else:
        steps.append(
            [steps[-1][0] + 1, f"Nie, zostawiamy ten kawałek w spokoju", steps[-1][2].copy()])

def stepquick(arr):
    w = [a.cena for a in arr]
    x = np.argsort(np.argsort(w))
    y = [[0, "Start", x]]
    stepquicksort(arr, 0, len(arr)-1, y)
    for el in y:
        print(f"{el[0]}. {el[1]}")
        print(f"{el[2]}")

# Quicksort bez kroków

def partition(arr, l, r):
    pivot = arr[r].cena
    x = l - 1
    for y in range(l, r):
        if arr[y].cena <= pivot:
            x += 1
            arr[x], arr[y] = arr[y], arr[x]
    arr[x+1], arr[r] = arr[r], arr[x+1]
    return x+1

def quicksort(arr, l, r):
    if l < r:
        p = partition(arr, l, r)
        quicksort(arr, l, p-1)
        quicksort(arr, p+1, r)

# Countsort
def countsort(arr):
    count = [0 for _ in range(101)]
    for r in arr:
        count[r.zasieg] += 1
    for i in range(1, 101):
        count[i] += count[i-1]

    out = [None] * len(arr)
    for i in range(len(arr) - 1, -1, -1):
        z = arr[i].zasieg
        count[z] -= 1
        pos = count[z]
        out[pos] = arr[i]
    return out

# Radixsort

def radixsort(matrix, col=0):
    if col >= len(matrix[0]):
        return matrix
    max_val = max(row[col] for row in matrix)
    exp = 1                             # eksponent 10^(exp-1)

    while max_val // exp > 0:
        matrix = countingsort(matrix, col, exp)
        exp *= 10

    # Przesuwanie się po kolumnach jeżeli są identyczne
    idx = 0
    while idx < len(matrix):
        end = idx + 1
        while end < len(matrix) and matrix[idx][0:col + 1] == matrix[end][0:col+1]:
            # Powyższa pętla sprawdza czy się powtarza wartośc pomiędzy rzędem id a rzędem end dla
            # pierwszych col kolumn, jeżeli tak to stwórz nową macierz zawierającą je i wrzuć do radixa
            # przesuwając aktualną kolumnę o jeden w prawo
            end += 1
        group = matrix[idx:end]
        if len(group) > 1:              # Sprawdź czy grupa składa się z więcej niż jednego rzędu
            matrix[idx:end] = radixsort(group, col + 1)
        idx = end
    return matrix

def countingsort(matrix, col, exp):
    count = [0] * 10                    # Dziesięć cyfr
    out = [0] * len(matrix)

    for row in matrix:
        digit = (row[col] // exp) % 10
        count[digit] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    for row in reversed(matrix):
        digit = (row[col] // exp) % 10
        count[digit] -= 1
        out[count[digit]] = row

    return out

def plot(f : Fabryka, n=1000):
    t_heap, t_quick, t_count, t_radix = [], [], [], []
    robot_arr = [_ for _ in range(10, n + 1, 10)]
    for i in robot_arr:
        print(i)
        f.stworzRoboty(i)

        start = timer()
        heapsort(f.lista_robotow.copy())
        t_heap.append(timer() - start)

        start = timer()
        quicksort(f.lista_robotow.copy(), 0, len(f.lista_robotow)-1)
        t_quick.append(timer() - start)

        start = timer()
        countsort(f.lista_robotow)
        t_count.append(timer() - start)

        ceilsqrt = ceil(sqrt(i))
        matrix = [[randint(0, ceilsqrt) for _ in range(i)] for __ in range(i)]
        start = timer()
        radixsort(matrix)
        t_radix.append(timer() - start)

    fig, ax = plt.subplots()
    ax.plot(robot_arr, t_heap, c="red", label="Heapsort")
    ax.plot(robot_arr, t_quick, c="green", label="Quicksort")
    ax.plot(robot_arr, t_count, c="blue", label="Countsort")
    ax.plot(robot_arr, t_radix, c="black", label="Radixsort")
    plt.legend()
    plt.show()

f = Fabryka()

def zad1():
    f.stworzRoboty(10)
    stepheap(f.lista_robotow)
    f.przedstawRoboty()

def zad2():
    f.stworzRoboty(10)
    stepquick(f.lista_robotow)
    f.przedstawRoboty()

def zad3():
    f.stworzRoboty(10)
    f.lista_robotow = countsort(f.lista_robotow)
    f.przedstawRoboty()

def zad4():
    tab = [
        [1, 2, 3, 4],
        [7, 8, 10, 10],
        [5, 2, 1, 3],
        [7, 6, 10, 12],
        [7, 8, 10, 13],
        [2, 1, 3, 7]
    ]
    tab = radixsort(tab)
    for row in tab:
        print(row)

def zad5():
    plot(f)

zad2()
