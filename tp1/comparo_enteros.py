import random

# Genera un número aleatorio entre 1 y 10
numero_aleatorio = random.randint(1, 10)

while True:
    try:
        # Solicita un número al usuario
        numero_usuario = int(input("Por favor, introduce un número entero entre 1 y 10: "))

        # Compara el número del usuario con el número aleatorio
        if numero_usuario == numero_aleatorio:
            print(f"El número {numero_usuario} es igual al número generado ({numero_aleatorio}).")
        else:
            print(f"El número {numero_usuario} es distinto al número generado ({numero_aleatorio}).")
        
        if numero_usuario < numero_aleatorio:
            print(f"El número {numero_usuario} es menor que el número generado ({numero_aleatorio}).")
        elif numero_usuario > numero_aleatorio:
            print(f"El número {numero_usuario} es mayor que el número generado ({numero_aleatorio}).")

        if numero_usuario <= numero_aleatorio:
            print(f"El número {numero_usuario} es menor o igual que el número generado ({numero_aleatorio}).")
        if numero_usuario >= numero_aleatorio:
            print(f"El número {numero_usuario} es mayor o igual que el número generado ({numero_aleatorio}).")
        
        break  # Sale del bucle si se introduce un número válido

    except ValueError:
        # Captura el error si el usuario introduce un valor no convertible a entero
        print("Error: Por favor, introduce un número entero válido.")