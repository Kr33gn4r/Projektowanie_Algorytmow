from zad2 import sito
from zad3 import ENWD
from zad4 import FMP
from itertools import compress
from random import randint

class RSA:
    def __init__(self, p, q):
        self.n = p*q
        phi = (p-1) * (q-1)

        f = False
        while not f:
            e = randint(1, phi)
            if ENWD(e, phi) == 1: f = True
        self.e = e
        self.d = self.ext_euclid_modular(self.e, phi)

    def ext_euclid_modular(self, a, n):
        # at = 1 (mod n) -> de = 1 (mod phi)
        t, new_t, r, new_r = 0, 1, n, a
        while new_r != 0:
            q = r // new_r
            (t, new_t) = (new_t, t - q * new_t)
            (r, new_r) = (new_r, r - q * new_r)

        if r > 1: return False
        if t < 0: t += n
        return t

    def encode(self, message):
        m_array = bytearray(message.encode('ascii'))
        blocks, b, t = [], 0, 0
        for elem in m_array:
            if b == 0:
                b = int(elem)
                continue
            t = b * 1000 + int(elem)
            if t > self.n:
                blocks.append(b)
                b = int(elem)
                t = 0
            else:
                b = t
        blocks.append(b)

        c = []
        for block in blocks:
            c.append(FMP(block, self.e, self.n))
        return c

    def decode(self, encoded_blocks):
        blocks = []
        for en in encoded_blocks:
            blocks.append(FMP(en, self.d, self.n))

        message = ''
        for block in blocks:
            s = ''
            while block != 0:
                m = block % 1000
                s += chr(m)
                block = (block - m) // 1000
            message += s[::-1]
        return message

wynik = sito(10000000)
pierwsze = list(compress(range(len(wynik)), wynik))
p, q = 1, 1
while p == q: p, q = pierwsze[randint(1000, len(pierwsze))], pierwsze[randint(1000, len(pierwsze))]

rsa = RSA(p, q)
teksty = ['test', 'chyba dziala', '1a2b3DP\tJSA??\n1FSAd!#@%^  d', 'niestety dziala to tylko w ascii smutek ale przynajmniej dziala :)']

for tekst in teksty:
    print(f"Tekst: {tekst}")
    e = rsa.encode(tekst)
    print(f"Zakodowana wiadomość: {''.join(map(str, e))}")
    d = rsa.decode(e)
    print(f"Odkodowana wiadomość: {d}")
    print()
