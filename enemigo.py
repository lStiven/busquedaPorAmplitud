
class Enemigo():
    
    def __init__(self, x, y, heuristica, live, ope, ide):
        self.x = x
        self.y = y
        self.heuristica = heuristica
        self.live = live
        self.ope = ope
        self.ide = ide

    def morir(self):
        self.live = False

    def vivir(self):
        self.live = True
        