from Terreno import Terreno
from typing import List, MutableMapping
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
            print('')
            ListaTerrenos.MostrarTerrenos()
            print('-------------------------------')
            OpcionGraficaTerreno=input('Escriba el nombre del terreno a graficar: \n> ')
            GenerarGrafica(ListaTerrenos.getTerreno(OpcionGraficaTerreno))


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
                columnas=elemento10.text
            for elemento11 in elemento9.iter('n'):
                filas=elemento11.text
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
  
    texto1="""
        digraph L{
        node[shape=box fillcolor="#FFFFFF" style =filled]
        subgraph cluster_p{"""
    texto2=f"""label= "{mapa_graficar.nombreMapa}"
        bgcolor = "#E5E8E8"
        edge[dir = "none"]
        """
    texto3=''
    cont=1
    while cont<=mapa_graficar.numFilas:
        texto3+=f"""
         Fila{cont}[label="{mapa_graficar.Lista_Posiciones.buscarPosicion(cont,1).getCombustible()}",group=1,color = white]; 
        """
        cont+=1
    contfilas=1
    texto4=''
    while contfilas!=mapa_graficar.numFilas:
            texto4+=f""" 
            Fila{contfilas}->Fila{contfilas+1};\n"""
            contfilas+=1
        
    texto5=''
    cont1=2
    print(mapa_graficar.numColumnas)
    while cont1<=mapa_graficar.numColumnas:
        texto5+=f"""
        Columna{cont1}[label="{mapa_graficar.Lista_Posiciones.buscarPosicion(1,cont1).getCombustible()}",group={cont1},color = white]; 
        """
        cont1+=1
    contcols=2
    texto6='Fila1->Columna2;\n'
    while contcols!=mapa_graficar.numColumnas:
        texto6+=f"""
         Columna{contcols}->Columna{contcols+1};
        """
        contcols+=1
    
      
       

       
   
    contcols2=2
    texto7='{rank=same;Fila1;'
    while contcols2<=mapa_graficar.numColumnas:
        texto7+=f"""Columna{contcols2};"""
        contcols2+=1
    texto7+='}'


    
    texto8=''
    for i in range(2,mapa_graficar.numFilas+1,1):
        for j in range(2,mapa_graficar.numColumnas+1,1):
            texto8+=f"""nodo{i}_{j}[label="{mapa_graficar.Lista_Posiciones.buscarPosicion(i,j).getCombustible()}",fillcolor=green,group={j}]\n"""
    texto9=''
    for k in range(2,mapa_graficar.numFilas+1,1):
        texto9+=f"""Fila{k}->nodo{k}_2\n"""

    texto10=''
    for i in range(2,mapa_graficar.numFilas+1,1):
        for j in range(2,mapa_graficar.numColumnas+1,1):
            if j==mapa_graficar.numColumnas:
                texto10+=f"""nodo{i}_{j}\n"""
            else:
                texto10+=f"""nodo{i}_{j}->"""

    for i in range(2,mapa_graficar.numFilas+1,1):
        texto10+='{'
        texto10+=f"""rank=same;Fila{i};"""
        for j in range(2,mapa_graficar.numColumnas+1,1):
            texto10+=f"""nodo{i}_{j};"""
        texto10+='}\n'

    texto10+="""
    }
    }
    """
    texto11="""
         {rank=same;Fila3;nodo3_2;nodo3_3;nodo3_4;nodo3_5}
        {rank=same;Fila4;nodo4_2;nodo4_3;nodo4_4;nodo4_5}
        {rank=same;Fila5;nodo5_2;nodo5_3;nodo5_4;nodo5_5}


        Columna2->nodo2_2
        Columna3->nodo2_3
        Columna4->nodo2_4
        Columna5->nodo2_5
    }
    }
    """

  
    txt=texto1+texto2+texto3+texto4+texto5+texto6+texto7+texto8+texto9+texto10
    miarchivo=open('grap.dot','w')
    miarchivo.write(txt)
    miarchivo.close()
    system('dot -Tpng grap.dot -o grap.png')
    system('cd ./grap.png')
    startfile('grap.png')




  

Menu()
