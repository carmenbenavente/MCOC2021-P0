from numpy import zeros
from time import perf_counter

#Tamaño
N = 100
A = zeros((N,N))+1
B = zeros((N,N))+2

#print(f"A = {A}")
#print(f"B = {B}")

t1 = perf_counter()

C = A@B   #multiplicación de matrices

t2 = perf_counter()

dt = t2-t1

print(f"C = {C}")

print(dt)
