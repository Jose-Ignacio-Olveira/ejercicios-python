import random

def elegir_numeros_distintos():
    while True:
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        if num1 != num2:
            return num1, num2

def obtener_apuesta():
    while True:
        apuesta = input("Elija su apuesta (1 o 2): ")
        if apuesta in ['1', '2']:
            return int(apuesta)
        else:
            print("Por favor, ingrese un valor válido (1 o 2).")

def jugar():
    partidas_ganadas = 0
    partidas_perdidas = 0

    while True:
        num1, num2 = elegir_numeros_distintos()
        
        apuesta = obtener_apuesta()
        print("Los números eran: {} y {}".format(num1, num2))
        
        if (apuesta == 1 and num1 > num2) or (apuesta == 2 and num2 > num1):
            print("¡GANASTE! :D")
            partidas_ganadas += 1
        else:
            print("PERDISTE. :(")
            partidas_perdidas += 1
        
        continuar = input("¿Queres jugar otra vez? (s/n): ").lower()
        if continuar != 's':
            print(f"Partidas ganadas: {partidas_ganadas}")
            print(f"Partidas perdidas: {partidas_perdidas}")
            break

if __name__ == "__main__":
    jugar()