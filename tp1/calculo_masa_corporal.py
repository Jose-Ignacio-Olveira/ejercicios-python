while True:
    try:
        peso = float(input("ingrese su peso: "))
        altura = float(input("ingrese su altura: "))

        masa = peso / (altura*altura)

        print("El indice de masa corporal (IMC) del usuario es de:", masa)
        break
    except ValueError:
        print("El valor ingresado no es valido. ")