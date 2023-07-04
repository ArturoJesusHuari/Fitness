from funciones import *

db = DataBase()
db.connect()
db.createTables()
hoy = obtenerDiaSemanaHoy()
def inicioBanner():
    printBannerInicio()
    op = int(input("->"))
    if(op==1):
        ejerciciosHoy()
    elif(op==2):
        ejerciciosTodos()
    elif(op==4):
        db.closeConexion
        exit()
    else:
        inicioBanner()
def ejerciciosTodos():
    printVerEjercicios(db.allEjercicios())
    op = input("->")
    try:
        if(int(op) in range(1,db.cantidadRegistros('ejercicio')+1)):
            insertSerie(op)
    except:
        if(op == 'add'):
            db.insertEjercicio(input('Nombre:'),getGrupoMuscular(),obtenerDiaSemana(input('Día:')),input('Descanso(min):'))
        elif(op == 'back'):
            inicioBanner()
        else:
            ejerciciosTodos()
def ejerciciosHoy():
    listEjerciciosHoy=db.ejerciciosHoy(hoy)
    printEjerciciosHoy(listEjerciciosHoy)
    op = input("->")
    try:
        if(int(op) in db.idsEjerciciosHoy(hoy)):
            insertSerie(op)
    except:
        if(op == 'add'):
            db.insertEjercicio(input('Nombre:'),getGrupoMuscular(),hoy,input('Descanso(min):'))
        elif(op == 'back'):
            inicioBanner()
        else:
            ejerciciosHoy()
def insertSerie(op):
    clear()
    while True:
        reps = int(input('rep:'))
        peso = int(input('Kgs:'))
        db.insertSerie(op,reps,peso)
        if(input('continue? :')=='Y'):
            pass
        else:
            break
    ejerciciosHoy()
inicioBanner()
#db = DataBase()
#db.connect()
#db.createTables()
#db.insertEjercicio('Press militar',1,1,3)
#db.insertEjercicio('Press de banca',2,2,2)
#db.insertEjercicio('Curl de biseps',0,1,2)
#db.closeConexion()