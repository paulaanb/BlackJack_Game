#Importamos librerias
import random
import time

#Empezamos con las variables globales 
global cards
cards = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]

global gamersname
gamersname = []

#Establecemos las funciones
def CardTurn (name) :
    total = 0
    choice = 1
    i = 1
    deck = []
    print ("->Es el turno de ", name, ":")
    
    while (choice!= 0 and total<21) :
        number = 0
        naturalnumber = [2, 3, 4, 5, 6, 7, 8, 9, 10]
        
        print ("\nLa carta tiene un valor de ", i, ":")
        time.sleep (4)
        number = random.choice(cards)
        print(number)
        
#Empezamos a darle valores a las cartas "especiales"

        if (number=="A"):
            deck.append(number)
            print ("Ahora debe elegir el valor deseado de su 'A' entre 1 u 11")
            number = input()
            if (number!=1 or number!=11) :
                print("Usted eligió un número que no esta dentro de los 2 valores predeterminados, por lo tanto no puede seguir jugando.")
                return 0
                break
        
        elif (number=="J"):
            deck.append(number)
            number = 10
        elif (number=="Q"):
            deck.append(number)
            number = 10
        elif (number=="K"):
            deck.append(number)
            number = 10
            
        else:
            deck.append(number)
        
        
        total+= number
        time.sleep(2)
        if(i>1):
            print("\n->Su puntuación total es de ", total, "puntos")
        
        if(total<21):
            answer = 2
            while(answer==2):
                answer = input("1) Pedir otra carta  2) Visualizar sus cartas 3) Finalizar el turno")
                if (answer==1):
                    i += 1
                elif (answer==2):
                    print("\n-> Las cartas obtuvidas fueron:", deck)
                    time.sleep(3)
                else:
                    choice = 0
                    return total
        elif (total ==21):
            deck.append(number)
            print("¡Enhorabuena! Usted a conseguido hacer un BlackJack.")
            return total
        else:
            print("¡Otra vez será! Vuelva a intentarlo.")
            return 0

#Definimos los nombres de los jugadores
def playersname(playersnumber):
    for i in range (playersnumber):
        playersname = []
        name = input("Introduzca aquí el nombre del Jugador: ")
        playersname.append(name)

#Main
continuar = 1
while continuar != 0:
    print("Vamos a comenzar a jugar al BlackJack.")
    playersnumber= input("Número de jugadores: 1.")
 
if (playersnumber==1):
    print("Bienvenido, vamos a comenzar a jugar al BlackJack")
    time.sleep(4)
    print("Iniciamos a jugar.")
    time.sleep(2)
    print("El número total de jugadores es 1.")
    time.sleep(3)
    continuar = input("¿Desea volver a jugar? 1) Si 2) No")
    del playersname[:]