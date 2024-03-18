import numpy as np
from matplotlib import pyplot as plt

def FFT(x : np.ndarray):
    l = len(x)
    if (l & (l-1) != 0) or l == 0:
        bl = len(bin(l)) - 2
        x = np.append(x,[0 for i in range(l, 2**bl)])
    return Cooley_Tukey(x)

def IFFT(x : np.ndarray):
    return (1 / len(x)) * np.conj(FFT(np.conj(x)))
def Cooley_Tukey(x : np.ndarray):
    N = len(x)

    if N == 1: return x
    else:
        X_even = Cooley_Tukey(x[::2])
        X_odd = Cooley_Tukey(x[1::2])
        f = np.exp(-2j * np.pi * np.arange(N) / N)

        X = np.concatenate([X_even + f[:int(N/2)] * X_odd,\
                           X_even + f[int(N/2):] * X_odd])
        return X

if __name__ == '__main__':
    sr = 128
    ts = 1.0/sr
    t = np.arange(0, 1, ts)
    x = 3 * np.sin(2 * np.pi * t)
    x += np.sin(8 * np.pi * t)
    x += 0.5 * np.sin(14 * np.pi * t)

    X = FFT(x)
    N = len(X)
    n = np.arange(N)
    T = N/sr
    freq = n/T
    print(abs(X))
    fig, ax = plt.subplots(1, 3)
    ax[0].plot(t, x)
    ax[0].set_xlabel('Time (s)')
    ax[0].set_ylabel('Function Value')
    ax[1].stem(freq, abs(X), 'b', markerfmt="", basefmt="-b")
    ax[1].set_xlabel('Frequency (Hz)')
    ax[1].set_ylabel('FFT Amplitude Value')

    xfft = np.fft.fft(x)
    ax[2].stem(freq, abs(xfft), 'b', markerfmt="", basefmt="-b")
    ax[2].set_xlabel('Frequency (Hz)')
    ax[2].set_ylabel('FFT Amplitude Value')

    plt.show()