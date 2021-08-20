from time import perf_counter
from numpy import zeros
from numpy import float16, float32, float64
from scipy.linalg import inv
from laplaciana import laplaciana

N = 2500

t1 = perf_counter()
A = laplaciana(N, dtype=float32)
t2 = perf_counter()
#print(A)
Am1 = inv(A)

t3 = perf_counter()

dt_ensamblaje = t2 - t1
dt_inversion = t3 - t2

bytes_total = A.nbytes + Am1.nbytes

print(f"Uso memoria: {bytes_total} bytes")
print(f"Tiempo ensamblaje: {dt_ensamblaje} s")
print(f"Tiempo inversión: {dt_inversion} s")

