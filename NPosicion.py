class NodoPosicion:
    def __init__(self,posX,posY,combustible):
        self.posicionX=posX
        self.posicionY=posY
        # # # #  #   # # # #

        self.Combustible=combustible
        self.siguientePos=None
    
    def getPosicionX(self):
        return self.posicionX
    def getPosicionY(self):
        return self.posicionY
    def getCombustible(self):
        return self.Combustible



       