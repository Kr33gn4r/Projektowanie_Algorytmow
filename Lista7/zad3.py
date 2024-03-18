import numpy as np
from zad2 import FFT, IFFT

def FFT_polynomial_multiplication(p1 : list, p2 : list):
    P1 = np.concatenate([p1, [0 for _ in range(len(p2) - 1)]])
    P2 = np.concatenate([p2, [0 for _ in range(len(p1) - 1)]])

    f1 = FFT(P1)
    f2 = FFT(P2)

    C = [f1[i] * f2[i] for i in range(len(f1))]
    # ifft(x) = 1/n * sprzężenie(FFT(sprzężenie(X)))
    ifft = IFFT(C)
    return np.trim_zeros([int(np.round(_)) for _ in ifft])

if __name__ == '__main__':
    w1 = [1, 0, 3, 1, 2, 9, 11]       #od najmniejszego
    w2 = [13, 3, 1, 0, 3, 2, 11, 11]  #od najmniejszego

    print(FFT_polynomial_multiplication(w1, w2))