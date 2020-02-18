
class Enemigo():
    
    def __init__(self):
        self._x = None
        self._y = None
        self._heuristica = None
        self._live = None
        self._ope = None
        self._ide = None


    def initialState(self, _x, _y, _heuristica, _live, _ope, _ide):
        self._x = _x
        self._y = _y
        self._heuristica = _heuristica
        self._live = _live
        self._ope = _ope
        self._ide = _ide       

    def morir(self):
        self._live = False

    def vivir(self):
        self._live = True
        