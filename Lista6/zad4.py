from random import sample
def tobin(x):
    return tobin(x//2) + [x%2] if x>1 else [x]

# 1. a^b mod n = (a^(b0 * 2^0) mod n) * (a^(b1 * 2^1) mod n) * ... * (a^(bm * 2^m) mod n)
# 2. a^2m mod n = (a^2m-1 * a^2m-1) mod n
# 3. bit = 0 : a^(bx * 2^x) mod n = a^0 mod n = 1
def FMP(a, b, n):
    b = tobin(b)
    b.reverse()
    m = len(b)
    a %= n
    w = 1
    x = a
    for i in range(m):
        if b[i] == 1:
            w *= x
            w %= n
        x **= 2
        x %= n
    return w

def SFT(p, n):
    a = sample(range(2, p), n)
    for el in a:
        if (FMP(el, p, p) - el) % p != 0: return False
    return True

def MRT(p, n):
    s = 0
    while (p-1) % 2**s == 0: s += 1
    s -= 1
    d = int(p // 2**s)
    a = sample(range(1, p), n)
    for el in a:
        if FMP(el, d, p) != 1:
            flag = True
            for r in range(s):
                if FMP(el, (2**r)*d, p) == p-1:
                    flag = False
                    break
            if flag: return False
    return True

if __name__ == '__main__':
    p = int(input("Liczba do sprawdzenia czy pierwsza: "))
    n = int(input("Ile razy sprawdzić: "))
    print(SFT(p, n))
    print(MRT(p, n))
