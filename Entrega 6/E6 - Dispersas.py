import numpy as np
import scipy.sparse as sp
import scipy.sparse.linalg as lin
from time import perf_counter
from numpy import double, ones
from scipy.linalg import inv
import matplotlib.pylab as plt

def matriz_laplaciana(N, t):
    return sp.eye(N, dtype=t) - sp.eye(N,N,1,dtype=t)



fid = open("rendimientoSOLVEE6Dispersas.txt","w")
fid1 = open("rendimientoINVE6Dispersas.txt","w")
Ns = [1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000] #no entiendo como ver hasta donde tengo que correrlo, asiq ue lo deje así nomas

ensambladoS = []
solucionS = []

ensambladoI = []
solucionI = []

for i in range(10):
    dtensambladoS = []
    dtsolucionS = []

    dtensambladoI = []
    dtsolucionI = []
    for N in Ns:
        t0 = perf_counter()

        Lp = matriz_laplaciana(N,double)
        A = sp.csr_matrix(Lp)
        B = ones(N)

        t1 = perf_counter()

        x = lin.spsolve(A,B)

        t2 = perf_counter()

        densamblado = t1 - t0

        dsolucion = t2 - t1
        dtensambladoS.append(densamblado)
        dtsolucionS.append(dsolucion)

        print(f"N = {N} tiempo ensamblado = {densamblado} s tiempo solucion = {dsolucion}")

        fid.write(f"N = {N} tiempo ensamblado = {densamblado} s tiempo solucion = {dsolucion} \n")

        ensambladoS.append(dtensambladoS)
        solucionS.append(dtsolucionS)

        t0 = perf_counter()

        Lp = matriz_laplaciana(N, double)
        A = sp.csc_matrix(Lp)

        t1 = perf_counter()

        x = lin.inv(A)

        t2 = perf_counter()

        densamblado = t1 - t0

        dsolucion = t2 - t1
        dtensambladoI.append(densamblado)
        dtsolucionI.append(dsolucion)

        print(f"N = {N} tiempo ensamblado = {densamblado} s tiempo solucion = {dsolucion}")

        fid1.write(f"N = {N} tiempo ensamblado = {densamblado} s tiempo solucion = {dsolucion} \n")

        ensambladoI.append(dtensambladoI)
        solucionI.append(dtsolucionI)


fid.close()
fid1.close()
plt.figure(1)
plt.subplot(2,1,1)
for i in range(10):
    plt.loglog(Ns,ensambladoS[i], '-ko', alpha=0.1)
plt.xlabel('Tamaño N')
plt.ylabel('Tiempo Ensamblado s')
plt.title('E6 Matrices Dispersas Solve')
plt.subplot(2,1,2)
for i in range(10):
    plt.loglog(Ns,solucionS[i], '-ko', alpha=0.1)
plt.xlabel('Tamaño N')
plt.ylabel('Tiempo Solución s')
plt.savefig('GraficoE6DispersasSolve.png')
plt.show()

plt.figure(2)
plt.subplot(2,1,1)
for i in range(10):
    plt.loglog(Ns,ensambladoI[i], '-ko', alpha=0.1)
plt.xlabel('Tamaño N')
plt.ylabel('Tiempo Ensamblado s')
plt.title('E6 Matrices Dispersas Inv')
plt.subplot(2,1,2)
for i in range(10):
    plt.loglog(Ns,solucionI[i], '-ko', alpha=0.1)
plt.xlabel('Tamaño N')
plt.ylabel('Tiempo Solución s')
plt.savefig('GraficoE6DispersasInv.png')
plt.show()
