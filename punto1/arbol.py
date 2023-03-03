import csv

class TreeNode:
    def __init__(self, value = None):
        self.value = value
        self.parent = None
        self.children = []
        self.left_child = None
        self.right_child = None
        self.left = None
        self.right = None
        self.height = 1


    def insert(self, value):
        if self.value is None:
            self.value = value
        elif value < self.value:
            if self.left is None:
                self.left = TreeNode(value)
                self.left.parent = self  
            else:
                self.left.insert(value)
        elif value > self.value:
            if self.right is None:
                self.right = TreeNode(value)
                self.right.parent = self  
            else:
                self.right.insert(value)
    
    # inserta un nuevo valor en el árbol. Si el valor ya existe, no hace nada.


    def delete(self, value):
        if value < self.value:
            if self.left:
                self.left = self.left.delete(value)
        elif value > self.value:
            if self.right:
                self.right = self.right.delete(value)
        else:
            if not self.left:
                return self.right
            elif not self.right:
                return self.left
            else:
                min_node = self.right.get_min()
                self.value = min_node.value
                self.right = self.right.delete(min_node.value)
        if not self:
            return None
        self.height = 1 + max(self.left.get_height() if self.left else 0, self.right.get_height() if self.right else 0)
        balance = self.get_balance()
        if balance > 1:
            if self.left.get_balance() < 0:
                self.left = self.left.rotate_left()
            return self.rotate_right()
        elif balance < -1:
            if self.right.get_balance() > 0:
                self.right = self.right.rotate_right()
            return self.rotate_left()
        return self

    # elimina un valor del árbol. Si el valor no existe, no hace nada.
    

    def search(self, value):
        if value is None:
            return None
        elif value == self.value:
            return self
        elif value < self.value and self.left is not None:
            return self.left.search(value)
        elif value > self.value and self.right is not None:
            return self.right.search(value)
        else:
            return None
    
    # busca un valor en el árbol y devuelve el nodo que lo contiene, o None si no se encuentra.

    def get_min(self):
        current = self
        while current.left is not None:
            current = current.left
        return current

    

    def get_height(self):
        
        if self.left is None and self.right is None:
            return 1
        elif self.left is None:
            return 1 + self.right.get_height()
        elif self.right is None:
            return 1 + self.left.get_height()
        else:
            return 1 + max(self.left.get_height(), self.right.get_height())
            
    

    def get_balance(self):
         return self.left.get_height() - self.right.get_height() if self and self.left and self.right else 0

    def left_rotate(self):
        new_root = self.right
        self.right = new_root.left
        new_root.left = self

        self.height = 1 + max(self.get_height(self.left), self.get_height(self.right))
        new_root.height = 1 + max(self.get_height(new_root.left), self.get_height(new_root.right))

        return new_root


    def right_rotate(self):
        if self.left is None:
            return self
        
        new_root = self.left
        self.left = new_root.right
        new_root.right = self

        self.height = 1 + max(self.get_height(self.left), self.get_height(self.right))

        return new_root



    def tour_in_order_by_level(self):
        queue = []
        queue.append(self)
        while len(queue) > 0:
            node = queue.pop(0)
            print(node.value, end=" ")
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)

    #  recorre el árbol en orden de nivel y para cada nodo imprime su valor.

    def get_grandpa(self, value=None):
        if self.parent is None:
            return None
        elif self.parent.parent is None:
            return None
        elif value is None:
            return self.parent.parent
        elif self.parent.parent.value == value:
            return self.parent.parent
        else:
            return self.parent.get_grandpa(value)

    # devuelve el abuelo del nodo actual, o None si no tiene abuelo o si el valor dado no coincide con el valor del abuelo.

    def get_uncle(self):
        if self.parent is None or self.parent.parent is None:
            return None
        grandparent = self.parent.parent
        if grandparent.left == self.parent:
            return grandparent.right if grandparent.right is not None else None
        else:
            return grandparent.left if grandparent.left is not None else None

    # devuelve el tío del nodo actual, o None si no tiene tío.

    def print_level_order(self):
        if self is None:
            return
        queue = []
        queue.append(self)
        while(len(queue) > 0):
            print(queue[0].value,end=" ")
            node = queue.pop(0)
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)

    # imprime los nodos del árbol en orden de nivel.

    def read_user_ids_from_csv(cls, filename):
        with open(filename) as csv_file:
            csv_reader = csv.reader(csv_file)
            root = TreeNode() 
            for i, row in enumerate(csv_reader):
                if i == 0:
                    continue  
                user_id = int(row[0])
                root.insert(user_id)  
        return root  

    # lee los identificadores de usuario de un archivo CSV y los inserta en un árbol AVL. El archivo debe tener una columna llamada "user_id" con un número entero en cada fila.

    @classmethod
    def run_with_user_ids(cls, user_ids):
        root = cls()
        for user_id in user_ids:
            root.insert(user_id)
        while True:
            print("\nMenu:")
            print("1. Inserta un nodo")
            print("2. Elimina un nodo")
            print("3. Buscar un nodo")
            print("4. Recorrido en orden por nivel")
            print("5. Obtener la altura de un nodo")
            print("6. Obtener abuelo de un nodo")
            print("7. Obtener tío de un nodo")
            print("8. salir")
            choice = int(input("\nIntroduzca su elección: "))
            if choice == 1:
                value = int(input("Introduzca el valor del nodo a insertar: "))
                root.insert(value)
            elif choice == 2:
                value = int(input("Ingrese el valor del nodo a eliminar: "))
                root.delete(value)
            elif choice == 3:
                value = int(input("Introduzca el valor del nodo a buscar: "))
                node = root.search(value)
                if node is None:
                    print(f"Nodo con valor {value} no encontrado.")
                else:
                    print(f"Nodo con valor {value} encontrado.")
            elif choice == 4:
                print("Recorrido en orden por nivel:")
                root.print_level_order()
            elif choice == 5:
                value = int(input("Ingrese el valor del nodo para obtener la altura: "))
                node = root.search(value)
                if node is None:    
                    print(f"Nodo con valor {value} no encontrado.")
                else:
                    height = node.get_height()
                    print(f"Altura del nodo con valor {value}: {height}")
            elif choice == 6:
                value = int(input("Ingrese el valor del nodo para obtener el abuelo: "))
                node = root.search(value)
                if node is None:
                    print(f"Nodo con valor {value} no encontrado.")
                else:
                    grandpa = node.get_grandpa()
                    if grandpa is None:
                        print(f"Nodo con valor {value} no tiene abuelo.")
                    else:
                        print(f"abuelo de nodo con valor {value}: {grandpa.value}")
            elif choice == 7:
                value = int(input("Ingrese el valor del nodo para obtener el tío: "))
                node = root.search(value)
                if node is None:
                    print(f"Nodo con valor {value} no encontrado.")
                else:
                    uncle = node.get_uncle()
                    if uncle is None:
                        print(f"Nodo con valor {value} no tiene tio.")
                    else:
                        print(f"Tío de nodo con valor {value}: {uncle.value}")
            elif choice == 8:
                break
            else:
                print("Elección no válida. Inténtalo de nuevo.")

        #  es un método de clase que crea un nuevo árbol AVL a partir de una lista de identificadores de usuario. Esta función se utiliza para crear un árbol a partir de una lista de identificadores de usuario.

    

