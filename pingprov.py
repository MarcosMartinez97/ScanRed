#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 13:25:37 2022

@author: alumnotd


"""
import os,argparse,platform
#No he hecho nada con la opción verbose
#Sólo se cambia el último punto de la dirección ip
def escanearIp24(ip,verbose):
    comando=""
    if platform.system() == "Linux":
        comando="ping -c 1"
    elif platform.system() == "Windows":
        comando="ping -n 1"
    listaip = ip.split(".")
    listaip = listaip[:-1] #Eliminamos el último punto de la ip ya que es la que va a variar
    ip24 =""
    for i in listaip:
        ip24+=str(i)+"."#Se recorre los elemontos de la lista para convetirlo en un único dato junto 
    listaips=[] #Esta va a ser la lista con los hosts que respondan
    for i in range(1,255):
        response = os.system(comando+" "+ip24+str(i))
        if response==0:
            listaips.append(ip24+str(i))
    return listaips


#Cambiar los dos últimos puntos de la dirección ip
def escanearIp16(ip,verbose):
    comando=""
    if platform.system() == "Linux":
        comando="ping -c 1"
    elif platform.system() == "Windows":
        comando="ping -n 1"
    listaip = ip.split(".")
    listaip = listaip[:-2]
    ip16=""
    for i in listaip:
        ip16+=str(i)+"."
    listaips=[]
    for i in range(1,255):
        for j in range(1,255):
            response = os.system(comando+" "+ip16+str(i)+"."+str(j))
            if response == 0:
                listaips.append(ip16+str(i)+"."+str(j))
    return listaips
    
#Cambiar todos los puntos menos el primero de la dirección ip
def escanearIp8(ip,verbose):
    comando=""
    if platform.system() == "Linux":
        comando="ping -c 1"
    elif platform.system() == "Windows":
        comando="ping -n 1"
    listaip = ip.split(".")
    ip8=listaip[0]
    listaips=[]
    for i in range(1,255):
        for j in range(1,255):
            for z in range(1,225):
                response = os.system(comando+" "+ip8+str(i)+"."+str(j)+"."+str(z))
                if response ==0:
                    listaips.append(ip8+str(i)+"."+str(j)+"."+str(z))
    return listaips

#Comprueba que la ip viene en formato 0.0.0.0 si es así devuelve true
def comprobarIp(ip):
    bien = False
    ip = ip.split(".")
    if len(ip) == 4:
        bien = True
    return bien

#Main

parser=argparse.ArgumentParser(description='recibe una dirección ip y hace un ping a la red, devuelve los hosts que respondan')
parser.add_argument("-t",dest="target_ip",help="direccion ip del objetivo",required=True)
parser.add_argument("-v",dest="verbose",action="store_true",help="muestra todos los ping que se van haciendo")
params=parser.parse_args()
mascara = params.target_ip.split("/")
if len(mascara)==2: #Se comprueba que la ip lleva máscara
    if comprobarIp(mascara[0]):
        if mascara[1] =="24":
            print("La lista de hosts que han respondido son:")
            for i in escanearIp24(mascara[0],params.verbose):
                print(i)
        elif mascara[1] == "16":
            print("La lista de hosts que han respondido son:")
            for i in escanearIp16(mascara[0],params.verbose):
                print(i)
        elif mascara[1] == "8":
            print("La lista de hosts que han respondido son:")
            for i in escanearIp8(mascara[0],params.verbose):
                print(i)
        else:
            print("La máscara de red es dinámica")
            print("Prueba con /24,/16 o /8")
    else:
        print("Tienes que poner una dirección ip válida")
        print("El formato es 0.0.0.0")
else:
    print("Error, no has puesto máscara de red")
