def mostrarAnfiteatro(anfiteatro):
    for i in range (len(anfiteatro)):
        for j in range (len(anfiteatro)):
            print (f"|{anfiteatro[i][j]}|", end = "")
            if (j == 9):
                print(f"  FILA {i+1}")
            
    print()
    for i in range (len(anfiteatro)):
        print (f"|{i+1}|", end="")
    print("\n")

def asientosDisponibles(anfiteatro, asientos_disponibles):
    for i in range (len(anfiteatro)):
        for j in range (len(anfiteatro)):
            if (anfiteatro[i][j] == "X"):
                asientos_disponibles = asientos_disponibles - 1
            
    return asientos_disponibles

def elegirAsiento(anfiteatro, asientos_disponibles):

    while (True):
        try:
            cantAsientos = int(input("Cuanto asientos quiere comprar?: "))
            if (cantAsientos < 1):
                raise ValueError("Debe comprar mas de un asiento")
            if (cantAsientos > asientos_disponibles):
                raise ValueError(f"Solo hay {asientos_disponibles} asientos disponibles")
            break
        except ValueError as error:
            print(f"Error: {error}.")
        
    while (cantAsientos != 0):
        while (True):
            try:
                fila = int(input("En que fila quiere estar? (1 a 10): "))
                if (fila < 1 or fila > 10):
                    raise ValueError("De fila 1 a 10")
                break
            except ValueError as error:
                print(f"Error: {error}.")

        while (True):
            try:
                columna = int(input(f"En asiento de la fila {fila} quiere sentarse? (1 a 10): "))
                if (columna < 1 or columna > 10):
                    raise ValueError("De asiento 1 a 10")
                break
            except ValueError as error:
                print(f"Error: {error}.")

        if (anfiteatro[fila-1][columna-1] == "L"):
            anfiteatro[fila-1][columna-1] = "X"
            cantAsientos = cantAsientos - 1
        
        else:
            print ("Asiento no disponible, elija otro")

        
def cambiarAsiento (anfiteatro, fila, columna):
    if (anfiteatro[fila-1][columna-1] == "L"):
        anfiteatro[fila-1][columna-1] = "X"
    
    else:
        print ("Asiento no disponible, elija otro")
        elegirAsiento(anfiteatro)

anfiteatro = [
    ["L", "L", "L", "L", "L", "L", "L", "L", "L", "L"],
    ["L", "L", "L", "L", "L", "L", "L", "L", "L", "L"],
    ["L", "L", "L", "L", "L", "L", "L", "L", "L", "L"],
    ["L", "L", "L", "L", "L", "L", "L", "L", "L", "L"],
    ["L", "L", "L", "L", "L", "L", "L", "L", "L", "L"],
    ["L", "L", "L", "L", "L", "L", "L", "L", "L", "L"],
    ["L", "L", "L", "L", "L", "L", "L", "L", "L", "L"],
    ["L", "L", "L", "L", "L", "L", "L", "L", "L", "L"],
    ["L", "L", "L", "L", "L", "L", "L", "L", "L", "L"],
    ["L", "L", "L", "L", "L", "L", "L", "L", "L", "L"]
]

asientos_disponibles = 100
while True:
    mostrarAnfiteatro(anfiteatro)
    asientos_disponibles = asientosDisponibles(anfiteatro, asientos_disponibles)

    if (asientos_disponibles != 0):
        elegirAsiento(anfiteatro, asientos_disponibles)
        mostrarAnfiteatro(anfiteatro)
    else:
        print ("No hay asientos disponibles")
        break

    try:
        seguir = input("Quiere comprar otro asiento? (si/no): ")
        if (seguir == "no"):
            break
        elif (seguir == "si"):
            continue
        else:
            raise ValueError("Debe escribir si o no")
    except ValueError as error:
        print(f"Error: {error}.")
    