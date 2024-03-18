from roboty import Fabryka, Robot
from random import choice, randint, uniform

class Stos():
    def __init__(self):
        self.stos = []

    def dodaj(self, typ=None, cena=None, zasieg=None, kamera=None):
        if typ not in ["AGV", "AFV", "ASV", "AUV"]:
            typ = choice(["AGV", "AFV", "ASV", "AUV"])
        if type(cena) != float:
            cena = round(uniform(0, 10000), 2)
        if type(zasieg) != int:
            zasieg = randint(0, 100)
        if kamera not in [0, 1]:
            kamera = randint(0, 1)

        self.stos.append(Robot(typ, cena, zasieg, kamera))

    def usun(self):
        try:
            robot = self.stos[-1]
            print(f"Typ: {robot.typ}, Cena: {robot.cena}, Zasięg: {robot.zasieg}, Kamera: {robot.kamera}")
            self.stos.pop(-1)
        except IndexError:
            print("Stos jest pusty, nie można nic usunąć")

    def wyczysc(self):
        for _ in range(len(self.stos)):
            self.usun()

if __name__ == "__main__":
    stos = Stos()
    for _ in range(10):
        stos.dodaj()
    stos.dodaj(typ="AGV", cena=420.69)
    stos.usun()
    print("------------")
    stos.wyczysc()
    stos.usun()
