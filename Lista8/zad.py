import json
from random import uniform, randint, choice
from os.path import exists
from math import gcd
from numpy import linspace
from timeit import default_timer as timer
from matplotlib import pyplot as plt

class Robot:
    def __init__(self, typ, cena, zasieg, kamera):
        self.typ = typ
        self.cena = cena
        self.zasieg = zasieg
        self.kamera = kamera

class Fabryka:
    def __init__(self):
        self.lista_robotow = []

    def stworzRoboty(self, ilosc, alfa=0.5):
        self.lista_robotow = [Robot(typ = choice(["AGV", "AFV", "ASV", "AUV"]),
                                    cena = round(uniform(0, 10000), 2),
                                    zasieg = randint(0, 100),
                                    kamera = randint(0, 1))
                              for i in range(ilosc)]
        self.stworzHash(alfa, "cena")

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

    def zapiszRoboty(self, nazwa, sciezka = "/home/rskay/PycharmProjects/PWR/Sem4/Projektowanie Algorytmów/Lista8/"):
        if exists(sciezka + nazwa + ".json"):
            if input("Plik już istnieje, czy chcesz go nadpisać? TAK lub NIE: ").lower() == "nie":
                return 0
        dane = [{"typ" : robot.typ, "cena" : robot.cena, "zasieg" : robot.zasieg,
                "kamera" : robot.kamera} for robot in self.lista_robotow]
        with open(nazwa + ".json", "w") as f:
            json.dump(dane, f, indent=4)

    def wczytajRoboty(self, nazwa, sciezka = "/home/rskay/PycharmProjects/PWR/Sem4/Projektowanie Algorytmów/Lista8/", alfa=0.5):
        if not exists(sciezka + nazwa + ".json"):
            print("Plik nie istnieje, także nie da się go wczytać")
        else:
            with open(nazwa + ".json", "r") as f:
                dane = json.load(f)
            self.lista_robotow = [Robot(robot["typ"], robot["cena"], robot["zasieg"], robot["kamera"])
                                  for robot in dane]
        self.stworzHash(alfa, "cena")

    def _wczytajklucze(self, kombinacja):
        klucze = kombinacja.replace(' ', '').split(';')
        for k in range(4):
            match klucze[k][0].lower():
                case "n": klucze[k] = None
                case "[":
                    if k == 0:
                        klucze[k] = list(map(str, klucze[k][1:-1].split(",")))
                    elif k == 1:
                        klucze[k] = list(map(float, klucze[k][1:-1].split(",")))
                    else:
                        klucze[k] = list(map(int, klucze[k][1:-1].split(",")))
                case _:
                    if k == 0:
                        klucze[k] = [str(klucze[k])]
                    elif k == 1:
                        klucze[k] = [float(klucze[k])]
                    else:
                        klucze[k] = [int(klucze[k])]
        return klucze

    def wyszukajLiniowo(self, kombinacja):
        klucze = self._wczytajklucze(kombinacja)
        for robot in self.lista_robotow:
            if (klucze[0] == None or robot.typ in klucze[0]) and \
                    (klucze[1] == None or robot.cena in klucze[1]) and \
                    (klucze[2] == None or robot.zasieg in klucze[2]) and \
                    (klucze[3] == None or robot.kamera in klucze[3]):
                return (f"{robot.typ}, {robot.cena} zł, {robot.zasieg} km, {robot.kamera}")
        return "brak"

    def wyszukajBinarnie(self, parametr, wartosci, sortowanie=True):
        if sortowanie == True:
            posortowana_lista = \
                sorted(self.lista_robotow, key=lambda robot: getattr(robot, parametr.lower()))
        else: posortowana_lista = self.lista_robotow.copy()
        l = len(posortowana_lista)
        if wartosci.lower() == "none": return f"{self.lista_robotow[0].typ}, {self.lista_robotow[0].cena} zł, " \
                           f"{self.lista_robotow[0].zasieg} km, {self.lista_robotow[0].kamera}"
        elif parametr.lower() == "typ": wartosci = list(map(str, wartosci.split(",")))
        elif parametr.lower() == "cena": wartosci = list(map(float, wartosci.split(",")))
        else: wartosci = list(map(int, wartosci.split(",")))
        for klucz in wartosci:
            n = len(self.lista_robotow) // 2
            m = len(self.lista_robotow) // 2
            while m > 1:
                if getattr(posortowana_lista[n], parametr.lower()) == klucz:
                    return f"{posortowana_lista[n].typ}, {posortowana_lista[n].cena} zł, " \
                           f"{posortowana_lista[n].zasieg} km, {posortowana_lista[n].kamera}"
                m = round(m/2)
                n = n - m if getattr(posortowana_lista[n], parametr.lower()) > klucz else n + m
                if n < 0: n = 0
                elif n >= l: n = l - 1
        return "brak"

    def stworzHash(self, alfa, parametr):
        rozmiar = len(self.lista_robotow)
        rozmiar_hash = int(rozmiar / float(alfa))
        tablica_hashow = [None for _ in range(rozmiar_hash)]

        while True:
            a1 = randint(1, rozmiar_hash)
            a2 = randint(1, rozmiar_hash)
            if gcd(a1, rozmiar_hash) == 1 and gcd(a2, rozmiar_hash) == 1 \
                    and a1 % 2 == 1 and a2 % 2 == 1: break

        for robot in self.lista_robotow:
            # ( h2(k) + c1*i + c2*i^2 ) mod m
            i = 0
            index = (hash(getattr(robot, parametr.lower())) + a1 * i + a2 * (i ** 2)) % rozmiar_hash
            while tablica_hashow[index] is not None:
                i += 1
                index = (hash(getattr(robot, parametr.lower())) + a1 * i + a2 * (i ** 2)) % rozmiar_hash
            tablica_hashow[index] = robot
        self.tablica_hashow = tablica_hashow
        self.rozmiar_hash = rozmiar_hash
        self.a1 = a1
        self.a2 = a2

    def wyszukajHashem(self, parametr, wartosci, alfa="0.5", stworzHash=False):
        if stworzHash == True:
            self.stworzHash(alfa, parametr)

        if wartosci.lower() == "none": return f"{self.lista_robotow[0].typ}, {self.lista_robotow[0].cena} zł, " \
                           f"{self.lista_robotow[0].zasieg} km, {self.lista_robotow[0].kamera}"
        elif parametr.lower() == "typ": wartosci = list(map(str, wartosci.split(",")))
        elif parametr.lower() == "cena": wartosci = list(map(float, wartosci.split(",")))
        else: wartosci = list(map(int, wartosci.split(",")))

        for klucz in wartosci:
            i = 0
            while i < self.rozmiar_hash:
                index = (hash(klucz) + self.a1 * i + self.a2 * (i**2)) % self.rozmiar_hash
                if self.tablica_hashow[index] is None:
                    i += 1
                    continue
                if getattr(self.tablica_hashow[index], parametr.lower()) == klucz:
                    return f"{self.tablica_hashow[index].typ}, {self.tablica_hashow[index].cena} zł, " \
                           f"{self.tablica_hashow[index].zasieg} km, {self.tablica_hashow[index].kamera}"
                i += 1
            return "brak"

    def TimeGraph(self, alfa):
        t_lin, t_bin, t_hsh = [], [], []
        amounts = linspace(100, 10000, 100, dtype=int)
        for n in amounts:
            self.stworzRoboty(n, alfa)
            x = randint(0, n-1)
            cena = self.lista_robotow[x].cena
            self.lista_robotow = \
                sorted(self.lista_robotow, key=lambda robot: robot.cena)

            start = timer()
            self.wyszukajLiniowo(f"None;{cena};None;None")
            t_lin.append(timer() - start)
            start = timer()
            self.wyszukajBinarnie("cena", f"{cena}", False)
            t_bin.append(timer() - start)
            start = timer()
            self.wyszukajHashem("cena", f"{cena}")
            t_hsh.append(timer() - start)

        plt.plot(amounts, t_lin, c="red", label="Liniowe")
        plt.plot(amounts, t_bin, c="green", label="Binarne")
        plt.plot(amounts, t_hsh, c="blue", label="Hashowe")
        plt.suptitle("Porownanie czasów")
        plt.legend()
        plt.show()

f = Fabryka()
def zad1():
    f.stworzRoboty(10)
    f.przedstawRoboty()
    f.zapiszRoboty("zapisz")
    f.przedstawRoboty()
    print("")
    f.wczytajRoboty("test")
    f.przedstawRoboty()

def zad2():
    f.wczytajRoboty("test")
    print(f.wyszukajLiniowo(input("Kombinacja: ")))

def zad3():
    f.wczytajRoboty("test")
    print(f.wyszukajBinarnie(input("Parametr po którym chcesz posortować: "),
                             input("Wartości które chcesz wyszukać: ")))

def zad4():
    f.wczytajRoboty("test")
    print(f.wyszukajHashem(input("Parametr po którym chcesz hashować: "),
                           input("Wartości które chcesz wyszukać: "),
                           input("Współczynnik wypełnienia tablicy (0-1): "),
                           stworzHash=True))

def zad5():
    f.TimeGraph(input("Współczynnik wypełnienia tablicy (0-1): "))

zad5()