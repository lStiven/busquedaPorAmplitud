import random
from cola import Cola
from nodo import Nodo
from enemigo import Enemigo
import copy
#import Interfaz

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

matrizInterfaz=leerMatriz()

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
#Camino desde la meta, hasta el padre
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
                #camino.insert(0, i)
                padre = i._padre
                break
    return camino

# Trae l información del nodo
def info(nodo, cola, visitados):
    print(f'Posicion actual: ({nodo._x},{nodo._y}) - Padre: ({nodo._padre}) - Id: {nodo._id}')
    print(f'tamanio de la cola {cola.size()}')
    print(f'visitados: {len(visitados)}')

# return -> boolean
def move(tablero, nodo, x, y, target, direction, visitados):
    #En caso de ir hacia arriba, se valida que quien siga no sea padre del nodo actual
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

#Construye una puerta en una posición aleatoria y sin salir de la dimensión correspondiente
def buildDoor(ambiente):
    doorX = (int(random.randint(0, len(ambiente)-1)))
    doorY = (int(random.randint(0, len(ambiente[0])-1)))
    while ambiente[doorX][doorY] != 0:
        doorX = (int(random.randint(0, len(ambiente)-1)))
        doorY = (int(random.randint(0, len(ambiente[0])-1)))
    ambiente[doorX][doorY] = door
    return ambiente

#Se encarga de buscar la llave
def findKey(goal, visitados, cola, meta):
    padre = 0
    prof = None
    _id = 0
    #Saca de la cola al nodo que ya se evaluó
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
            imprimir(meta._estado)
            info(p, cola, visitados)
            del p
            return True
        else:
            p._estado[p._x][p._y] = link
            
        # Verifica que no se salga de los limites del tablero
        # verifica si puede avanzar en las cuatro cardinalidades con el siguiente orden de prioridad:
        # up, left, down, right. Tambien busca si ya paso por este nodo, de ser asi, no agrega este camino
        # a la cola

        expand = False
        #Validaciones en cuanto a cuál dirección se mueve el nodo actual
        if (move(p._estado, p, p._x-1, p._y, goal, 'up', visitados)):
            expand = True
            p._estado[p._x][p._y] = way
            _id += 1
            n = Nodo()
            n.initialState(p._x - 1, p._y, padre, 'up', prof, 1, _id, p._estado, False)
            cola.agregar(n)
            visitados.append(n)
            del n

        if (move(p._estado, p, p._x, p._y-1, goal, 'left', visitados)):
            expand = True
            p._estado[p._x][p._y] = way
            _id += 1
            n = Nodo()
            n.initialState(p._x, p._y - 1, padre, 'left', prof, 1, _id, p._estado, False)
            cola.agregar(n)
            visitados.append(n)
            del n
        
        if (move(p._estado, p, p._x+1, p._y, goal, 'down', visitados)):
            expand = True
            p._estado[p._x][p._y] = way
            _id += 1
            n = Nodo()
            n.initialState(p._x + 1, p._y, padre, 'down', prof, 1, _id, p._estado, False)
            cola.agregar(n)
            visitados.append(n)
            del n

        if (move(p._estado, p, p._x, p._y+1, goal, 'right', visitados)):
            expand = True
            p._estado[p._x][p._y] = way
            _id += 1
            n = Nodo()
            n.initialState(p._x, p._y + 1, padre, 'right', prof, 1, _id, p._estado, False)
            cola.agregar(n)
            visitados.append(n)
            del n

        if not expand:
            p._estado[p._x][p._y] = way

        del p

#Run ejecuta todo lo correspondiente a esta clase
def run():
   
    ambiente = leerMatriz()
    ambiente = findCharacter(ambiente, visitadosKey, colaKey)
    imprimir(ambiente)
    if findKey(key, visitadosKey, colaKey, metaK):
        print(makeWay(visitadosKey, metaK), '\n')
        # al encontrar la llave, se crea una puerta con coordenadas aleatorias
        return makeWay(visitadosKey, metaK)

#Run1 construye una puerta y colocarla 
#en el espacio aleatorio que le corresponde
def run1():
    ambiente = leerMatriz()
    ambiente = findCharacter(ambiente, visitadosDoor, colaDoor)
    buildDoor(ambiente)
    ambiente = findCharacter(ambiente, visitadosDoor, colaDoor)
    return buildDoor(ambiente)
    
#Run2 hace seguimiento para saber en qué posición se encuentra la puerta
#y los nodos por los que debe pasar
def run2():
    if(findKey(door,visitadosDoor,colaDoor,metaD)):
        return makeWay(visitadosDoor,metaD)

#Función para impresión de matrices
def imprimir(matriz):
    for i in range(len(matriz)):
        print(matriz[i])
    print()

#Cola de llave
colaKey = Cola()
#Cola de puerta
colaDoor = Cola()
#Objeto de la clase Enemigo
enemigo = Enemigo()
#Lista que guardará los nodos visitados mientras se llega a la llave
visitadosKey = []
#Lista que guardará los nodos visitados mientras se llega a la puerta
visitadosDoor = []
#Nodo donde se encontrará el nodo meta de la llave
metaK = Nodo()
#Nodo donde se encontrará el nodo meta de la puerta
metaD = Nodo()
#Valores que realmente representan los números de las matrices en los txt
way = 0
wall = 1
key = 2
ganon = 3
door = 4
link = 5

if __name__ == "__main__":
   
    run()