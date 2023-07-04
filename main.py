from funciones import *
class Main:
    def __init__(self):
        self.db = DataBase()
        self.db.connect()
        self.db.createTables()
        self.hoy = obtenerDiaSemanaHoy()
    def inicioBanner(self):
        printBannerInicio()
        op = int(input("->"))
        if(op==1):
            self.ejerciciosHoy()
        elif(op==2):
            self.ejerciciosTodos()
        elif(op==4):
            self.db.closeConexion
            exit()
        else:
            self.inicioBanner()
    def ejerciciosTodos(self):
        printVerEjercicios(self.db.allEjercicios())
        op = input("->")
        try:
            if(int(op) in range(1,self.db.cantidadRegistros('ejercicio')+1)):
                self.insertSerie(op)
                self.ejerciciosTodos()
        except:
            if(op == 'add'):
                self.db.insertEjercicio(input('Nombre:'),getGrupoMuscular(),obtenerDiaSemana(input('Día:')),input('Descanso(min):'))
                self.ejerciciosTodos()
            elif(op == 'back'):
                self.inicioBanner()
            else:
                self.ejerciciosTodos()
    def ejerciciosHoy(self):
        listEjerciciosHoy=self.db.ejerciciosHoy(self.hoy)
        printEjerciciosHoy(listEjerciciosHoy)
        op = input("->")
        try:
            if(int(op) in self.db.idsEjerciciosHoy(self.hoy)):
                self.insertSerie(op)
                self.ejerciciosHoy()
        except:
            if(op == 'add'):
                self.db.insertEjercicio(input('Nombre:'),getGrupoMuscular(),self.hoy,input('Descanso(min):'))
                self.ejerciciosHoy()
            elif(op == 'back'):
                self.inicioBanner()
            else:
                self.ejerciciosHoy()
    def insertSerie(self,op):
        clear()
        while True:
            reps = int(input('rep:'))
            peso = int(input('Kgs:'))
            self.db.insertSerie(op,reps,peso)
            if(input('continue? :')=='Y'):
                pass
            else:
                break
def main():
    Main().inicioBanner()
if __name__ == '__main__':
    main()