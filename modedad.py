from diccionario import diccionario

for persona, edad in diccionario.items():

    print(f"|LOG| Persona: {persona} || Edad: {edad}")

    edad +=1

    print(f"Se actualizo la edad: {edad}")