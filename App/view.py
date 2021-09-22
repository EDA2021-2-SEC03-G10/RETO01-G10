﻿"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf

default_limit = 1000
sys.setrecursionlimit(default_limit*10)


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print(chr(27)+"[1;32m")
    print("Bienvenido")
    print(chr(27)+"[0;37m")
    print(chr(27)+"[4;32m"+"1" + chr(27)+ "[0;37m" + "- Cargar información en el catálogo")
    print(chr(27)+"[4;32m"+ "2" + chr(27)+ "[0;37m" + "- Listar cronológicamente los artistas")
    print(chr(27)+"[4;32m"+ "3" + chr(27)+ "[0;37m" + "- Listar cronologicamente las adquisiciones")
    print(chr(27)+"[4;32m"+ "4" + chr(27)+ "[0;37m" + "- Clasificar las obras de un artista por tecnica")
    print(chr(27)+"[4;32m"+ "5" + chr(27)+ "[0;37m" + "- Clasificar las obras por la nacionalidad de sus creadores")
    print(chr(27)+"[4;32m"+ "6" + chr(27)+ "[0;37m" + "- Transportar obras de un departamento")

def initCatalog():
    return controller.initCatalog()

def loadData(catalog):
    controller.loadData(catalog)

# Requisito 1
def listarCronologicamente(catalog, añoInicial, añoFinal):
    return controller.listarCronologicamente(catalog, añoInicial, añoFinal)

# Requisito 4
def nacionalidadCreadores(catalog):
    nacionalidades = controller.nacionalidadCreadores(catalog)
    return nacionalidades

def transportar_obras(catalog):
    pass

catalog = None

"""
Menu principal
"""
while True:
    printMenu()
    print(chr(27)+"[1;37m")
    inputs = input('Seleccione una opción para continuar: ')
    print(chr(27)+"[0;37m")

    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")
        catalog = initCatalog()
        loadData(catalog)
        print('Obras cargadas: ' + str(lt.size(catalog['obras'])))
        print('Artistas cargados: ' + str(lt.size(catalog['artistas'])))

    elif int(inputs[0]) == 2:
        añoInicial = int(input("Ingrese el año inicial(yyyy): "))
        añoFinal = int(input("Ingrese el año final(yyyy): "))
        print("Listando los artistas de manera cronologica ....")
        
        listaEnRango = listarCronologicamente(catalog, añoInicial, añoFinal)
        tamaño = lt.size(listaEnRango)
        print("\n")
        print("Numero de artistas dentro del rango: " + str(tamaño)+"\n")

        artist1 = lt.getElement(listaEnRango, 1)
        artist2 = lt.getElement(listaEnRango, 2)
        artist3 = lt.getElement(listaEnRango, 3)
        artist4 = lt.getElement(listaEnRango, tamaño-2)
        artist5 = lt.getElement(listaEnRango, tamaño-1)
        artist6 = lt.getElement(listaEnRango, tamaño)

        print(chr(27)+"[1;37m"+"Los primeros y los ultimos 3 son: "+chr(27)+"[0;37m")

        artistas = artist1,artist2,artist3,artist4,artist5,artist6
        for artista in artistas:    
            print(chr(27)+"[1;34m"+ "Nombre: " + chr(27)+"[0;37m"+ artista["DisplayName"],
                    chr(27)+"[1;34m"+ ", Nacimiento: "+ chr(27)+"[0;37m"+ artista["BeginDate"], 
                    chr(27)+"[1;34m"+ ", Fallecimmiento: " + chr(27)+"[0;37m"+ artista["EndDate"],
                    chr(27)+"[1;34m"+ ", Nacionalidad: " + chr(27)+"[0;37m"+ artista["Nationality"],
                    chr(27)+"[1;34m"+ ", Genero: " + chr(27)+"[0;37m"+ artista["Gender"])
    
    elif int(inputs[0]) == 3:
        pass

    elif int(inputs[0]) == 4:
        pass

    elif int(inputs[0]) == 5:
       clasificacion,obras = nacionalidadCreadores(catalog)
       print(chr(27)+"[1;44m"+"NACIONALIDADES CON EL MAYOR NUMERO DE OBRAS"+chr(27)+"[0;37m")
       print("\n")
       for pais in lt.iterator(clasificacion): 
           for llave in pais.keys():
               print(chr(27)+"[1;34m"+llave+"   "+chr(27)+"[0;37m"+str(pais[llave]))
               print("\n")

       print(chr(27)+"[1;44m"+"INFORMACION DE LAS 20 PRIMERAS OBRAS DE LA NACIONALIDAD CON EL MAYOR NUMERO DE OBRAS"+chr(27)+"[0;37m")
       conteo = 0
       for obra in lt.iterator(obras): 
           print("\n")
           conteo += 1
           for llave2 in obra.keys():
               print(chr(27)+"[1;34m"+llave2+": "+chr(27)+"[0;37m"+obra[llave2])
           if conteo == 25:
               break 
           



    elif int(inputs[0]) == 6:
        departamento = (input("Ingrese el departamento a transportar las obras"))
        transportar_obras(catalog,departamento)

    else:
        sys.exit(0)
sys.exit(0)
