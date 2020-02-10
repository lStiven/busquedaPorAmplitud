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
                n.initialState(x,y, None, '', None, 1)
                # agregarlo a la cola como Raiz del arbol
                c.agregar(n)
                visitados.append(n)
                # habiliat el paso en la posicion de link
                matriz[i][j] = way

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

def checkNode(lista, x, y):
    # revisa si se ha pasado por las coordenadas dadas
    for i in lista:
        if (x == i._x and y == i._y):
            return True
    return False
    

def findKey(ambiente):
    expand = False
    padre = None
    prof = None
    while (True):
        try:
            p = c.quitar()
        except IndexError:
            print('Link se encuentra encerrado')
            break
        
        if (ambiente[p._x][p._y] == key):
            find = True
            break
        # verificar que no se salga de los limites del tablero
        if (p._x-1 >= 0):
            ''' verifica si puede avanzar en las cuatro cardinalidades con el siguiente orden de prioridad:
            up, left, down, right. Tambien busca si ya paso por este nodo, de ser asi, no agrega este camino
            a la cola '''
            
            if ((ambiente[p._x - 1][p._y] == way or ambiente[p._x - 1][p._y] == key) and not checkNode(visitados, p._x-1, p._y)):
                
                n = Nodo()
                n.initialState(p._x - 1, p._y, padre, 'up', prof, 1)
                c.agregar(n)
                visitados.append(n)

        if (p._y-1 >= 0):
            if ((ambiente[p._x][p._y -1] == way or ambiente[p._x][p._y -1] == key) and not checkNode(visitados, p._x, p._y-1)):
                
                n = Nodo()
                n.initialState(p._x, p._y - 1, padre, 'left', prof, 1)
                c.agregar(n)
                visitados.append(n)
        
        if (p._x+1 < len(ambiente)):
            if ((ambiente[p._x + 1][p._y] == way or ambiente[p._x + 1][p._y] == key) and not checkNode(visitados, p._x+1, p._y)):
                
                n = Nodo()
                n.initialState(p._x + 1, p._y, padre, 'down', prof, 1)
                c.agregar(n)
                visitados.append(n)

        if (p._y+1 < len(ambiente[0])):
            if ((ambiente[p._x][p._y + 1] == way or ambiente[p._x][p._y + 1] == key) and not checkNode(visitados, p._x, p._y+1)):
                
                n = Nodo()
                n.initialState(p._x, p._y + 1, padre, 'right', prof, 1)
                c.agregar(n)
                visitados.append(n)
                
        #print(padre)
    print(f'X -> {p._x}')
    print(f'Y -> {p._y}')
    print(f'tamanio de la cola {c.size()}')
    print(f'visitados:\n{len(visitados)}')

def run():
   
    ambiente = leerMatriz()
    findLink(ambiente)
    findKey(ambiente)

if __name__ == "__main__":
    c = Cola()
    visitados = []
    way = 0
    wall = 1
    key = 2
    ganon = 3
    door = 4
    link = 5
    run()