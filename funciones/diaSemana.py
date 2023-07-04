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