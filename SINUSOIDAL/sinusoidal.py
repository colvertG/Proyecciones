#!/usr/bin/env python
# -*- coding: utf-8 -*-
def main():
    import math
    lista_fi=[]
    lista_la=[]
    lista_x=[]
    lista_y=[]
    la0=int(input("Ingresa el valor de la0"))
    with open('puntos.txt','r') as archivo:
        lineas=archivo.read().splitlines()
        lineas.pop(0)
        for elemento in lineas:
            linea=elemento.split(',')
            lista_la.append(float(linea[1]))
            lista_fi.append(float(linea[2]))
    for elemento2,elemento3 in zip(lista_la,lista_fi):
        x=(elemento2-la0)*(math.cos(math.radians(elemento3)))
        lista_x.append(x)
    for elemento4 in lista_fi:
        y=elemento4
        lista_y.append(y)

    f = open ('proyectadas.txt','a')
    for elemento5,elemento6 in zip(lista_x,lista_y):
        f.write('%s \t' %elemento5)
        f.write('%s \n' % elemento6)
    f.close()
main()
