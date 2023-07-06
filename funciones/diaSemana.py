from datetime import datetime
def obtenerDiaSemanaHoy():
    today = datetime.today()
    return today.isoweekday()
def obtenerDiaSemana(dia):
    if(dia == 'Lunes'):
        return 1
    elif(dia == 'Martes'):
        return 2
    elif(dia == 'Miercoles'):
        return 3
    elif(dia == 'Jueves'):
        return 4
    elif(dia == 'Viernes'):
        return 5
    elif(dia == 'Sabado'):
        return 6
    elif(dia == 'Domingo'):
        return 7
    else:
        return 0
def numToDia(_int):
    if(_int==1):
        return 'Lunes'
    elif(_int==2):
        return 'Martes'
    elif(_int==3):
        return 'Miercoles'
    elif(_int==4):
        return 'Jueves'
    elif(_int==5):
        return 'Viernes'
    elif(_int==6):
        return 'Sabado'
    elif(_int==7):
        return 'Domingo'
    else:
        return 0