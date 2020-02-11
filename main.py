import random
from cola import Cola
from nodo import Nodo

# buscar las coordenadas de link
def findLink(matriz):
    for i in range (len(matriz)):
        for j in range (len(matriz[i])):
            if matriz[i][j] == 5:
                # crear un objeto tipo Nodo
                n = Nodo()
                n.initialState(i,j, None, None, None, 1, 0)
                # agregarlo a la cola como Raiz del arbol
                c.agregar(n)
                visitados.append(n)
                # habiliat el paso en la posicion de link
                matriz[i][j] = way
                return matriz

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

def checkPadre(lista, x, y, padre):
    # si el nodo no se ha creado anteriormente, retornara False
    # si el nodo ya se ha generado, revisa quien es su padre para evitar devolverse
    for nodo in lista:
        if (nodo._id == padre):
            if (nodo._x == x and nodo._y == y):
                return True
    return False
    
def makeWay(listaVisitados, nodo):

    camino = []
    camino.insert(0, nodo._y)
    camino.insert(0, nodo._x)
    padre = nodo._padre
    while(padre != None):
        for i in visitados:
            if (i._id == padre):
                camino.insert(0, i._y)
                camino.insert(0, i._x)
                padre = i._padre
                break
    return camino

def info(nodo):
    print(f'Posicion actual: ({nodo._x},{nodo._y}) - Padre: ({nodo._padre}) - Id: {nodo._id}')
    print(f'tamanio de la cola {c.size()}')
    print(f'visitados: {len(visitados)}')

def move(ambiente, nodo, x, y, target, direction):
    if (direction == 'up'):
        if (x >= 0):            
            return (ambiente[x][y] == way or ambiente[x][y] == target) and (not checkPadre(visitados, x, y, nodo._padre))
        return False
        
    if (direction == 'left'):
        if (y >= 0):
            return (ambiente[x][y] == way or ambiente[x][y] == target) and (not checkPadre(visitados, x, y, nodo._padre))
        return False

    if (direction == 'down'):
        if (x < len(ambiente)):
            return (ambiente[x][y] == way or ambiente[x][y] == target) and (not checkPadre(visitados, x, y, nodo._padre)) 
        return False

    if (direction == 'right'):
        if (y < len(ambiente[0])):
            return (ambiente[x][y] == way or ambiente[x][y] == target) and (not checkPadre(visitados, x, y, nodo._padre))
        return False

def buildDoor(ambiente):
    doorX = (int(random.randint(0, len(ambiente)-1)))
    doorY = (int(random.randint(0, len(ambiente[0])-1)))
    while ambiente[doorX][doorY] != 0:
        doorX = (int(random.randint(0, len(ambiente)-1)))
        doorY = (int(random.randint(0, len(ambiente[0])-1)))
    ambiente[doorX][doorY] = door

def findKey(ambiente):
    padre = 0
    prof = None
    id = 0
    while (True):
        try:
            p = c.quitar()
            padre = p._id
        except IndexError:
            print('Link se encuentra encerrado')
            print(info(p))
            return False
        
        # condicional si encuentra la llave
        if (ambiente[p._x][p._y] == key):
            ambiente[p._x][p._y] = link
            return True
            
        # verificar que no se salga de los limites del tablero
        # verifica si puede avanzar en las cuatro cardinalidades con el siguiente orden de prioridad:
        # up, left, down, right. Tambien busca si ya paso por este nodo, de ser asi, no agrega este camino
        # a la cola
        if (move(ambiente, p, p._x-1, p._y, key, 'up')):
            id += 1
            n = Nodo()
            n.initialState(p._x - 1, p._y, padre, 'up', prof, 1, id)
            c.agregar(n)
            visitados.append(n)

        if (move(ambiente, p, p._x, p._y-1, key, 'left')):
            id += 1
            n = Nodo()
            n.initialState(p._x, p._y - 1, padre, 'left', prof, 1, id)
            c.agregar(n)
            visitados.append(n)
        
        if (move(ambiente, p, p._x+1, p._y, key, 'down')):
            id += 1
            n = Nodo()
            n.initialState(p._x + 1, p._y, padre, 'down', prof, 1, id)
            c.agregar(n)
            visitados.append(n)

        if (move(ambiente, p, p._x, p._y+1, key, 'right')):
            id += 1
            n = Nodo()
            n.initialState(p._x, p._y + 1, padre, 'right', prof, 1, id)
            c.agregar(n)
            visitados.append(n)

def run():
   
    matriz = leerMatriz()
    ambiente = findLink(matriz)
    print(ambiente)
    if findKey(ambiente):
        # al encontrar la llave, se crea una puerta con coordenadas aleatorias
        buildDoor(ambiente)
        pass


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