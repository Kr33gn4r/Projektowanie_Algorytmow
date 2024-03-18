import json
from random import uniform, randint, choice
from os.path import exists
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