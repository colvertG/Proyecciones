#!/usr/bin/env python
# -*- coding: utf-8 -*-
def main():
    import math
    lista_fi=[]
    lista_la=[]
    lista_x=[]
    lista_y=[]
    r=6371
    pis=3.14159265
    with open('puntos.txt','r') as archivo:
        lineas=archivo.read().splitlines()
        lineas.pop(0)
        for elemento in lineas:
            linea=elemento.split(',')
            lista_la.append(float(linea[1]))
            lista_fi.append(float(linea[2]))
    for elemento2 in lista_la:
        x=r*elemento2*math.cos(math.radians(36))
        lista_x.append(x)
    for elemento3 in lista_fi:
        y=r*elemento3
        lista_y.append(y)

    f = open ('proyectadas.txt','a')
    for elemento5,elemento6 in zip(lista_x,lista_y):
        f.write('%s \t' %elemento5)
        f.write('%s \n' % elemento6)
    f.close()
main()