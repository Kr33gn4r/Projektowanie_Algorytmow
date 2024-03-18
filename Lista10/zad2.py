from roboty import Fabryka, Robot
from random import choice, randint, uniform

class Kolejka():
    def __init__(self):
        self.kolejka = []

    def dodaj(self, typ=None, cena=None, zasieg=None, kamera=None):
        if typ not in ["AGV", "AFV", "ASV", "AUV"]:
            typ = choice(["AGV", "AFV", "ASV", "AUV"])
        if type(cena) != float:
            cena = round(uniform(0, 10000), 2)
        if type(zasieg) != int:
            zasieg = randint(0, 100)
        if kamera not in [0, 1]:
            kamera = randint(0, 1)

        self.kolejka.append(Robot(typ, cena, zasieg, kamera))

    def usun(self):
        try:
            robot = self.kolejka[0]
            print(f"Typ: {robot.typ}, Cena: {robot.cena}, Zasięg: {robot.zasieg}, Kamera: {robot.kamera}")
            self.kolejka.pop(0)
        except IndexError:
            print("Kolejka jest pusta, nie można nic usunąć")

    def wyczysc(self):
        for _ in range(len(self.kolejka)):
            self.usun()

if __name__ == "__main__":
    kolejka = Kolejka()
    for _ in range(10):
        kolejka.dodaj()
    kolejka.dodaj(typ="AGV", cena=420.69)
    kolejka.usun()
    print("------------")
    kolejka.wyczysc()
    kolejka.usun()
