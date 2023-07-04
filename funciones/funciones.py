from colorama import *
from os import system
listaGruposMusculares = ['Brazos y antebrazos','Hombros','Pectorales','Espalda','Piernas','Glúteos','Abdominales']
def clear():
    system("cls")
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
def printVerEjercicios(lista):
    clear()
    if(len(lista)>0):
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
    [3].Estadisticas
    [4].Salir"""
    print(Fore.CYAN + inicioBanner + Fore.RESET + inicioOpciones )