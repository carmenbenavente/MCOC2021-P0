import numpy as np
from time import perf_counter
from numpy import eye, double
import matplotlib.pylab as plt

def matriz_laplaciana(N, t=np.double):
    e = np.eye(N) - np.eye(N, N, 1)
    return t(e + e.T)

fid = open("rendimientoE5Completas.txt","w")
Ns = [1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000] #no entiendo como ver hasta donde tengo que correrlo, asiq ue lo deje así nomas

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
plt.title('E5 Matrices Completas')
plt.subplot(2,1,2)
for i in range(10):
    plt.loglog(Ns,solucion[i], '-ko')
plt.xlabel('Tamaño N')
plt.ylabel('Tiempo Solución s')
plt.savefig('GraficoE5Completas.png')
plt.show()



