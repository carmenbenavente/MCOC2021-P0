# MCOC2021-P0
Comente las diferencias que ve en el comportamiento de los algoritmos en el caso de matrices llenas y dispersas.
¿Cual parece la complejidad asintótica (para N→∞)  para el ensamblado y solución en ambos casos y porqué?
¿Como afecta el tamaño de las matrices al comportamiento aparente?
¿Qué tan estables son las corridas (se parecen todas entre si siempre, nunca, en un rango)?

A continuación muestro los gráficos para cada caso:

![GraficoE6CompletasInv](https://user-images.githubusercontent.com/62263342/132064933-e90bf0ea-48f8-4105-81af-ae09c441a384.png)
![GraficoE6CompletasSolve](https://user-images.githubusercontent.com/62263342/132064927-aef41120-3a09-41be-8760-54f1e1316b42.png)
![GraficoE6DispersasInv](https://user-images.githubusercontent.com/62263342/132064929-13e4ee43-77ac-4c78-9fc4-e172d4c35c3a.png)
![GraficoE6DispersasSolve](https://user-images.githubusercontent.com/62263342/132064932-9bd28715-de12-4472-9634-75002be5ba4e.png)

La mayor diferencia que se puede ver en el caso de matrices llenas y dispersas es el timepo de ensamblado de las matrices. En términos de tiempo en el caso de las soluciones no es tán notoria la diferencia pero se ve que en el caso de las matrices dispersas existe una tendencia lineal menor que en las completas.

La mayor complejidad es que en todos los caso, mientras más grande sea el valor de N, mayor es el tiempo de ejecución y de ensamblaje. Esto significa que al tener un N tendiendo a infinito, puede generar que el programa colapse por un tema de espera del programa. En el caso de Solve, es mayor el tiempo utilizado que en el caso de INV.

EL comportamiento aparente por lo general es menos estable con N más pequeños que en caso de los N más grandes. Esto se puede ver por lo difuminada que se ve la linea en un comienzo comparado con el final.

Las corridas las llamariá más estables que inestables. En el caso de las matrices dispersas con la función Solve es donde menos parecidas son las corridas, mientras que para el caso de las matrices completas con la funcion INV son las más parecidas las corridas comparando las cuatro.
