import random
from cola import Cola
from nodo import Nodo
from enemigo import Enemigo
import copy

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
def findCharacter(matriz, visitados, cola):
    contEnemigos = 0
    for i in range (len(matriz)):
        for j in range (len(matriz[i])):
            if matriz[i][j] == 5:
                # crear un objeto tipo Nodo
                n = Nodo()
                n.initialState(i,j, None, None, None, 1, 0, matriz, False)
                # agregarlo a la cola como Raiz del arbol
                cola.agregar(n)
                visitados.append(n)
                # habiliat el paso en la posicion de link
                #matriz[i][j] = way
                print()
                del n
            # crea un objeto de tipo enemigo
            if matriz[i][j] == 3:
                enemigo.initialState(i, j, None, True, None, contEnemigos)
                contEnemigos += 1
                
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
    #camino.insert(0, nodo._y)
    #camino.insert(0, nodo._x)
    camino.insert(0, nodo._ope)
    padre = nodo._padre
    while(padre != None):
        for i in listaVisitados:
            if (i._id == padre):
                #camino.insert(0, i._y)
                #camino.insert(0, i._x)
                camino.insert(0, i._ope)
                padre = i._padre
                break
    return camino
# return -> string
def info(nodo, cola, visitados):
    print(f'Posicion actual: ({nodo._x},{nodo._y}) - Padre: ({nodo._padre}) - Id: {nodo._id}')
    print(f'tamanio de la cola {cola.size()}')
    print(f'visitados: {len(visitados)}')

# return -> boolean
def move(tablero, nodo, x, y, target, direction, visitados):
    if (direction == 'up'):
        return (tablero[x][y] == way or tablero[x][y] == target) and (not checkPadre(visitados, x, y, nodo._padre))

    if (direction == 'left'):
        return (tablero[x][y] == way or tablero[x][y] == target) and (not checkPadre(visitados, x, y, nodo._padre))

    if (direction == 'down'):
        return (tablero[x][y] == way or tablero[x][y] == target) and (not checkPadre(visitados, x, y, nodo._padre))

    if (direction == 'right'):
        return (tablero[x][y] == way or tablero[x][y] == target) and (not checkPadre(visitados, x, y, nodo._padre))

# return -> matriz
def buildDoor(matriz):
    doorX = (int(random.randint(0, len(matriz)-1)))
    doorY = (int(random.randint(0, len(matriz[0])-1)))
    while matriz[doorX][doorY] != 0:
        doorX = (int(random.randint(0, len(matriz)-1)))
        doorY = (int(random.randint(0, len(matriz[0])-1)))
    matriz[doorX][doorY] = door
    return matriz


