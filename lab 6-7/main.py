import numpy as np
from math import pi
from numpy import dot


# add two vectors
def add(A, B):
    result = []
    if len(A) == len(B):
        for i in range(len(A)):
            result.append(A[i] + B[i])
    return result


# subtract two vectors
def subtr(A, B):
    result = []
    if len(A) == len(B):
        for i in range(len(A)):
            temp=A[i] - B[i]
            result.append(temp)
    return result


def multi(A, B):
    result = []
    for i in range(len(A)):
        total = 0
        for j in range(len(B)):
            total += A[i, j] * B[j]
        result.append(total)
    return result


def gaussElimin(A, B, N, X):
    # Elimination Phase
    for k in range(0, N - 1):
        for i in range(k + 1, N):
            if A[i, k] == 0:
                continue
            var = A[k, k] / A[i, k]
            for j in range(k,N):
                A[i,j]=A[k,j]-A[i,j]*var
            B[i] = B[k] - B[i]*var
    print("\nUpper triangle A and vector b")
    for i in range(my_A_rows):
        print(np.round(A[i],2), np.round(B[i],2))

    # Back substitution
    X[N-1]=B[N-1]/A[N-1,N-1]
    for i in range(N - 1, -1, -1):
        sum_ax=0
        for j in range(i+1, N):
            sum_ax+=A[i,j]*X[j]
        X[i]=(B[i]-sum_ax)/A[i,i]
    print("\nSolution vector")
    for i in range (my_A_rows):
        print(f"x{[i]} = {np.round(X[i],2)}")
    return X

print("--------------")
print('For now, please convert pi before input')
print("---------------")
my_A_rows = int(input("введите число строк матрицы коэфициентов: "))

print("введите матрицу коэфициентов (по строках, пробелы между коэффициентами")
myA = [list(map(float, (input(f"строка {i + 1}: ").split())))
       for i in range(my_A_rows)]


myB = map(float, input("Введите матрицу правых частей, пробелы между числами: ").split())
myB = list(myB)

x_val= np.zeros(len(myB), float)
A = np.array(myA)
B = np.array(myB)


print("\nMatrix A and vector b")
for i in range (my_A_rows):
    print(A[i], B[i])
gauss_x = gaussElimin(A, B, my_A_rows, x_val)
mm = multi(np.array(myA),gauss_x)
delta = subtr(mm,np.array(myB))
print(f"\ndelta = {delta}")
