# element -> liczba może się powtórzyć
# liczony najgorszy przypadek

def najwiekszy(lista):      #2O(n) + 2O(1) => O(n)
    a = -9999               #O(1)
    for el in lista:        #pętla długości n
        if el > a:          #n * O(1) = O(n)
            a = el          #n * O(1) = O(n)
    return a                #O(1)

def druginajwiekszy(lista): #5O(n) + 4O(1) => O(n)
    a = -9999               #O(1)
    b = -9999               #O(1)
    for el in lista:        #pętla długości n
        if el > a:          #n * O(1) = O(n)
            b = a           #n * O(1) = O(n)
            a = el          #n * O(1) = O(n)
        elif el > b:        #n * O(1) = O(n)
            b = el          #n * O(1) = O(n)
    return b                #O(1)

def srednia(lista):         #2O(n) + 3O(1) => O(n)
    am = 0                  #O(1)
    su = 0                  #O(1)
    for el in lista:        #pętla długości n
        su += el            #n * O(1)
        am += 1             #n * O(1)
    return su / am          #O(1)

if __name__ == '__main__':
    lista = list(map(float, input("Podaj listę: ").split(',')))
    print(najwiekszy(lista), druginajwiekszy(lista), srednia(lista))