def findKey(goal, visitados, cola, meta):
    padre = 0
    prof = None
    _id = 0
    while (True):
        try:
            p = cola.quitar()
            padre = p._id
        except IndexError:
            print('Link se encuentra encerrado')
            print(info(p, cola, visitados))
            return False
        
        # condicional si encuentra la llave
        if (p._estado[p._x][p._y] == goal):
            p._estado[p._x][p._y] = link
            meta.initialState(p._x, p._y, p._padre, p._ope, p._prof, p._cost, p._id, p._estado, False)
            print('Link encuentra su objetivo (llave o puerta)')
            imprimir(meta._estado)
            info(p, cola, visitados)
            del p
            return True
        else:
            p._estado[p._x][p._y] = link

        # variable para verificar si un nodo se expande o no
        expand = False
            
        # verificar que no se salga de los limites del tablero
        # verifica si puede avanzar en las cuatro cardinalidades con el siguiente orden de prioridad:
        # up, left, down, right. Tambien busca si ya paso por este nodo, de ser asi, no agrega este camino
        # a la cola
        if (p._x-1 >= 0):
            # si al avanzar le estorba un enemigo, link lo mata y termina su turno
            if (p._estado[p._x-1][p._y] == ganon):
                expand = True
                p.atacar(True)
                enemigo.morir()
                temp = copy.deepcopy(p._estado)
                temp[p._x-1][p._y] = way
                _id += 1
                # crea un objeto tipo nodo(link) y lo agrega a la cola
                n = Nodo()
                n.initialState(p._x, p._y, padre, 'atack', p._prof, p._cost, _id, temp, p._atack)
                cola.agregar(n)
                visitados.append(n)

                # eliminar variables
                del n
                del temp
            
            # si no encuentra un enemigo, se valida si link puede avanzar
            elif (move(p._estado, p, p._x-1, p._y, goal, 'up', visitados)):
                # en caso de haber atacado en el turno anterior, se inhabilita el ataque
                # para que pueda avanzar
                if (p._atack):
                    p._atack = False
                expand = True
                p._estado[p._x][p._y] = way
                _id += 1
                n = Nodo()
                n.initialState(p._x - 1, p._y, padre, 'up', prof, 1, _id, p._estado, False)
                cola.agregar(n)
                visitados.append(n)
                del n

        if (p._y-1 >= 0):   
            if (p._estado[p._x][p._y-1] == ganon):
                expand = True
                p.atacar(True)
                enemigo.morir()
                temp = copy.deepcopy(p._estado)
                temp[p._x][p._y-1] = way
                _id += 1
                n = Nodo()
                n.initialState(p._x, p._y, padre, 'atack', p._prof, p._cost, _id, temp, p._atack)
                cola.agregar(n)
                visitados.append(n)

                del n
                del temp

            elif (move(p._estado, p, p._x, p._y-1, goal, 'left', visitados)):
                if (p._atack):
                    p._atack = False
                expand = True
                p._estado[p._x][p._y] = way
                _id += 1
                n = Nodo()
                n.initialState(p._x, p._y - 1, padre, 'left', prof, 1, _id, p._estado, False)
                cola.agregar(n)
                visitados.append(n)
                del n

        if (p._x+1 < len(p._estado)):
            if (p._estado[p._x+1][p._y] == ganon):
                expand = True
                p.atacar(True)
                enemigo.morir()
                temp = copy.deepcopy(p._estado)
                temp[p._x+1][p._y] = way
                _id += 1
                n = Nodo()
                n.initialState(p._x, p._y, padre, 'atack', p._prof, p._cost, _id, temp, p._atack)
                cola.agregar(n)
                visitados.append(n)

                del n
                del temp

            elif (move(p._estado, p, p._x+1, p._y, goal, 'down', visitados)):
                if (p._atack):
                    p._atack = False
                expand = True
                p._estado[p._x][p._y] = way
                _id += 1
                n = Nodo()
                n.initialState(p._x + 1, p._y, padre, 'down', prof, 1, _id, p._estado, False)
                cola.agregar(n)
                visitados.append(n)
                del n
            
        if (p._y+1 < len(p._estado[0])):
            if (p._estado[p._x][p._y+1] == ganon):
                expand = True
                p.atacar(True)
                enemigo.morir()
                temp = copy.deepcopy(p._estado)
                temp[p._x][p._y+1] = way
                _id += 1
                n = Nodo()
                n.initialState(p._x, p._y, padre, 'atack', p._prof, p._cost, p._id, temp, p._atack)
                cola.agregar(n)
                visitados.append(n)

                del n
                del temp

            elif (move(p._estado, p, p._x, p._y+1, goal, 'right', visitados)):
                if (p._atack):
                    p._atack = False
                expand = True
                p._estado[p._x][p._y] = way
                _id += 1
                n = Nodo()
                n.initialState(p._x, p._y + 1, padre, 'right', prof, 1, _id, p._estado, False)
                cola.agregar(n)
                visitados.append(n)
                del n
        # si el nodo no se expande (no tiene salida, ya que es evitando devolverse)
        # se ubica un 0, para indicar que es una hoja del arbol
        if not expand:
            p._estado[p._x][p._y] = way

        ########## T U R N O   E N E M I G O ######### 
        
        if (enemigo._live):
            direccion = ''
            heuristica = 100
            # up
            if (enemigo._x-1 >= 0):
                if (p._estado[enemigo._x-1][enemigo._y]) == way:
                    up = abs(((enemigo._x-1)-p._x)+(enemigo._y - p._x))
                    if heuristica > up:
                        heuristica = up
                        direccion = 'up'
            
            #left
            if (p._y-1 >= 0):
                if (p._estado[enemigo._x][enemigo._y-1]) == way:
                    left = abs((enemigo._x - p._x) + ((enemigo._y-1) - p._y))
                    if heuristica > left:
                        heuristica = left
                        direccion = 'left'

            #down
            if (p._x+1 < len(p._estado)):
                if (p._estado[enemigo._x][enemigo._y-1]) == way:
                    down = abs(((enemigo._x+1) - p._x) + (enemigo._y - p._y))   
                    if heuristica > down:
                        heuristica = down
                        direccion = 'down'

            #right
            if (p._y+1 < len(p._estado[0])):
                if (p._estado[enemigo._x][enemigo._y-1]) == way:
                    right = abs((enemigo._x - p._x) + (enemigo._y - (p._y+1)))
                    if heuristica >  right:
                        heuristica = right
                        direccion = 'right'

            if direccion == 'up':
                p._estado[enemigo._x][enemigo._y] = way
                p._estado[enemigo._x][enemigo._y-1] = ganon
            if direccion == 'left':
                p._estado[enemigo._x][enemigo._y] = way
                p._estado[enemigo._x][enemigo._y-1] = ganon
            if direccion == 'down':
                p._estado[enemigo._x][enemigo._y] = way
                p._estado[enemigo._x+1][enemigo._y] = ganon
            if direccion == 'right':
                p._estado[enemigo._x][enemigo._y] = way
                p._estado[enemigo._x][enemigo._y+1] = ganon
            
        del p

def run():

    # lee archivo de texto plano y crea una matriz bidimencional mediante un diccionario
    ambiente = leerMatriz()
    # busca los diferentes componentes del escenario (link, ganon, muros, etc)
    ambiente = findCharacter(ambiente, visitadosKey, colaKey)
    print('Tablero inicial')
    imprimir(ambiente)
    if findKey(key, visitadosKey, colaKey, metaK):
        print(makeWay(visitadosKey, metaK), '\n')
        # al encontrar la llave, se crea una puerta con coordenadas aleatorias
        puerta = copy.deepcopy(ambiente)
        puerta = buildDoor(metaK._estado)
        print('Se genera puerta aleatoria (4)' )
        imprimir(puerta)
        puerta = findCharacter(metaK._estado, visitadosDoor, colaDoor)
        findKey(door, visitadosDoor, colaDoor, metaD)
        print(makeWay(visitadosDoor, metaD))
        return makeWay(visitadosKey, metaK)

def imprimir(matriz):
    for i in range(len(matriz)):
        print(matriz[i])
    print()

ambiente = dict()
colaKey = Cola()
colaDoor = Cola()
enemigo = Enemigo()
visitadosKey = []
visitadosDoor = []
metaK = Nodo()
metaD = Nodo()
way = 0
wall = 1
key = 2
ganon = 3
door = 4
link = 5

if __name__ == "__main__":
    
    run()