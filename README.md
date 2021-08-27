# MCOC2021-P0

En esta entrega se nota una clara diferencia entre las matrices que estan completas y las que son dispersas. Para comenzar, el rango de valores que utilicé para las matrices completas es de máximo 5.000 mientras que en las dispersas es de 5.000.000 y aún así se demora menos el código de las dispersas. A lo largo de toda la entrega 0 no logré entender bien que era lo que nos pedían cuando decían el llevar al máximo el computador, por eso inventaba valores que se demoraran en total en correr aproximadamente unos 2 minutos y ahí lo dejaba. En términos de código, la diferencia es más que nada que en el caso de las dispersas utilicé la libreria sparce de scipy mas que numpy. A continuación presento los códigos y gráficos de cada una de las partes.

```
import numpy as np
def matriz_laplaciana(N, t=np.double):
    e = np.eye(N) - np.eye(N, N, 1)
    return t(e + e.T)
```
![GraficoE5Completas](https://user-images.githubusercontent.com/62263342/131179992-fc22f76c-387e-4dc9-85f7-3e295a8ce925.png)


```
import scipy.sparse as sparce
def matriz_laplaciana(N, t=np.double):
    return sparce.eye(N, dtype=t) - sparce.eye(N,N,1,dtype=t)
```

![GraficoE5Dispersas](https://user-images.githubusercontent.com/62263342/131179542-47349905-9020-4333-8032-886c79fcc709.png)
