import numpy as np

def naive_polynomial_multiplication(p1 : list, p2 : list):
    if (len(p1) != len(p2)):
        for _ in range(len(p1), len(p2)): p1.append(0)
        for _ in range(len(p2), len(p1)): p2.append(0)
    n = len(p1)
    pmultiplied = [0 for _ in range(2*n)]

    for i, val in enumerate(p1):
        for j, mul in enumerate(p2):
            k, m = i + j, val * mul
            pmultiplied[k] += m
    return np.trim_zeros(pmultiplied)

if __name__ == '__main__':
    w1 = [1, 0, 3, 1, 2, 9, 11]     #od najmniejszego
    w2 = [13, 3, 1, 0, 3, 2, 11, 11]#od najmniejszego

    print(naive_polynomial_multiplication(w1, w2))