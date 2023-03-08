#lista enlazada

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.primer_nodo = None

    def agregar_nodo(self, valor):
        nuevo_nodo = Nodo(valor)
        if self.primer_nodo is None:
            self.primer_nodo = nuevo_nodo
        else:
            nodo_actual = self.primer_nodo
            while nodo_actual.siguiente is not None:
                nodo_actual = nodo_actual.siguiente
            nodo_actual.siguiente = nuevo_nodo

    def imprimir_lista(self):
        if self.primer_nodo is None:
            print("La lista está vacía.")
        else:
            nodo_actual = self.primer_nodo
            while nodo_actual is not None:
                print(nodo_actual.valor)
                nodo_actual = nodo_actual.siguiente

# Ejemplo de uso
lista = ListaEnlazada()
lista.agregar_nodo(5)
lista.agregar_nodo(10)
lista.agregar_nodo(15)
lista.imprimir_lista()