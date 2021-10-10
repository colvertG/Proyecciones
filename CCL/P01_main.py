#!/usr/bin/env python
# -*- coding: utf-8 -*-
import csv
def main():
    import math
    n1=1
    lista_elipsoides = []
    lista_a=[]
    lista_b=[]
    lista_fi=[]
    lista_la=[]
    lista_x=[]
    lista_y=[]
    lista_ro=[]
    lista_teta=[]
    with open('C:/Users/HP/Dropbox/FI/6to semestre/Cartografia/Tema 4/CCL/elipsoides.csv','r') as archivo:
        lineas=archivo.read().splitlines()
        lineas.pop(0)
        for elemento in lineas:
            linea=elemento.split(',')
            lista_elipsoides.append(str(linea[0]))
            lista_a.append(float(linea[1]))
            lista_b.append(float(linea[2]))
    print("Escoje el elipsoide de referencia:")
    for el in lista_elipsoides:
        print(n1,":",el)
        n1=n1+1
    n_elipsoide=int(input())
    n_elipsoide2=n_elipsoide-1
    a=lista_a[n_elipsoide2]
    b=lista_b[n_elipsoide2]
    print ("a=",a)
    print ("b=",b)
    e2=(a**2-b**2)/(a**2)#e^2
    print ("e^2=",e2)
    e=(e2**(.5)) #e
    print ("e=",e)

    escala1=int(input("Ingrese la escala 1:"))

    escala=(1.0/escala1) #escala
    print ("Escala=",escala)
    fi1=float(input("Introduzca la latitud del primer paralelo tipo en grados decimanles"))#Paralelo tipo 1
    fi2=float(input("Introduzca la latitud del segundo paralelo tipo en grados decimanles"))#Paralelo tipo 2
    fi0=float(input("Introduzca el punto de origen en grados decimanles (latitud)"))#latitud de origen
    la0=float(input("Introduzca el punto de origen en grados decimanles (longitud)"))#longitud de origen


    m1=(math.cos(math.radians(fi1)))/(1-e2*(math.sin(math.radians(fi1)))**2)**(.5)
    m2=(math.cos(math.radians(fi2)))/(1-e2*(math.sin(math.radians(fi2)))**2)**(.5)
    print ("m1=",m1)
    print ("m2=",m2)

    t1=(math.tan(math.radians(45-fi1/2)))/(((1-e*math.sin(math.radians(fi1)))/(1+e*math.sin(math.radians(fi1))))**(e/2))
    t2=(math.tan(math.radians(45-fi2/2)))/(((1-e*math.sin(math.radians(fi2)))/(1+e*math.sin(math.radians(fi2))))**(e/2))
    t0=(math.tan(math.radians(45-fi0/2)))/(((1-e*math.sin(math.radians(fi0)))/(1+e*math.sin(math.radians(fi0))))**(e/2))
    print ("t1=",t1)
    print ("t2=",t2)
    print ("t0=",t0)

    n=(math.log(m1)-math.log(m2))/(math.log(t1)-math.log(t2))
    print("n=",n)
    F=(m1/(n*(t1**n)))
    print("F=",F)
    ro0=a*F*(t0**n)
    print("Ro0=",ro0)
    with open('C:/Users/HP/Dropbox/FI/6to semestre/Cartografia/Tema 4/CCL/volvanescsv.csv','r') as archivo2:
        lineas2=archivo2.read().splitlines()
        lineas2.pop(0)
        for elemento2 in lineas2:
            linea2=elemento2.split(',')
            lista_fi.append(float(linea2[0]))
            lista_la.append(float(linea2[1]))
    for elemento3 in lista_fi:
        tp=(math.tan(math.radians(45.0-elemento3/2.0)))/(((1-e*math.sin(math.radians(elemento3)))/(1+e*math.sin(math.radians(elemento3))))**(e/2.0))
        #print("tp=",tp)
        ro=a*F*(tp**n)
        lista_ro.append(ro)
        #print("Ro=",ro)
    for elemento4 in lista_la:
        teta=math.radians(n*(elemento4-la0))
        #print("teta=",teta)
        lista_teta.append(teta)
    for elemento5,elemento6 in  zip(lista_ro,lista_teta):
        x=elemento5*math.sin(elemento6)*escala
        #print("x=",x)
        lista_x.append(x)
        y=(ro0-elemento5*math.cos(elemento6))*escala
        lista_y.append(y)
        #print("y=",y)
    """m20=open('C:/Users/HP/Dropbox/FI/6to semestre/Cartografia/CCL/archivo1.csv','w')
    m20_c=csv.writer(m20)
    m20_c.writerow(lista_x)
    m20.close()"""
    f = open ('C:/Users/HP/Dropbox/FI/6to semestre/Cartografia/Tema 4/CCL/proyectadas.txt','a')
    for elemento6,elemento7 in zip(lista_x,lista_y):
        f.write('%s \t' %elemento6)
        f.write('%s \n' % elemento7)
    f.close()
main()
