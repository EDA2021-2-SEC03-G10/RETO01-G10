"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf
import datetime

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos
def newCatalog():
    catalog = {'obras': None,
               'artistas': None}

    catalog['obras'] = lt.newList()
    catalog['artistas'] = lt.newList()

    return catalog
# Funciones para agregar informacion al catalogo

def addObra(catalog, obra):
    lt.addLast(catalog['obras'], obra)

def addArtist(catalog, artista):
    lt.addLast(catalog['artistas'], artista)
# Funciones para creacion de datos



# Funciones de consulta
def listarCronologicamente(catalog, añoInicial, añoFinal):
    listaEnRango = lt.newList()
    for artista in lt.iterator(catalog["artistas"]):
        if int(artista["BeginDate"]) >= añoInicial and int(artista["BeginDate"]) <= añoFinal:
            lt.addLast(listaEnRango, artista)

    listaFinal = lt.newList()
    for i in range(añoInicial,añoFinal+1):
        for elemento in lt.iterator(listaEnRango):
            if int(elemento["BeginDate"]) == i:
                lt.addLast(listaFinal, elemento)  

    return listaFinal
   
def listarAdquisiciones(catalog, fechaInical, fechaFinal):
    fechas = lt.newList()
    compra=0
    for obra in lt.iterator(catalog['obras']):
        if (obra["CreditLine"])=="Purchase":
            compra+=1
        if (obra["DateAcquired"]) != "":
            año3,mes3,dia3 = map(int, (obra['DateAcquired']).split('-'))
            fechaA=(año3,mes3,dia3)
            if fechaA >= fechaInical and fechaA<= fechaFinal:
                lt.addLast(fechas, obra)
    adquisiciones = lt.newList()
    for i in range(fechaInical[0],fechaFinal[0]):
        for eso in lt.iterator(fechas):
            if fechaA[0]== i:
                lt.addLast(adquisiciones, eso)  

    return adquisiciones,compra

def clasificar_tecnica(catalog,nombre):
    datos= {}    
    for artista in lt.iterator(catalog["artistas"]):
        if artista["DisplayName"] ==nombre:
            datos[artista["ConstituentID"]] = {"Nombre":artista["DisplayName"]}  
        for obra in lt.iterator(catalog["obras"]):
            for id in obra["ConstituentID"].split(", "):
                id = id.replace("[","")
                id = id.replace("]","")
                tecnica = datos[id]["Nombre"]
            pass

def nacionalidadCreadores(catalog):
    dictNacionalidades = {}
    info = {}
    for artista in lt.iterator(catalog["artistas"]):
        if artista["Nationality"] not in dictNacionalidades:
            dictNacionalidades[artista["Nationality"]]= 0 
        info[artista["ConstituentID"]] = {"Nacionalidad":artista["Nationality"],"Nombre":artista["DisplayName"]}
    
    for obra in lt.iterator(catalog["obras"]):
        for id in obra["ConstituentID"].split(", "):
            id = id.replace("[","")
            id = id.replace("]","")
            pais = info[id]["Nacionalidad"]
            dictNacionalidades[pais] += 1

    paisDesconocido = dictNacionalidades[""]
    dictNacionalidades["Nationality unknown"]+= paisDesconocido
    dictNacionalidades.pop("")


    return dictNacionalidades,info

def transportar_obras(catalog,departamento):
    count = 0
    peso= 0
    precio_estimado=0
    obras_departamento= lt.newList()
    obras_precios= lt.newList()
    for obra in lt.iterator(catalog["obras"]):
        Altura=1
        Ancho=1
        Largo=1
        if departamento == (obra["Department"]):
            count += 1
            num_int = (obra["Dimensions"]).replace(")","(")
            num_int = num_int.split ("(")
            mayor=0
            for elemento in (num_int):
                numeros= 1
    return obras_departamento,count,peso

# Funciones utilizadas para comparar elementos dentro de una lista

def comparar_antigüedad(obra1, obra2):
    if (obra1["Date"]) != "" and (obra2["Date"] !=""):
        return (int(obra1['Date']) < int(obra2['Date']))

# Funciones de ordenamiento

def sortpaises(dict):
    lista = lt.newList("ARRAY_LIST") 
    for i in range(0,10):
        mayor = -1
        llaveMayor = ""
        for llave in dict.keys():
            if dict[llave] > mayor:
                mayor = dict[llave]
                llaveMayor = llave
        lt.addLast(lista,{llaveMayor: mayor})
        dict.pop(llaveMayor)
    return lista

def artistatecnica(catalog,datos):
    pass

def obrasPais(catalog,info,lista):
   for i in (lt.getElement(lista, 1)).keys():
       pais = i
   listaFinal = lt.newList()
   for obra in lt.iterator(catalog["obras"]):
        condicion = False
        for id in obra["ConstituentID"].split(", "):
            id = id.replace("[","")
            id = id.replace("]","")
            if info[id]["Nacionalidad"] == pais:
                condicion = True
        if condicion: 
            formatoObra =  {"Titulo":obra["Title"] ,"Artistas":info[id]["Nombre"],
            "Fecha":obra["Date"],"Medio":obra["Medium"],
            "Dimensiones":obra["Dimensions"]} 
            lt.addLast(listaFinal,formatoObra)

   return listaFinal


def ordenarObras(transporte):
    sub_list = lt.subList(transporte,1,lt.size(transporte))
    sub_list = sub_list.copy()
    sorted_list = sa.sort(sub_list, comparar_antigüedad)
    return sorted_list
   
