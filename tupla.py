import datetime  

luis = datetime.date.fromisoformat("1995-01-12")
mela = datetime.date.fromisoformat("1992-01-10")
leonor = datetime.date.fromisoformat("1972-01-05")
kenny = datetime.date.fromisoformat("2009-02-01")
betsy = datetime.date.fromisoformat("2002-08-13")

tupla = tuple((luis, mela, leonor, kenny, betsy))

print(tupla)
