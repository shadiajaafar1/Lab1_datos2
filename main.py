#PUNTO 3------

#Queremos resolver una expresión aritmética usando árboles balanceados. 
#Este tipo de árboles, son particularmente útiles para resolver expresiones aritmeticas porque nos garatizan
#que las operaciones se van a realizar en el orden adecuado y siguiendo su estructura jerarquica para evitar la ambiguedad
#Además son eficientes en términos de tiempo de ejecución, ya que este es proporcional a la altura del árbol.

#En este caso resolveremos la siguiente expresión: 
#(10*2+3)/(4-15)

from funcion import *

#creamos el arbol balanceado, en los nodos estarán las operaciones y los numeros que se operarán

root = nodo("/")
root.izq = nodo("+")
root.der = nodo("-")
root.izq.izq = nodo("*")
root.izq.der = nodo(3)
root.izq.izq.izq = nodo(10)
root.izq.izq.der = nodo(2)
root.der.izq = nodo(4)
root.der.der = nodo(15)

#se calcula la solución llamando la función y se envía la raíz
sol = root.calcula_arbol(root)

#se imprime la solucion del arbol
print("La solución del árbol es: ", sol)

