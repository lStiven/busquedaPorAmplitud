
class Nodo():

    def __init__(self):
        self._x = None
        self._y = None
        self._padre = None
        self._ope = None
        self._prof = None
        self._cost = None

    def initialState(self, x, y, padre, ope, prof, cost):
        self._x = x
        self._y = y
        self._padre = padre
        self._ope = ope
        self._prof = prof
        self._cost = cost
    
        