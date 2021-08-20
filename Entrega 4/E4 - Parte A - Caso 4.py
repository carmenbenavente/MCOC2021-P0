from scipy import matmul, rand
from time import perf_counter
from scipy.linalg import solve, inv
from numpy import eye, float32, double, ones
import matplotlib.pylab as plt

def laplacianadb(N,dtype=double):
    e=eye(N)- eye(N,N,1)
    return dtype(e+ e.T)
def laplaciana32(N,dtype=float32):
    e=eye(N)- eye(N,N,1)
    return dtype(e+ e.T)


fid = open("rendimientoE4A4.txt","w")
Ns = [1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000] #desde 5000 hacia arriba, solve tira error, por eso lo dejo hasta ese número
dtsdb = []
dts32 = []
memsdb=[]
mems32=[]

for N in Ns:
    A = laplaciana32(N)
    B = ones(N)

    t1 = perf_counter()

    x = solve(A, B,assume_a='sym')

    t2 = perf_counter()

    uso_memoria_total = A.nbytes + B.nbytes + x.nbytes
    mems32.append(uso_memoria_total)

    dt = t2 - t1
    dts32.append(dt)

    print(f"N = {N} dt = {dt} s mem = {uso_memoria_total} bytes")

    fid.write(f" dtype = float 32 N = {N} dt = {dt} s mem = {uso_memoria_total} bytes \n")

    A = laplacianadb(N)
    B = ones(N)

    t1 = perf_counter()

    x = solve(A, B,assume_a='sym')

    t2 = perf_counter()

    uso_memoria_total = A.nbytes + B.nbytes + x.nbytes
    memsdb.append(uso_memoria_total)

    dt = t2 - t1
    dtsdb.append(dt)

    print(f"N = {N} dt = {dt} s mem = {uso_memoria_total} bytes")

    fid.write(f" dtype = double N = {N} dt = {dt} s mem = {uso_memoria_total} bytes \n")

fid.close()
plt.figure(1)
plt.subplot(2, 1, 1)
plt.loglog(Ns, dts32, '-ro', label='Float 32')
plt.loglog(Ns, dtsdb, '-bo', label='Double')
plt.xlabel('Tamaño N')
plt.ylabel('Tiempo s')
plt.title('Parte A Caso 4 Solve')
plt.legend(loc='upper left')
plt.subplot(2, 1, 2)
plt.loglog(Ns, mems32, '-ro', label='Float 32')
plt.loglog(Ns, memsdb, '-bo', label='Double')
plt.xlabel('Tamaño N')
plt.ylabel('Memoria bytes')
plt.legend(loc='upper left')
plt.savefig('GraficoE4A4.png')
plt.show()