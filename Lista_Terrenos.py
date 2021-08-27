from ListaPosiciones import ListaPosiciones
from Terreno import Terreno

class ListaTerreno():
    def __init__(self):
        self.inicio = None 
        self.size = 0 

    def insertarTerreno(self, nombreMapa, posinicialX,posicionInicialY,posicionFinalX,posicionFinalY,numFilas,numColumnas):
        nuevoTerreno = Terreno(nombreMapa, posinicialX,posicionInicialY,posicionFinalX,posicionFinalY,numFilas,numColumnas) 
        self.size += 1 
        if self.inicio is None:
            self.inicio=nuevoTerreno
            
        else:
            tempo=self.inicio
            while tempo.siguiente is not None:
                tempo=tempo.siguiente
            tempo.siguiente=nuevoTerreno


    def getTerreno(self, nombreTerreno):
        tempo = self.inicio
        while tempo is not None:
            if tempo.nombreMapa == nombreTerreno:
                return tempo    
            tempo = tempo.siguiente
        return None


    def MostrarTerrenos(self):
        tempo = self.inicio
        while tempo is not None:
            print('- Nombre del Terreno: ',tempo.nombreMapa, 'Posicion Inicial: ','(',tempo.posInicialx,',',tempo.posInicialY,')')
            print('- Dimensiones:',tempo.numFilas,'x',tempo.numColumnas)
            #tempo.Lista_Posiciones.mostrarPosiciones()
            tempo = tempo.siguiente

