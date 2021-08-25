from ListaPosiciones import ListaPosiciones

class Terreno:

    def __init__(self,nombremapa,posx,posy,posfx,posfy,nFilas,nColumnas):
        self.nombreMapa=nombremapa
        self.posInicialx=int(posx)
        self.posInicialY=int(posy)
        ####
        self.posFinalx=int(posfx)
        self.posFinaly=int(posfy)
        ###
        self.numFilas=int(nFilas)
        self.numColumnas=int(nColumnas)

        self.Lista_Posiciones=ListaPosiciones()
        self.siguiente = None


