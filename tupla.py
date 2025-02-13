import datetime  
from datetime import date

luis = datetime.date.fromisoformat("1995-01-12")
mela = datetime.date.fromisoformat("1992-01-10")
leonor = datetime.date.fromisoformat("1972-01-05")
kenny = datetime.date.fromisoformat("2009-02-01")
betsy = datetime.date.fromisoformat("2002-08-13")
penultimo = date(1993, 6, 29)


creacion = list()
for x in range(3):

    creacion.append(input(f"Ingrese el valor {x}: "))

ultimo = datetime.date.fromisoformat(f"{creacion[0]}-{creacion[1]}-{creacion[2]}")

tupla = tuple([luis, mela, leonor, kenny, betsy, penultimo, ultimo])

print(tupla)
    
