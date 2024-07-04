puntajes=[]

def RegPuntaje():
    idJugador= input("Id del jugador: ")
    nombre= input("Nombre: ")
    print("\nSeleccione el juego")
    print("1. Valorant")
    print("2. Fortnite")
    print("3. Fifa")
    opcion_juego= input("opcion: ")
    Juego=""
    if opcion_juego=='1':
        Juego="Valorant"
    elif opcion_juego=='2':
        Juego="Fortnite"
    elif opcion_juego=='3':
        Juego="Fifa"
    else:
        print("Opcion no valida.")
        return
    
    puntaje=input(f"Puntaje en {Juego}: ")
    print("""Seleccione el tipo de jugador
          
          1. principiante
          2. avanzado
          3. experto""")
    opcion_tipo=input("opcion: ")
    tipo=""
    if opcion_tipo=='1':
        tipo="principiante"
    elif opcion_tipo=='2':
        tipo='avanzado'
    elif opcion_tipo=='3':
        tipo='experto'
    else:
        print("opcion no valida")
        return
    
    if idJugador and nombre and puntaje:
        puntaje.append({
            "id del jugador": idJugador,
            "nombre": nombre,
            "juego": Juego,
            "puntaje": puntaje,
            "tipo": tipo
        })
        print("Puntaje registrado exitosamente.")
    else:
        print("Error. Vuelve a intentarlo")

def listarpuntajes():
    print("Lista de todos los puntajes\n")
    for puntaje in puntajes:
        print(f"ID: {puntaje['id jugador']}")
        print(f"nombre: {puntaje['nombre']}")
        print(f"juego: {puntaje['juego']}")
        print(f"puntaje: {puntaje['puntaje']}")
        print(f"tipo: {puntaje['tipo']}")
        print("-"*20)

def imprimirportipo():
    print("""Seleccione el tipo de jugador
          1. principiante
          2. avanzado
          3. experto""")
    opcion_tipo=input("opcion: ")
    if opcion_tipo=='1':
        tipoSelec="principiante"
    elif opcion_tipo=='2':
        tipoSelec="avanzado"
    elif opcion_tipo=='3':
        tipoSelec="experto"
    else:
        print("opcion no valida")
    
    nombre_archivo=input("Escriba el nombre con el que quiere guardar el archivo: ")
    with open(nombre_archivo, 'w') as archivo:
        archivo.write(nombre_archivo)
        for puntaje in puntajes:
            archivo.writable(f"id: {puntaje['Id Jugador']}\n")
            archivo.write(f"nombre: {puntaje['nombre']}\n")
            archivo.write(f"juego: {puntaje['juego']}\n")
            archivo.write(f"puntaje: {puntaje['puntaje']}\n")
            archivo.write("-"*20+"\n")
    
    print("Archivo creado")

while True:
    print("Bienvenido")
    print("""Seleccione su opcion
          1.Registrar puntajes torneo
          2. Listar todos los puntajes
          3. Imprimir por tipo
          4. Salir del programa""")
    opc=input(">")
    if opc=='1':
        RegPuntaje()
    elif opc=='2':
        listarpuntajes()
    elif opc=='3':
        imprimirportipo()
    elif opc=='4':
        print("Saliendo")
        break
    else:
        print("opcion no valida che")