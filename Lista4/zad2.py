# liczony najgorszy przypadek

def mnozenie(m1, m2):                               #O(n^3) + 2O(n^2) + 2O(n) + 3O(1) => O(n^3)
    n = len(m1)                                     #O(1)
    nm = []                                         #O(1)
    for row in range(n):                            #pętla długości n
        nrow = []                                   #n * O(1) = O(n)
        for col in range(n):                        #pętla długości n
            sum = 0                                 #n * n * O(1) = O(n^2)
            for num in range(n):                    #pętla długości n
                sum += m1[row][num] * m2[num][col]  #n * n * n * O(1) = O(n^3)
            nrow.append(sum)                        #n * n * O(1) = O(n^2)
        nm.append(nrow)                             #n * O(1) = O(n)
    return nm                                       #O(1)

if __name__ == '__main__':
    m1, m2 = [], []
    tmpm1 = input("Pierwsza macierz: ").split('|')
    for el in tmpm1: m1.append(list(map(float, el.split(','))))
    tmpm2 = input("Druga macierz: ").split('|')
    for el in tmpm2: m2.append(list(map(float, el.split(','))))

    print(m1)
    print(m2)
    print(mnozenie(m1, m2))