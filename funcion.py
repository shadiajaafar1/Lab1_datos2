class nodo: #constructor del nodo
    def __init__(self, data): #cada nodo como atributos tiene la data, puede ser un numero o una operacion, izquierda y derecha
        self.data = data
        self.izq = None
        self.der = None
        
    #esta función que se encarga de resolver las operaciones del arbol
    def calcula_arbol(self, root): 
        if (root is None): #primero verifica que el arbol no esté vacío, si lo está el resultado es 0
            return 0

        if (root.izq is None and root.der is None): #ahora, se verifica que la raiz tenga hijos, sino no es así el resultado es el valor de la raiz
            return int(root.data)
        
        #dado que ya descartamos los casos triviales, quiere decir que hay subarboles, llamamos 
        #a la funcion de forma recursiva
        
        #iniciamos revisando el subarbol izquierdo, calculando de abajo hacia arriba
        subarbol_izquierdo = self.calcula_arbol(root.izq)
        #al terminar de revisar el subarbol izquierdo, vamos por el derecho
        subarbol_derecho = self.calcula_arbol(root.der)
        
        #validamos el tipo de operacion de los nodos
        if(root.data=="*"): #si el nodo tiene de operacion la multiplicacion
            op = subarbol_izquierdo*subarbol_derecho #se multiplican los nodos izquierdo y derecho y se guarda en op
            return op
        elif (root.data == "+"): #si el nodo tiene la suma, se suman los subarboles
            op = subarbol_izquierdo + subarbol_derecho
            return op
        elif(root.data == "-"): #de la misma forma para la resta. Hay que tener en cuenta que el orden de operacion es izquierdo menos derecho
            op = subarbol_izquierdo-subarbol_derecho
            return op
        else:
            op = subarbol_izquierdo/subarbol_derecho #similar para la división
            return op
    


        

        
        