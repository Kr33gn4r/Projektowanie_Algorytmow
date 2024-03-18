from roboty import Fabryka, Robot
from random import choice, randint, uniform
class Lista():
    def __init__(self):
        self.lista = []
        self.adres = 0
        self.dlugosc = 0
        # klucz to poprostu od 0 do n
        # adres wskazuje na indeks pierwszego elementu listy

    def dodaj(self, typ=None, cena=None, zasieg=None, kamera=None, pos=-1):
        if typ not in ["AGV", "AFV", "ASV", "AUV"]:
            typ = choice(["AGV", "AFV", "ASV", "AUV"])
        if type(cena) != float:
            cena = round(uniform(0, 10000), 2)
        if type(zasieg) != int:
            zasieg = randint(0, 100)
        if kamera not in [0, 1]:
            kamera = randint(0, 1)

        if self.dlugosc == 0:
            self.adres = len(self.lista)
            self.lista.append([Robot(typ, cena, zasieg, kamera), -1])
        elif pos == 0:
            self.lista.append([Robot(typ, cena, zasieg, kamera), self.adres])
            self.adres = len(self.lista) - 1
        elif pos == -1:
            adr = self.adres
            for i in range(self.dlugosc):
                adr = self.lista[adr][1]
            self.lista[adr][1] = len(self.lista)
            self.lista.append([Robot(typ, cena, zasieg, kamera), -1])
        else:
            pos = pos if pos >= 0 else self.dlugosc + pos
            adr = self.adres
            for i in range(pos):
                adr = self.lista[adr][1]
            tempadr = self.lista[adr][1]
            self.lista[adr][1] = len(self.lista)
            self.lista.append([Robot(typ, cena, zasieg, kamera), tempadr])
        self.dlugosc += 1

    def usun(self, pos=-1):
        if self.dlugosc == 0:
            print("Lista jest pusta")
        elif pos == 0:
            tempadr = self.lista[self.adres][1]
            self.lista[self.adres] = [None, None]
            self.adres = tempadr
            self.dlugosc -= 1
        else:
            pos = pos if pos >= 0 else self.dlugosc + pos
            adr = self.adres
            for i in range(pos - 1):
                adr = self.lista[adr][1]
            tempadr = self.lista[adr][1]
            try:
                nextempadr = self.lista[tempadr][1]
            except IndexError:
                nextempadr = -1
            self.lista[adr][1] = nextempadr
            self.lista[tempadr] = [None, None]
            self.dlugosc -= 1

    def wyszukaj(self, pos=-1):
        if pos == 0:
            return self.lista[self.adres][0]
        else:
            pos = pos if pos >= 0 else self.dlugosc + pos
            adr = self.adres
            for i in range(pos):
                adr = self.lista[adr][1]
            return self.lista[adr][0]

    def posortuj(self):
        nowalista = []
        adres = -1
        for i in range(self.dlugosc):
            curr = self.adres
            maxim = self.adres
            maxpos = 0
            for j in range(self.dlugosc):
                if self.lista[curr][0].cena > self.lista[maxim][0].cena:
                    maxim = curr
                    maxpos = j
                curr = self.lista[curr][1]
            nowalista.append([self.lista[maxim][0], adres])
            adres += 1
            self.usun(pos=maxpos)
        self.lista = nowalista
        self.adres = self.dlugosc - 1
        self.dlugosc = len(nowalista)

if __name__ == "__main__":
    l = Lista()
    for i in range(10):
        l.dodaj()
    l.dodaj(pos=4)
    l.dodaj(pos=0)
    l.usun(pos=3)
    l.usun()
    l.usun(pos=0)
    print(l.lista)
    l.posortuj()
    print(l.lista)
    print(l.dlugosc, l.adres)
    for i in range(l.dlugosc):
        print(i)
        print(l.wyszukaj(pos=i).cena)


