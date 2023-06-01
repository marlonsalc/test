from datetime import datetime

months = {1: "Enero",
          2: "Febrero",
          3: "Marzo",
          4: "Abril",
          5: "Mayo",
          6: "Junio",
          7: "Julio",
          8: "Agosto",
          9: "Septiembre",
          10: "Octubre",
          11: "Noviembre",
          12: "Diciembre"}

def humanDate():
    now = datetime.now()
    return "El dia de hoy es {} de {} del año {}".format(now.day, months[now.month], now.year)

def computerTime():
    diaHumano = input("Ingrese el dia en formato humano (Ejemplo: 1 de Enero del año 2021): ")
    diaHumano = diaHumano.split(" ")
    dia = int(diaHumano[0])
    mes = list(months.keys())[list(months.values()).index(diaHumano[2])]
    anio = int(diaHumano[5])
    return datetime(anio, mes, dia)
