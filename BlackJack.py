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
        
        print ("/nCarta #", i, ":")
        time.sleep (4)
        number = random.choice(cards)
        print("number")
        
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
            print("/n->Su puntuación total es de ", total, "puntos")
        
        if(total<21):
            deck.append(number)
            answer = 2
            while(answer==2):
                answer = input("1ª Opción -> Pedir otra carta  /n2ª Opción -> Visualizar sus cartas  /n3ª Opción -> Finalizar el turno")
                if (answer==1):
                    i += 1
                elif (answer==2):
                    print("/n-> Las cartas son:", deck)
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
def PlayerName(playersnumber):
    for i in range (playersnumber):
        print("Introduzca aquí el nombre del Jugador", i+1)
        name = raw_imput()
        playersname.append(name)
        print ("-")*50

        
        