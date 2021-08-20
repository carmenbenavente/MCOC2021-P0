from scipy import matmul, rand
from time import perf_counter
from scipy.linalg import inv, eigh
from numpy import eye, float32, double, ones
import matplotlib.pylab as plt

def laplacianadb(N,dtype=double):
    e=eye(N)- eye(N,N,1)
    return dtype(e+ e.T)
def laplaciana32(N,dtype=float32):
    e=eye(N)- eye(N,N,1)
    return dtype(e+ e.T)


fid = open("rendimientoE4B1.txt","w")
Ns = [1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000] #desde 5000 hacia arriba, se demora mucho en correr, por eso lo dejo hasta ese número
dtsdb = []
dts32 = []

for N in Ns:
    A = laplaciana32(N)

    t1 = perf_counter()

    w,h = eigh(A)

    t2 = perf_counter()

    dt = t2 - t1
    dts32.append(dt)

    print(f"Eigh: N = {N} dt = {dt} s ")

    fid.write(f" dtype = float 32 {N} {dt} \n")

    A = laplacianadb(N)
    B = ones(N)

    t1 = perf_counter()

    w,h = eigh(A)

    t2 = perf_counter()

    dt = t2 - t1
    dtsdb.append(dt)

    print(f"Eigh: N = {N} dt = {dt} s ")

    fid.write(f" dtype = double {N} {dt} \n")

fid.close()
plt.figure(1)
plt.loglog(Ns,dts32, '-ro', label='Float 32')
plt.loglog(Ns,dtsdb, '-bo', label='Double')
plt.xlabel('Tamaño N')
plt.ylabel('Tiempo s')
plt.title('Parte B Caso 1 Eigh')
plt.legend(loc='upper left')
plt.show()
