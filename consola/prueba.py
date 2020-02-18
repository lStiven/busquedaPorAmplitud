from main import *
def run():
    c = Cola()
    lista = []
    if True:
        n = Nodo()
        n.initialState(2,3,0,'',0,0)
        c.agregar(n)
        lista.append(n)
    if True:
        n = Nodo()
        n.initialState(1,3,0,'',0,0)
        c.agregar(n)
        lista.append(n)
    if True:
        n = Nodo()
        n.initialState(2,2,0,'',0,0)
        c.agregar(n)
        lista.append(n)
    if True:
        n = Nodo()
        n.initialState(0,3,0,'',0,0)
        c.agregar(n)
        lista.append(n)
    if True:
        n = Nodo()
        n.initialState(1,2,0,'',0,0)
        c.agregar(n)
        lista.append(n)
    if True:
        n = Nodo()
        n.initialState(2,3,0,'',0,0)
        c.agregar(n)
        lista.append(n)
    if True:
        n = Nodo()
        n.initialState(2,2,0,'',0,0)
        c.agregar(n)
        lista.append(n)

    x = Nodo()
    x.initialState(1,2,0,'',0,0)
    cont = 1
    for i in lista:
        print(cont)
        if ((x._x == i._x and x._y == i._y)):
            print(True)
            break
        cont += 1

if __name__ == "__main__":
    run()