import sys

sys.setrecursionlimit(100000)

def start_najwiekszy(tab):
    return najwiekszy(tab, 0, len(tab)-1, 0)

def start_druginajwiekszy(tab):
    return druginajwiekszy(tab, 0, len(tab)-1, 0, 0)[1]

def start_srednia(tab):
    return srednia(tab, 0, len(tab)-1, 0, 0)[0]

def najwiekszy(tab, p, r, m):
    if p >= r: return tab[r]
    q = (p+r)//2
    m1 = najwiekszy(tab, p, q, m)
    m2 = najwiekszy(tab, q+1, r, m)
    return m1 if m1 > m2 else m2

def druginajwiekszy(tab, p, r, m1, m2):
    if r - p == 1:
        if tab[p] > tab[r]: return tab[p], tab[r]
        else: return tab[r], tab[p]
    elif r - p <= 0: return tab[r], None
    q = (p+r)//2
    b1, sb1 = druginajwiekszy(tab, p, q, m1, m2)
    b2, sb2 = druginajwiekszy(tab, q+1, r, m1, m2)
    if b1 > b2:
        b = b1
        sb = b2
    else:
        b = b2
        sb = b1
    if sb1 != None:
        if sb1 > sb: sb = sb1
    if sb2 != None:
        if sb2 > sb: sb = sb2
    return b, sb

def srednia(tab, p, r, avg, n):
    if p >= r: return tab[r], 1
    q = (p+r)//2
    avg1, n1 = srednia(tab, p, q, avg, n)
    avg2, n2 = srednia(tab, q+1, r, avg, n)
    return (n1 * avg1 + n2 * avg2) / (n1 + n2), (n1 + n2)

if __name__ == '__main__':
    # tab = [11, 1, 4, 3, 1, 13, 9, 1, 3, 2, 10, 9]
    tab = list(map(int, input("Podaj listę: ").split(',')))
    print(start_najwiekszy(tab))
    print(start_druginajwiekszy(tab))
    print(start_srednia(tab))
