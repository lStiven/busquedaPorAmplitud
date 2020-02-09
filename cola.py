

class Cola:
    
    def __init__(self):
        self.nodos = []

    def estaVacia(self):
        return self.nodos == []

    def agregar(self, nodo):
        self.nodos.insert(0, nodo)

    def quitar(self):
        return self.nodos.pop()

    def size(self):
        return len(self.nodos)
