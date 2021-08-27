import numpy as np
import scipy.sparse as sparce
from time import perf_counter
from numpy import eye, double
import matplotlib.pylab as plt

def matriz_laplaciana(N, t=np.double):
    return sparce.eye(N, dtype=t) - sparce.eye(N,N,1,dtype=t)



fid = open("rendimientoE5Dispersas.txt","w")
Ns = [1000000, 1500000, 2000000, 2500000, 3000000, 3500000, 4000000, 4500000, 5000000] #no entiendo como ver hasta donde tengo que correrlo, asiq ue lo deje así nomas

ensamblado = []
solucion = []

for i in range(10):
    dtensamblado = []
    dtsolucion = []
    for N in Ns:
        t0 = perf_counter()

        A = matriz_laplaciana(N)
        B = matriz_laplaciana(N)

        t1 = perf_counter()

        x = A@B

        t2 = perf_counter()

        densamblado = t1 - t0

        dsolucion = t2 - t1
        dtensamblado.append(densamblado)
        dtsolucion.append(dsolucion)

        print(f"N = {N} tiempo ensamblado = {densamblado} s tiempo solucion = {dsolucion}")

        fid.write(f"N = {N} tiempo ensamblado = {densamblado} s tiempo solucion = {dsolucion} \n")

        ensamblado.append(dtensamblado)
        solucion.append(dtsolucion)


fid.close()
plt.figure(1)
plt.subplot(2,1,1)
for i in range(10):
    plt.loglog(Ns,ensamblado[i], '-ko')
plt.xlabel('Tamaño N')
plt.ylabel('Tiempo Ensamblado s')
plt.title('E5 Matrices Dispersas')
plt.subplot(2,1,2)
for i in range(10):
    plt.loglog(Ns,solucion[i], '-ko')
plt.xlabel('Tamaño N')
plt.ylabel('Tiempo Solución s')
plt.savefig('GraficoE5Dispersas.png')
plt.show()



