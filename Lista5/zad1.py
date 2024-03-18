from math import ceil, sqrt
import sys

sys.setrecursionlimit(100000)

def ciagpierwszy(n, x=1, iter=1):
    if n == 0: return x
    if n != iter: return ciagpierwszy(n, 3**iter + x, iter+1)
    else: return 3**iter + x

def ciagdrugi(n, x1=0, x2=0, iter=1):
    if n == 0: return x2
    if n != iter:
        x = iter + x1
        return ciagdrugi(n, x2, x, iter+1)
    else: return iter + x1

def fibonacci(n, x1=0, x2=1, iter=2):
    if n == 0: return x1
    elif n == 1: return x2
    if n != iter:
        x = x1 + x2
        return fibonacci(n, x2, x, iter+1)
    else: return x1+x2

def wzorciagpierwszy(n):
    sum = 0
    for i in range(n+1):
        sum += 3**i
    return sum

def wzorciagdrugi(n):
    sum = 0
    for i in range(n+1):
        sum += ceil(i/2)
    return sum

def wzorfibonacci(n):
    return 1/sqrt(5) * ((1 + sqrt(5))/2)**n - 1/sqrt(5) * ((1 - sqrt(5))/2)**n

def roznice(n):
    pier, drug, fib = [], [], []
    for i in range(n+1):
        pier.append(ciagpierwszy(i) - wzorciagpierwszy(i))
        drug.append(ciagdrugi(i) - wzorciagdrugi(i))
        fib.append(fibonacci(i) - wzorfibonacci(i))
    print(f"Różnice pierwszych {n} elementów od 0 dla: ")
    print(f"Ciągu pierwszego: {pier}")
    print(f"Ciągu drugiego: {drug}")
    print(f"Ciągu fibonacciego: {fib}")

n = int(input("n: "))
roznice(n)