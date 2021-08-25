from Terreno import Terreno
from typing import List
import xml.etree.ElementTree as ET
from Lista_Terrenos import ListaTerreno
from ListaPosiciones import ListaPosiciones
from os import system,startfile
#Menu
def Menu():
    Opcion=''
    OpcionTerreno=''
    OpcionGraficaTerreno=''
    ListaTerrenos=ListaTerreno()
    
    while(Opcion!='6'):
        print('|------------- Menu --------------|')
        print('| 1. Cargar Archivo               |')
        print('| 2. Procesar Archivo             |')
        print('| 3. Escribir archivo de salida   |')
        print('| 4. Mostrar datos del estudiante |')
        print('| 5. Generar Gráfica              |')
        print('| 6. Salir                        |')
        print('|---------------------------------|')
        Opcion=input('Seleccione una opción: \n > ')
        if Opcion=='1':
            Nombre_Archivo=input('Nombre del archivo: \n> ')
            Ruta='./'+Nombre_Archivo
            CargarArchivo(Ruta,ListaTerrenos)

        elif Opcion=='2':
            print('')
            OpcionTerreno=input('Nombre del mapa a procesar: \n > ')
            TerrenoAProcesar=ListaTerrenos.getTerreno(OpcionTerreno)
            #print(TerrenoAProcesar.Lista_Posiciones.buscandoCamino1().getCombustible())
            #print(TerrenoAProcesar.Lista_Posiciones.buscandoCamino1().getPosicionX(),TerrenoAProcesar.Lista_Posiciones.buscandoCamino1().getPosicionY())
            TerrenoAProcesar.Lista_Posiciones.buscandoCamino1()
            TerrenoAProcesar.Lista_Posiciones.listacamino.MostrarPosiciones()
                    #ListaTerrenos.MostrarTerrenos()
    
        elif Opcion=='3':
            pass   
        elif Opcion=='4':
            DatosEstudiantiles()
        elif Opcion=='5':
            map=ListaTerrenos.inicio
            GenerarGrafica(map)

##
def CargarArchivo(Ruta,listaterrenos):
    
    posinX=''
    posinY=''
    posfinX=''
    posfinY=''
    filas=''
    columnas=''
    tree=ET.parse(Ruta)
    root=tree.getroot()
    print('')
    for elemento in root:
        for elemento2 in elemento.iter('posicioninicio'):
            for elemento3 in elemento2.iter('x'):
                posinX=elemento3.text
            for elemento4 in elemento2.iter('y'):
                posinY=elemento4.text
        for elemento5 in elemento.iter('posicionfin'):
            for elemento6 in elemento5.iter('x'):
                posfinX=elemento6.text
            for elemento7 in elemento5.iter('y'):
                posfinY=elemento7.text
        for elemento9 in elemento.iter('dimension'):
            for elemento10 in elemento9.iter('m'):
                filas=elemento10.text
            for elemento11 in elemento9.iter('n'):
                columnas=elemento11.text
        listaterrenos.insertarTerreno(elemento.attrib['nombre'],posinX,posinY,posfinX,posfinY,filas,columnas)
        terreno=listaterrenos.getTerreno(elemento.attrib['nombre'])
        terreno.Lista_Posiciones.posicionInicialx=int(posinX)
        terreno.Lista_Posiciones.posicionInicialY=int(posinY)
        terreno.Lista_Posiciones.posicionFinalx=int(posfinX)
        terreno.Lista_Posiciones.posicionFinalY=int(posfinY)
        terreno.Lista_Posiciones.filas=int(filas)
        terreno.Lista_Posiciones.columnas=int(columnas)
        for elemento8 in elemento.iter('posicion'):
            terreno.Lista_Posiciones.insertarPosicion(int(elemento8.attrib['x']),int(elemento8.attrib['y']),int(elemento8.text))
        print('Se ha creado nuevo mapa: '+elemento.attrib['nombre'])    
    print('')
    ##
def DatosEstudiantiles():
    print(' ')
    print('| Kevin Gerardo Ruíz Yupe ')
    print('| 201903791               ')
    print('| Introducción a la programación y computación 2 sección "C"')
    print('| Ingeniería en Ciencias y Sistemas')
    print('| 4to Semestre')
    print('')
def GenerarGrafica(mapa_graficar):
    texto="""
    digraph L{
    node[shape=box fillcolor="#FFEDBB" style =filled]
    
    subgraph cluster_p{
        label= "Matriz Dispersa"
        bgcolor = "#398D9C"
        raiz[label = "0,0"]
        edge[dir = "none"]
        /*Aqui creamos las cabeceras
        de las filas*/
        Fila1[label="1",group=1];   
        Fila2[label="2",group=1];   
        Fila3[label="3",group=1];   
        Fila4[label="4",group=1];   
        Fila5[label="5",group=1];   
        /*Aqui enlazamos los
        nodos de las filas*/
        Fila1->Fila2;
        Fila2->Fila3;
        Fila3->Fila4;
        Fila4->Fila5; 
        /*Aqui enlazamos los
        nodos de las COLUMNAS*/
        Columna1[label = "1",group=2,fillcolor=yellow];
        Columna2[label = "2",group=3,fillcolor=yellow];
        Columna3[label = "3",group=4,fillcolor=yellow];
        Columna4[label = "4",group=5,fillcolor=yellow];
        Columna5[label = "5",group=6,fillcolor=yellow];
        /*Aqui enlazar los nodos
        de las caberas de las columnas*/
        Columna1->Columna2;
        Columna2->Columna3;
        Columna3->Columna4;
        Columna4->Columna5;
        /*aqui vamos a unir la raiz a las
        filas y a las columnas*/
        raiz->Fila1;
        raiz->Columna1;
        /*aqui vamos a alinear cada 
        nodo cabecera de las columnas*/
        {rank=same;raiz;Columna1;Columna2;Columna3;Columna4;Columna5}
        nodo1_1[label="1,1",fillcolor=green,group=2]
        nodo1_2[label="1,2",fillcolor=green,group=3]
        nodo1_3[label="1,3",fillcolor=green,group=4]
        nodo1_4[label="1,4",fillcolor=green,group=5]
        nodo1_5[label="1,5",fillcolor=green,group=6]
        nodo2_1[label="2,1",fillcolor=green,group=1]
        nodo2_2[label="2,2",fillcolor=green,group=3]
        
        Fila1->nodo1_1
        nodo1_1->nodo1_2
        nodo1_2->nodo1_3
        nodo1_3->nodo1_4
        nodo1_4->nodo1_5
        {rank=same;Fila1;nodo1_1;nodo1_2;nodo1_3;nodo1_4;nodo1_5}
        Fila2->nodo2_1
        nodo2_1->nodo2_2
        {rank=same;Fila2;nodo2_1;nodo2_2}

        Columna1->nodo1_1
        Columna2->nodo1_2
        Columna3->nodo1_3
        Columna4->nodo1_4
        Columna5->nodo1_5
        
        nodo1_1->nodo2_1
        nodo1_2->nodo2_2
    }
    }
    """
    miarchivo=open('grap.dot','w')
    miarchivo.write(texto)
    miarchivo.close()
    system('dot -Tpng grap.dot -o grap.png')
    system('cd ./grap.png')
    startfile('grap.png')




  

Menu()
