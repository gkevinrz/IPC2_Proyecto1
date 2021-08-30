from NPosicion import NodoPosicion
from ListaCamino import ListaCamino
class ListaPosiciones:
    def __init__(self):
        self.NodoCabeza=None
        self.tamaño=0
        self.posicionInicialx=0
        self.posicionInicialY=0
        self.posicionFinalx=0
        self.posicionFinalY=0
        self.filas=0
        self.columnas=0
        self.PosicionTermina=None
        self.PosicionInicial=None
        self.listacamino=ListaCamino()
        



    def insertarPosicion(self,posicionx,posiciony,gasolina):
        nuevaPosicion=NodoPosicion(posicionx,posiciony,gasolina)
        self.tamaño+=1
        
        if self.NodoCabeza is None:
            self.NodoCabeza=nuevaPosicion
        else:
            tempo=self.NodoCabeza
            while tempo.siguientePos is not None:
                tempo=tempo.siguientePos
            tempo.siguientePos=nuevaPosicion


    def mostrarPosiciones(self):
        tempo=self.NodoCabeza
        while tempo  is not None:
            print('(',tempo.posicionX,tempo.posicionY,')',' ','Combustible',tempo.Combustible)
            tempo = tempo.siguientePos
        
    def buscarPosicionInicial(self):
        temporal=self.NodoCabeza
        while temporal is not None:
            if temporal.posicionX==self.posicionInicialx and temporal.posicionY==self.posicionInicialY:
                return temporal
            temporal=temporal.siguientePos
        return None

    def buscarPosicionFinal(self):
        temporal=self.NodoCabeza
        while temporal is not None:
            if temporal.posicionX==self.posicionFinalx and temporal.posicionY==self.posicionFinalY:
                return temporal
            temporal=temporal.siguientePos
        return None


    def buscarPosicion(self,posx,posy):
        tempo = self.NodoCabeza
        while tempo is not None:
            if tempo.getPosicionX() == posx and tempo.getPosicionY()==posy:
                return tempo
            tempo=tempo.siguientePos          
        return None

    def buscandoCamino1(self):
        actual=self.buscarPosicionInicial()
        final=self.buscarPosicionFinal()
        numeros_enX=final.getPosicionY()-actual.getPosicionY()
        numeros_enY=final.getPosicionX()-actual.getPosicionX()
        cont_enX=actual.getPosicionX()
        cont_enY=actual.getPosicionY()
        self.listacamino.insertarPosicion(actual.getPosicionX(),actual.getPosicionY(),actual.getCombustible(),'1')
        while actual.getPosicionX()!=final.getPosicionX() or actual.getPosicionY()!=final.getPosicionY():
            #esquina superior izquierda
            if (self.buscarPosicion(actual.getPosicionX()-1,actual.getPosicionY()) and self.buscarPosicion(actual.getPosicionX(),actual.getPosicionY()-1)) is None and (self.buscarPosicion(actual.getPosicionX()+1,actual.getPosicionY()) and self.buscarPosicion(actual.getPosicionX(),actual.getPosicionY()+1)) is not None:
                if self.buscarPosicion(actual.getPosicionX(),actual.getPosicionY()+1).getCombustible() < self.buscarPosicion(actual.getPosicionX()+1,actual.getPosicionY()).getCombustible():
                    actual=self.buscarPosicion(actual.getPosicionX(),actual.getPosicionY()+1)
                    self.listacamino.insertarPosicion(actual.getPosicionX(),actual.getPosicionY(),actual.getCombustible(),'1')
                elif self.buscarPosicion(actual.getPosicionX()+1,actual.getPosicionY()).getCombustible() < self.buscarPosicion(actual.getPosicionX(),actual.getPosicionY()+1).getCombustible():
                    actual=self.buscarPosicion(actual.getPosicionX()+1,actual.getPosicionY())
                    self.listacamino.insertarPosicion(actual.getPosicionX(),actual.getPosicionY(),actual.getCombustible(),'1')
            elif self.buscarPosicion(actual.getPosicionX()+1,actual.getPosicionY()) and self.buscarPosicion(actual.getPosicionX(),actual.getPosicionY()+1) is not None:
                pass
            #esquina inferior izquierda
            elif (self.buscarPosicion(actual.getPosicionX()+1,actual.getPosicionY()) and self.buscarPosicion(actual.getPosicionX(),actual.getPosicionY()-1)) is None and (self.buscarPosicion(actual.getPosicionX()-1,actual.getPosicionY()) and self.buscarPosicion(actual.getPosicionX(),actual.getPosicionY()+1)) is not None:
                pass
            #esquina superior derecha
            elif (self.buscarPosicion(actual.getPosicionX()-1,actual.getPosicionY()) and self.buscarPosicion(actual.getPosicionX(),actual.getPosicionY()+1)) is None and (self.buscarPosicion(actual.getPosicionX()+1,actual.getPosicionY()) and self.buscarPosicion(actual.getPosicionX(),actual.getPosicionY()-1)) is not None:
                pass
            elif self.buscarPosicion(actual.getPosicionX()+1,actual.getPosicionY()+1) is None:
                pass
            #esquina inferior derech
            elif (self.buscarPosicion(actual.getPosicionX()+1,actual.getPosicionY()) and self.buscarPosicion(actual.getPosicionX(),actual.getPosicionY()+1)) is None and (self.buscarPosicion(actual.getPosicionX()-1,actual.getPosicionY()) and self.buscarPosicion(actual.getPosicionX(),actual.getPosicionY()-1)) is not None:
                pass

            
                  

            
      















    

    



    

    

