from NCamino import NodoCamino
class ListaCamino:
    def __init__(self):
        self.inicio=None


    def insertarPosicion(self,posx,posy,comb,marca):
        nuevaPosicion=NodoCamino(posx,posy,comb,marca)        
        if self.inicio is None:
            self.inicio=nuevaPosicion
        else:
            tempo=self.inicio
            while tempo.siguiente is not None:
                tempo=tempo.siguiente
            tempo.siguiente=nuevaPosicion
    def MostrarPosiciones(self):
        tempo = self.inicio
        while tempo is not None:
            print(tempo.PosicionX,tempo.PosicionY,tempo.Combustible)
            tempo = tempo.siguiente
    def buscarPosicion(self,posx,posy):
        tempo = self.inicio
        while tempo is not None:
            if tempo.PosicionX == posx and tempo.PosicionY==posy:
                return tempo
            tempo=tempo.siguiente          
        return None