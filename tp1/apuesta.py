import random
while True:
    try:
        conta_g=0
        conta_p=0
        seguir = "S"
        while seguir == "S":
            num1 = random.randint(1,100)
            num2 = random.randint(1,100)
            while num1 == num2 :
                num1 = random.randint(1,100)
                num2 = random.randint(1,100)
            else:
                print("Reglas: Se generaron 2 numeros enteros aleatorios, si elige el valor mayor gana")
                apuesta = int(input("Ingrese 1 si apuesta por el valor 1, o ingrese 2 si apuesta por el valor 2: "))
                print("numero 1: ", num1)
                print("numero 2: ", num2)
                if num1>num2 and apuesta == 1:
                    print("ha GANADO la apuesta :)")
                    conta_g = conta_g + 1
                elif num1<num2 and apuesta==1:
                    conta_p= conta_p +1
                    print("ha PERDIDO la apuesta :(")
                elif num1>num2 and apuesta==2:
                    conta_p= conta_p + 1 
                    print("ha PERDIDO la apuesta :(")
                elif num1<num2 and apuesta==2:
                    conta_g = conta_g + 1
                    print("ha GANADO la apuesta :(")
                seguir = str.upper(input("desea seguir jugando? S/N"))
        else:
            print("has ganado", conta_g, "veces!")
        break
    except ValueError:
        print("valor no permitido")


