from numpy import zeros, float16, float32, float64
from time import perf_counter
from scipy import rand
import matplotlib.pylab as plt

fid = open("rendimiento.txt", "w")

N = 1000
Ns = [10, 100, 1000, 2000]
dts =[]
mems=[]
for N in Ns:

    A = zeros((N,N), dtype=float32) +1
    B = zeros((N, N)) + 2

    t1 = perf_counter()

    C = A @ B

    t2 = perf_counter()

    uso_memoria_total = A.nbytes + B.nbytes + C.nbytes
    mems.append(uso_memoria_total)

    dt = t2 - t1
    dts.append(dt)

    print(f"N = {N} dt = {dt} s mem = {uso_memoria_total} bytes")

    fid.write(f"{N} {dt} {uso_memoria_total} \n")

fid.close()
plt.figure(1)
plt.subplot(2,1,1)
plt.loglog(Ns,dts)
plt.subplot(2,1,2)
plt.loglog(Ns, mems)
plt.show()


# código del enunciado

# A = rand(N,N)
# B = rand(N,N)

