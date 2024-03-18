import json, sys
class Automat:
    def __init__(self, file):
        with open(file) as f:
            data = json.load(f)
        self.Q = data['Q']
        self.Epsilon = data['Epsilon']
        self.Delta = data['Delta']
        self.Start = data['Start']
        self.Stop = data['Stop']
        status = self.test_correctness()
        if status: sys.exit(status)

    def test_correctness(self):
        if self.Start == '' or self.Start not in self.Q: return "Start jest pusty lub nie zawiera się w Q"
        for q in self.Q:
            for e in self.Epsilon:
                try:
                    if self.Delta[q][e] == '' or self.Delta[q][e] not in self.Q: return f"Pole {q}: {e} zawiera błąd"
                except Exception: return "Coś poszło nie tak"
        return False

    def check(self, word):
        status = self.Start
        for idsym, sym in enumerate(word):
            print(f"{idsym + 1}: {status}, {sym} -> ", end="")
            if sym not in self.Epsilon:
                print(f"\nNierozpoznany symbol w wyrazie: {sym}")
                return False
            status = self.Delta[status][sym]
            print(status)
        if status in self.Stop:
            print("Zakończono na symbolu kończącym - zatwierdzam słowo")
            return True
        else:
            print("Nie zakończono na symbolu kończącym - odrzucam słowo")
            return False

test = Automat('zad1.json')
test.check(str(input("Słowo: ")))