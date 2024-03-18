# liczony najgorszy przypadek

def graycode(lista): #8O(2^n) + O(n) + 8O(1) => O(2^(n+3))
    n = len(lista)                                              #O(1)
    lista_mozliwosci = []                                       #O(1)
    tf = [False for i in range(n)]                              #n * O(1) = O(n)
    log2dict = {2**i:n-i-1 for i in range(n)}                   #n * O(1) = O(n)
    sum = 0                                                     #O(1)
    for i in range(0, (1<<n)-1):                                #pętla długości 2^n
        xor = i^(i>>1) ^ (i+1)^((i+1)>>1)                       #2^n * O(1) = O(2^n)
        pos = log2dict[xor]                                     #2^n * O(1) = O(2^n)

        sum -= lista[pos] if tf[pos] else -lista[pos]           #2 * 2^n * O(1) = 2O(2^n)
        tf[pos] != tf[pos]                                      #2^n * O(1) = O(2^n)

        if sum == 0:                                            #2^n * O(1) = O(2^n)
            lista_mozliwosci.append(tf.copy())                  #2^n * O(1) = O(2^n)

    try:                                                        #O(1)
        lista_mozliwosci[0]                                     #O(1)
        return True                                             #O(1)
    except IndexError:                                          #O(1)
        return False                                            #O(1)

if __name__ == '__main__':
    lista = list(map(int, input("Podaj listę: ").split(',')))
    print(graycode(lista))