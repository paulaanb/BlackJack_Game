#Importamos la libreria
from random import choice, sample, shuffle

#Establecemos la bliblioteca donde se encuentra la lista de las cartas
cartas = {
    chr(0x1f0a1): 11,
    chr(0x1f0a2): 2,
    chr(0x1f0a3): 3,
    chr(0x1f0a4): 4,
    chr(0x1f0a5): 5,
    chr(0x1f0a6): 6,
    chr(0x1f0a7): 7,
    chr(0x1f0a8): 8,
    chr(0x1f0a9): 9,
    chr(0x1f0aa): 10,
    chr(0x1f0ab): 10,
    chr(0x1f0ad): 10,
    chr(0x1f0ae): 10,
}

#Base del juego
def game():
    print("Cartas: {}".format(" ".join(cartas.keys())))
    print("Puntos: {}".format(list(cartas.values())))       
#Establecemos el valor de cada carta
    print("Los valores de las cartas son los siguientes:")
    for carta, valor in cartas.items():
        print("La carta {} vale {} puntos.".format(carta, valor))
    
    print("Los valores del diccionario de cartas ordenados son:")
    for carta in sorted(cartas.keys()):
        print("La carta {} vale {} puntos.".format(carta, cartas[carta]))

#Le adjuntamos una lista al dicctionario de cartas
    print("\nEmpieza el juego de Black Jack")
    lista_cartas = list(cartas)
    
#Ahora nos disponemos a repartir las dos cartas al jugador y calcular su valor total
    print("\nUsted ha seleccionado la carta:", end=" ")
    carta = choice(lista_cartas)
    score = cartas[carta]
    print(carta, end=" ")
    carta = choice(lista_cartas)
    score += cartas[carta]
    print(carta, end=" ")
    print(" \n-> Su puntuación es de", score)

#Si el valor total de las anteriores cartas es menor a 21, podra seguir jugando
    stick= False
    while score < 21 and stick ==False:
        new_card = input("¿Quiere solicitar una carta nueva? 1) Si 2) No:")
        new_card = new_card.lower()
        if new_card == "1":
            carta = choice(lista_cartas)
            score += cartas[carta]
            print(carta, end=" ")
            print("\n-> Su puntuación es de", score)
        elif new_card == "2":
            stick= True
        else:
            print("Por favor, elija una respuesta permitida")
#Ahora es el turno de la banca
    main_banca = sample(lista_cartas, 2)
    score_banca = sum(cartas[carta] for carta in main_banca)
    print("La banca tiene: {} {} puntos y la suya es de {} puntos.".format(main_banca[0], main_banca[1], score_banca))

#La puntuación de mi juego depende del valor de las cartas repartidas.
    if score > 21:
        print("Lo lamento, su valor es mayor de 21, el ganandor ha sido la banca.")
    if score == score_banca:
        print("Ha habido un empate entre usted y la banca.")
    if score < 21 and score < score_banca:
        print("El ganador fue la banca.")
    if score < 21 and score > score_banca:
        print("¡Enhorabuena! Obtuvo más punto que la banca, ha ganado la partida.")
    if score == 21:
        print("¡Enhorabuena! Usted a logrado un Blackjack, ha ganado la partida.")
    play_again= input("¿Desea volver a jugar? 1)Si 2)No")
    play_again= play_again.lower()
    if play_again == "1":
        game()
    if play_again == "2":
        print("¡Nos vemos pronto!")

#Creamos la función para generar el juego
game()