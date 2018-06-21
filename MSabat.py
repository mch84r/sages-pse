import numpy as np
import random


print("Hello")


def matrix_multiplication(A, B):
    C=A@B
    print(C)
    return (C)



A =np.array([[1, 0], [0, 1]])
B =np.array([[4, 1], [2, 2]])
matrix_multiplication(A, B)



drug=np.random.randint(10,size=(16,16))


print("Druga macierz: ", drug)


drug4=drug[6:10,6:10]

print('-'*50)

print("Druga macierz: ", drug4)
print(drug4.flatten())
print(sum(drug4.flatten()))

