while True:
    try:
        num1 = int(input("Ingrese el primer entero: "))
        num2 = int(input("Ingrese el segundo entero: "))

        suma = num1 + num2

        print("la suma de", num1,"y",num2, "es: ", suma)
        break

    except ValueError:
        print("solo se permiten numeros enteros")