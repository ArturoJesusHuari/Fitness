import sqlite3
from datetime import datetime
from .diaSemana import numToDia
class DataBase:
    def __init__(self):
        now = datetime.now()
        self.format = now.strftime('%d/%m/%Y')
        self.createTableEjercicio="""CREATE TABLE ejercicio (
        id_ejercicio INT PRIMARY KEY,
        nombre VARCHAR(50),
        grupoMuscular INT,
        dia INT,
        descanso INT 
        );"""
        self.createTableSerie=""" 
        CREATE TABLE serie (
        id_serie INT PRIMARY KEY,
        fecha VARCHAR(50),
        id_ejercicio INT,
        repeticiones INT,
        peso INT,
        FOREIGN KEY (id_ejercicio) REFERENCES ejercicio(id_ejercicio)
        );"""
    def connect(self):
        self.conexion=sqlite3.connect("./src/bdFitness.db")
    def createTables(self):
        try:
            self.conexion.execute(self.createTableEjercicio)  
            self.conexion.execute(self.createTableSerie)                 
        except sqlite3.OperationalError:
            pass
    def closeConexion(self):                    
        self.conexion.close()
    def insertEjercicio(self,nombre,grupoMuscular,dia,descanso):
        _id = int(self.cantidadRegistros('ejercicio'))+1
        self.conexion.execute(f"INSERT INTO ejercicio(id_ejercicio, nombre,grupoMuscular,dia,descanso) values ({_id},'{nombre}',{grupoMuscular},{dia},{descanso})")
        self.conexion.commit()
    def insertSerie(self,id_ejercicio,repeticiones,peso):
        _id = int(self.cantidadRegistros('serie'))+1
        self.conexion.execute(f"INSERT INTO serie(id_serie, fecha, id_ejercicio, repeticiones, peso) values ({_id},'{self.format}','{id_ejercicio}',{repeticiones},{peso})")
        self.conexion.commit()
    def updateDescansoEjercicio(self,newTime,id_ejercicio):
        self.conexion.execute(f"UPDATE ejercicio SET descanso = {newTime} WHERE id_ejercicio = {id_ejercicio}")
        self.conexion.commit()
    def deleteEjercicio(self,id_ejercicio):
        listaSeries = self.listSelect(f"SELECT id_serie FROM serie WHERE id_ejercicio = {id_ejercicio}")
        try:
            for serie in listaSeries:
                listaRepeticiones = self.listSelect(f"SELECT id_repeticiones FROM repeticiones WHERE id_serie = {serie[0]}")
                try:
                    for repeticion in listaRepeticiones:
                        self.deleteRepeticiones(repeticion[0])
                except:
                    pass
                self.deleteSerie(serie[0])
        except:
            pass
        self.conexion.execute(f"DELETE FROM ejercicio WHERE id_ejercicio = {id_ejercicio};")
        print('nn')
        self.actualizar('ejercicio')
    def deleteSerie(self,id_serie):
        self.conexion.execute(f"DELETE FROM serie WHERE id_ejercicio = {id_serie};")
        self.actualizar('serie')
    def actualizar(self,table):
        cursor = self.conexion.execute(f"SELECT id_{table} FROM {table}")
        idsTable = cursor.fetchall()
        cantidadRegistrosTable = self.cantidadRegistros(table)
        if(cantidadRegistrosTable >= 1):
            for index in range(0,self.cantidadRegistros(table)):
                if idsTable[index] != index+1:
                    self.conexion.execute(f"UPDATE {table} SET id_{table} = {index+1} WHERE id_{table} = {idsTable[index][0]};")
        self.conexion.commit()
    def listSelect(self,sentencia):
        cursor = self.conexion.execute(sentencia)
        return cursor.fetchall()
    def cantidadRegistros(self,table):
        cantidad = self.conexion.execute(f"SELECT COUNT(id_{table}) FROM {table}")
        return cantidad.fetchone()[0]
    def cantidadRegistrosCondicion(self,table,condicion):
        cantidad = self.conexion.execute(f"SELECT COUNT(id_{table}) FROM {table} WHERE {condicion}")
        return cantidad.fetchone()[0]
    def idsEjerciciosHoy(self,today):
        idsEjerciciosHoy=[]
        listEjerciciosHoy = self.listSelect(f"SELECT id_ejercicio FROM ejercicio WHERE dia={today}")
        for id_ejercicio in listEjerciciosHoy:
            idsEjerciciosHoy.append(int(id_ejercicio[0]))
        return idsEjerciciosHoy 
    def ejerciciosHoy(self,today):
        ejerciciosHoy=[]
        listEjerciciosHoy = self.listSelect(f"SELECT id_ejercicio,nombre FROM ejercicio WHERE dia={today}")
        for EjercicioHoy in listEjerciciosHoy:
            cantSeriesHoy = self.conexion.execute(f"SELECT COUNT(id_serie) FROM serie WHERE id_ejercicio = {str(EjercicioHoy[0])}").fetchone()[0]
            if(cantSeriesHoy>0):
                grupoText='['+str(EjercicioHoy[0])+'].'+str(EjercicioHoy[1])+'\t\t Series completadas: '+str(cantSeriesHoy)
            else:
                grupoText='['+str(EjercicioHoy[0])+'].'+str(EjercicioHoy[1]+'\t\t No iniciado')
            ejerciciosHoy.append(grupoText)
        return ejerciciosHoy 
    def allEjercicios(self):
        allEjercicios=[]
        for grupos in range(0,7):
            grupoText=''
            grupo = self.listSelect(f"SELECT id_ejercicio,nombre,dia FROM ejercicio WHERE grupoMuscular={grupos}")
            for ejercicios in grupo:
                if(grupo[0]==ejercicios):
                    grupoText+='['+str(ejercicios[0])+'].'+str(ejercicios[1])+'\t\t'+str(numToDia(ejercicios[2]))
                else:
                    grupoText+='\n['+str(ejercicios[0])+'].'+str(ejercicios[1])
            allEjercicios.append(grupoText)
        return allEjercicios