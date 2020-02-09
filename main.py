from cola import Cola
from nodo import Nodo

# buscar las coordenadas de link
def findLink(matriz):
    for i in range (len(matriz)):
        for j in range (len(matriz[i])):
            if matriz[i][j] == 5:
                # guardar las coordenadas de link
                x = i
                y = j
                # crear un objeto tipo Nodo
                n = Nodo()
                n.initialState(x,y, None, None, 0, 0)
                # agregarlo a la cola como Raiz del arbol
                c.agregar(n)

# leer archivo de texto
def leerMatriz():
    # abrir el archivo
    matriz = open('archivo.txt', 'r')
    # crear diccionario para almacenar la matriz
    tablero = {}
    # guarda cada linea de la matriz separando por salto de linea
    linea = matriz.readlines()
    i = 0
    # recorre cada linea y se almacena en 'x' (filas)
    for l in linea:
        x = l.split('\n')
        tablero[i] = []
        #j = 0
        for colum in x[0]:
            # separa cada caracter de manera individual
            y = colum.split(' ')
            # castea el caracter a un entero y lo almacena en su respectiva fila
            # hasta que se complete toda la cadena
            tablero[i].append(int(y[0]))
            #j += 1
        i += 1
    # cierra el archivo.txt
    matriz.close()
    return tablero

def recorrer(ambiente):
    p = c.quitar()
    padre = 0
    prof = 0
    
    if (ambiente[(p._x - 1)][p._y] == way):
        n = Nodo()
        n.initialState((p._x - 1), p._y, padre, 'up', prof, 1)
        c.agregar(n)

    if (ambiente[(p._x)][(p._y -1)] == way):
        n = Nodo()
        n.initialState(p._x, (p._y - 1), padre, 'left', prof, 1)
        c.agregar(n)
    
    if (ambiente[p._x + 1][p._y] == way):
        n = Nodo()
        n.initialState(p._x + 1, p._y, padre, 'down', prof, 1)
        c.agregar(n)

    while(True):
        print(c.quitar()._ope)
        if (c.estaVacia()):
            break

def limites(matriz, x, y):
    pass
    
def run():
   
    ambiente = leerMatriz()
    findLink(ambiente)
    recorrer(ambiente)

if __name__ == "__main__":
    c = Cola()
    way = 0
    wall = 1
    key = 2
    ganon = 3
    door = 4
    link = 5
    run()