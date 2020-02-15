import random
from cola import Cola
from nodo import Nodo

# leer archivo de texto
def leerMatriz():
    # abrir el archivo
    matriz = open('test.txt', 'r')
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

# buscar las coordenadas de link
def findLink(matriz, visitados, cola):
    for i in range (len(matriz)):
        for j in range (len(matriz[i])):
            if matriz[i][j] == 5:
                # crear un objeto tipo Nodo
                n = Nodo()
                n.initialState(i,j, None, None, None, 1, 0, matriz)
                # agregarlo a la cola como Raiz del arbol
                cola.agregar(n)
                visitados.append(n)
                # habiliat el paso en la posicion de link
                #matriz[i][j] = way
                print()
                del n
                return matriz

# return -> boolean
def checkPadre(lista, x, y, padre):
    # si el nodo no se ha creado anteriormente, retornara False
    # si el nodo ya se ha generado, revisa quien es su padre para evitar devolverse
    for nodo in lista:
        if (nodo._id == padre):
            if (nodo._x == x and nodo._y == y):
                return True
    return False

# return -> list 
def makeWay(listaVisitados, nodo):

    camino = []
    camino.insert(0, nodo._y)
    camino.insert(0, nodo._x)
    padre = nodo._padre
    while(padre != None):
        for i in listaVisitados:
            if (i._id == padre):
                camino.insert(0, i._y)
                camino.insert(0, i._x)
                padre = i._padre
                break
    return camino

def info(nodo, cola, visitados):
    print(f'Posicion actual: ({nodo._x},{nodo._y}) - Padre: ({nodo._padre}) - Id: {nodo._id}')
    print(f'tamanio de la cola {cola.size()}')
    print(f'visitados: {len(visitados)}')

# return -> boolean
def move(tablero, nodo, x, y, target, direction, visitados):
    if (direction == 'up'):
        if (x >= 0):            
            return (tablero[x][y] == way or tablero[x][y] == target) and (not checkPadre(visitados, x, y, nodo._padre))
        return False
        
    if (direction == 'left'):
        if (y >= 0):
            return (tablero[x][y] == way or tablero[x][y] == target) and (not checkPadre(visitados, x, y, nodo._padre))
        return False

    if (direction == 'down'):
        if (x < len(tablero)):
            return (tablero[x][y] == way or tablero[x][y] == target) and (not checkPadre(visitados, x, y, nodo._padre)) 
        return False

    if (direction == 'right'):
        if (y < len(tablero[0])):
            return (tablero[x][y] == way or tablero[x][y] == target) and (not checkPadre(visitados, x, y, nodo._padre))
        return False

def buildDoor(ambiente):
    doorX = (int(random.randint(0, len(ambiente)-1)))
    doorY = (int(random.randint(0, len(ambiente[0])-1)))
    while ambiente[doorX][doorY] != 0:
        doorX = (int(random.randint(0, len(ambiente)-1)))
        doorY = (int(random.randint(0, len(ambiente[0])-1)))
    ambiente[doorX][doorY] = door

def findKey(goal, visitados, cola):
    padre = 0
    prof = None
    _id = 0
    while (True):
        try:
            p = cola.quitar()
            padre = p._id
        except IndexError:
            print('Link se encuentra encerrado')
            print(info(p))
            return False
        
        # condicional si encuentra la llave
        if (p._estado[p._x][p._y] == goal):
            p._estado[p._x][p._y] = link
            meta.initialState(p._x, p._y, p._padre, p._ope, p._prof, p._cost, p._id, p._estado)
            imprimir(meta._estado)
            info(p, colaKey, visitadosKey)
            del p
            return True
        else:
            p._estado[p._x][p._y] = link
            
        # verificar que no se salga de los limites del tablero
        # verifica si puede avanzar en las cuatro cardinalidades con el siguiente orden de prioridad:
        # up, left, down, right. Tambien busca si ya paso por este nodo, de ser asi, no agrega este camino
        # a la cola
        if (move(p._estado, p, p._x-1, p._y, goal, 'up', visitados)):
            temp = p._estado
            temp[p._x][p._y] = way
            _id += 1
            n = Nodo()
            n.initialState(p._x - 1, p._y, padre, 'up', prof, 1, _id, _estado=temp)
            cola.agregar(n)
            visitados.append(n)
            del temp
            del n

        if (move(p._estado, p, p._x, p._y-1, goal, 'left', visitados)):
            temp = p._estado
            temp[p._x][p._y] = way
            _id += 1
            n = Nodo()
            n.initialState(p._x, p._y - 1, padre, 'left', prof, 1, _id, _estado=temp)
            cola.agregar(n)
            visitados.append(n)
            del temp
            del n
        
        if (move(p._estado, p, p._x+1, p._y, goal, 'down', visitados)):
            temp = p._estado
            temp[p._x][p._y] = way
            _id += 1
            n = Nodo()
            n.initialState(p._x + 1, p._y, padre, 'down', prof, 1, _id, _estado=temp)
            cola.agregar(n)
            visitados.append(n)
            del temp
            del n

        if (move(p._estado, p, p._x, p._y+1, goal, 'right', visitados)):
            temp = p._estado
            temp[p._x][p._y] = way
            _id += 1
            n = Nodo()
            n.initialState(p._x, p._y + 1, padre, 'right', prof, 1, _id, _estado=temp)
            cola.agregar(n)
            visitados.append(n)
            del temp
            del n

        del p

def run():
   
    ambiente = leerMatriz()
    ambiente = findLink(ambiente, visitadosKey, colaKey)
    imprimir(ambiente)
    if findKey(key, visitadosKey, colaKey):
        print(makeWay(visitadosKey, meta), '\n')
        # al encontrar la llave, se crea una puerta con coordenadas aleatorias
        buildDoor(ambiente)
        imprimir(ambiente)
        ambiente = findLink(ambiente, visitadosDoor, colaDoor)
        findKey(door, visitadosDoor, colaDoor)
        print(makeWay(visitadosDoor, meta))

def imprimir(matriz):
    for i in range(len(matriz)):
        print(matriz[i])
    print()

if __name__ == "__main__":
    colaKey = Cola()
    colaDoor = Cola()
    visitadosKey = []
    visitadosDoor = []
    meta = Nodo()
    way = 0
    wall = 1
    key = 2
    ganon = 3
    door = 4
    link = 5
    run()