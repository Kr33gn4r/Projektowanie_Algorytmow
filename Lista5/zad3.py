def margesort(tab, p, r):
    if p >= r: return
    q = (p+r)//2
    margesort(tab, p, q)
    margesort(tab, q+1, r)
    marge(tab, p, q, r)

def marge(tab, p, q, r):
    t1 = tab[p:q+1]
    t2 = tab[q+1:r+1]
    i, j, k = 0, 0, p

    while i < len(t1) and j < len(t2):
        if t1[i] <= t2[j]:
            tab[k] = t1[i]
            i += 1
        else:
            tab[k] = t2[j]
            j += 1
        k += 1

    while i < len(t1):
        tab[k] = t1[i]
        i += 1
        k += 1
    while j < len(t2):
        tab[k] = t2[j]
        j += 1
        k += 1

if __name__ == '__main__':
    tab = list(map(int, input("Podaj listę: ").split(',')))
    #tab = [5,1,3,9,10,3,9,1,90,32,13,4,5]
    margesort(tab, 0, len(tab)-1)
    print(tab)