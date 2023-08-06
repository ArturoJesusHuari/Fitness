from colorama import *
from os import system
import os
listaGruposMusculares = ['Brazos y antebrazos','Hombros','Pectorales','Espalda','Piernas','Glúteos','Abdominales']
def clear():
    if(os.name =='nt'):
        system('cls')
    elif(os.name =='posix'):
        system('clear')
def getGrupoMuscular():
    for index in range(0,len(listaGruposMusculares)):
        print('['+str(index)+'] '+listaGruposMusculares[index])
    return input('Grupo muscular:')
def printEjerciciosHoy(lista):
    clear()
    if(len(lista)>0):
        for ejerciciosHoy in lista:
            print(ejerciciosHoy)
    else:
        print('No hay ejercicios para hoy')
def printVerEstadisticas(lista):
    clear()
    for ejercicios in lista:
        print(ejercicios)
def printVerEjercicios(lista):
    clear()
    if(lista[0]!='' or lista[1]!='' or lista[2]!='' or lista[3]!='' or lista[4]!='' or lista[5]!='' or lista[6]!=''):
        for grup in range(0,7):
            if(lista[grup]!=''):
                print(Fore.RED + listaGruposMusculares[grup] + Fore.RESET)
                print(lista[grup])
    else:
        print('No se ha registrado ningun ejercicio')
def printBannerInicio():
    clear()
    inicioBanner="""
    ███████╗██╗████████╗███╗   ██╗███████╗███████╗███████╗
    ██╔════╝██║╚══██╔══╝████╗  ██║██╔════╝██╔════╝██╔════╝
    █████╗  ██║   ██║   ██╔██╗ ██║█████╗  ███████╗███████╗
    ██╔══╝  ██║   ██║   ██║╚██╗██║██╔══╝  ╚════██║╚════██║
    ██║     ██║   ██║   ██║ ╚████║███████╗███████║███████║
    ╚═╝     ╚═╝   ╚═╝   ╚═╝  ╚═══╝╚══════╝╚══════╝╚══════╝"""
    inicioOpciones = """
    [1].Ejercicios de hoy
    [2].Todos los ejercicios
    [3].Borrar ejercicio
    [4].Estadisticas
    [5].Salir"""
    print(Fore.CYAN + inicioBanner + Fore.RESET + inicioOpciones )