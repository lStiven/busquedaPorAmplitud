
class Nodo():

    def __init__(self):
        self._x = None
        self._y = None
        self._padre = None
        self._ope = None
        self._prof = None
        self._cost = None
        self._id = None
        self._estado = None

    def initialState(self, _x, _y, _padre, _ope, _prof, _cost, _id, _estado):
        self._x = _x
        self._y = _y
        self._padre = _padre
        self._ope = _ope
        self._prof = _prof
        self._cost = _cost
        self._id = _id
        self._estado = _estado
    
        