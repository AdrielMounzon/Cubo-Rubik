# Implementación de Solucionador de Cubo de Rubik

**Elaborado por:** Adriel David Mounzón Baspineiro

## Descripción del Proyecto

Este proyecto consiste en una implementación computacional realista de un cubo de Rubik estándar 3x3. Proporciona un algoritmo que permite resolver un cubo desarmado mediante la búsqueda del algoritmo A*. Además, facilita la introducción de comandos para desordenar el cubo mediante un archivo de texto simple que genera el cubo inicial sobre el cual se buscará la solución.

## Requerimientos del Entorno de Programación

Este proyecto utiliza Python 3.11.3. La implementación hace uso de algunas librerías incluidas con Python. El único requerimiento adicional es la instalación de la librería NumPy, que se utiliza para una representación más eficiente y sencilla del cubo de Rubik.
Puede instalarse con el comando: `pip install numpy`

## Manual de Uso

El primer paso al iniciar el proyecto es modificar el archivo `/textos/comandos.txt`, donde se pueden incluir una lista de movimientos que se ejecutarán sobre un cubo inicial armado y se guardarán automáticamente para su ejecución. Estos comandos utilizan la notación Singmaster, excluyendo movimientos de capas centrales. También se reemplazan los valores prima ' con la letra 'p' para una mejor claridad visual. Los movimientos duplicados, como 'R2', deben descomponerse e introducirse 2 veces.
Aquí está la lista completa de los movimientos permitidos: `['U', 'Up', 'D', 'Dp', 'L', 'Lp', 'R', 'Rp', 'F', 'Fp', 'B', 'Bp']`

No es necesario introducir manualmente los datos, ya que con los comandos se genera automáticamente el cubo resultante. Sin embargo, es posible crear un cubo a partir de un archivo de texto directamente, comentando todo el contenido activo de `carga.py` y descomentando la parte comentada.

## Diseño e Implementación

Para la solución del cubo de Rubik se utilizó un algoritmo de búsqueda A* basado en una heurística que calcula la cantidad de piezas en todo el cubo que no están en la cara que corresponden, siendo 0 un sinónimo de que el cubo está desarmado. Esta búsqueda siempre toma el camino con la menor heurística posible.

Se eligió esta búsqueda debido a su eficiencia en combinación con una buena heurística. En comparación con algoritmos de búsqueda ciega probados como el BFS, se observa una gran ventaja. El algoritmo BFS devolvía la solución a un cubo desordenado con 4 movimientos en cerca de 1 minuto, mientras que la búsqueda implementada actualmente devuelve los mismos 4 movimientos en menos de un segundo.

La decisión de la heurística se da bajo la lógica de que mientras más elementos estén en la cara que corresponde, más cerca estaremos de la solución. Esta heurística, en comparación con la distancia a su posición, elimina la complejidad de buscar la posición de una pieza en toda la cara basada en los otros colores. Además, permite que aunque un cubito no esté en su posición exacta, pero sí en la cara correcta, se ordenará todo con los movimientos de las otras capas.

Para este proyecto se usó un modelo de generación de texto: Chat GPT. Este modelo colaboró mínimamente en el código, sin embargo, fue usado para generar ideas que luego fueron corregidas y complementadas para usar en este proyecto. El único prompt relevante fue "¿Qué algoritmos de búsqueda son eficientes para resolver una representación de cubo de Rubik?".

## Trabajo Futuro

Este algoritmo es muy eficiente, logrando resolver hasta 16 movimientos en aproximadamente un minuto (casi 185,000 billones de posibilidades). Por lo tanto, se recomienda mantenerlo e implementar posibles optimizaciones sobre este. La heurística permite acercarse a una solución, sin embargo, no garantiza que el camino recorrido sea el óptimo. Se recomienda profundizar en la búsqueda de patrones en la solución óptima de los cubos propuestos por otros simuladores para poder intercambiar la heurística actual por una nueva.