import random
numero=random.randint(1,100)
# print(número)
nombre_jugador=input("Ingresa tu nombre por favor: ")

intentos=0

while True:
    intento=int(input("¡Juguemos! Adivina el número entre 1 y 100 (presiona 0 para rendirte): "))

    if intento==0:
        print("Lo siento", nombre_jugador, "No lo lograste a pesar de tratar", intentos, "veces. ¡Más suerte para la próxima!")
        break
    intentos=intentos+1
    if intento==numero:
        print("¡Felicidades", nombre_jugador, "ganaste el juego!. Adivinaste el número en", intentos,"intentos.")
        break
    distancia=abs(numero-intento)
    if distancia<=5:
        print("Lo siento", nombre_jugador, "ese no es el número, pero estás a una distancia igual o menor a 5.")
    elif distancia>5 and distancia<=10:
        print("Lo siento", nombre_jugador, "ese no es el número, pero estás a una distancia mayor a 5 y menor o igual que 10.")
    elif distancia>10 and distancia<=20:
        print("Lo siento", nombre_jugador, "ese no es el número pero estás a una distancia mayor que 10 y menor o igual a 20.")
    else:
        print("Lo siento", nombre_jugador, "ese no es el número, estás a una distancia mayor que 20.")