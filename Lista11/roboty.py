from __future__ import annotations
import random
import typing


class Roboty:
    robot = tuple[str, float, int, int]

    def __init__(self, n, path: typing.Optional[str] = None):
        self.n = n
        self.robots_list = self.generate_robots_list() if not path else self.read_robots_list_from_file(path)

    @staticmethod
    def generate_robot() -> robot:
        typ = random.choice(["AGV", "AFV", "ASV", "AUV"])
        # cena = round(random.uniform(0, 10000), 2)
        cena = round(random.uniform(0, 100), 2)
        zasieg = random.randint(0, 10)
        kamera = random.choice([0, 1])
        return typ, cena, zasieg, kamera

    def generate_robots_list(self) -> list[Roboty.robot]:
        robots_list = [self.generate_robot() for _ in range(self.n)]
        return robots_list

    @staticmethod
    def print_robots_list(robots_list) -> None:
        print("{:<5} {:<10} {:<10} {:<10}".format("TYP", "CENA", "ZASIĘG", "KAMERA"))
        for robot in robots_list:
            typ, cena, zasieg, kamera = robot
            print("{:<5} {:<10.2f} {:<10} {:<10}".format(typ, cena, zasieg, kamera))

    @staticmethod
    def save_robots_list_to_file(rts, filename: str) -> None:
        with open(filename, "w+") as f:
            for robot in rts:
                f.write(",".join(str(x) for x in robot) + "\n")

    @staticmethod
    def read_robots_list_from_file(filename: str) -> list[Roboty.robot]:
        robots_list = []
        with open(filename, "r") as f:
            for line in f:
                robot_data = line.strip().split(",")
                typ, cena, zasieg, kamera = robot_data
                cena = float(cena)
                zasieg = int(zasieg)
                kamera = int(kamera)
                robot = (typ, cena, zasieg, kamera)
                robots_list.append(robot)
        return robots_list

    def __call__(self, *args, **kwargs):
        self.save_robots_list_to_file(self.robots_list, 'robots.csv')
        self.robots_list = self.read_robots_list_from_file("robots.csv")
        self.print_robots_list(self.robots_list)


def main():
    n = int(input("Podaj długość listy robotów: "))
    roboty = Roboty(n)
    roboty()


if __name__ == "__main__":
    main()
