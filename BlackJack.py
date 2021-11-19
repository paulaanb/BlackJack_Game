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
def PlayersName(playersnumber):
    for i in range (playersnumber):
        print("Introduzca aquí el nombre del Jugador", i+1)
        name = raw_input()
        PlayersName.append(name)
        print ("-")*50
#Definimos el ganador
def Winner(J1, J2, name):
    time.sleep(3)
    if (J1>J2):
        print(name[0], " finalizó con un total de ", J1, " puntos.")
    elif (J2>J1):
        print(name[1], "finalizó con un total de ", J2, "puntos.")
    elif(J1==J2):
        print("¡Vaya! Hay un empate. Cada jugador tiene un total de ", J1, "puntos.")
    else: 
        print("Ninguno de los dos jugadores ha conseguido una victoria. Intentadlo otra vez.")

#Main
continuar = 1
while continuar != 0:
    print("Vamos a comenzar a jugar al BlackJack.")
    playersnumber = input("Número de Jugadores deseados: 1ª Opción -> 1 Jugador /n2ª Opción -> 2 Jugadores")
    PlayersName(playersnumber)
    
    if (playersnumber==1):
        print("Bienvenido, vamos a comenzar a jugar al BlackJack")
        time.sleep(4)
        print("Iniciamos a jugar.")
        time.sleep(2)
        J1= CardTurn(PlayersName[0])
        print("El número total de jugadores es 1.")
        time.sleep(3)
        continuar = input("¿Desea volver a jugar? 1) Si 2) No")
        del PlayersName[:]
    
    
    elif(playersnumber==2):
        print("Bienvenido, vamos a comenzar a jugar al BlackJack")
        time.sleep(4)
        print("El número total de jugadores es 2.")
        J1= 0
        J2= 0
        for i in range(playersnumber):
            print("Iniciamos a jugar.")
            time.sleep(2)
            if(i==0):
                J1= CardTurn(PlayersName[i])
                print("El turno a finalizado. Debe esperar a su oponente.")
                time.sleep(3)
            else:
                J2= CardTurn(PlayersName[i])
                print("Su turno ha finalizado.")
        time.sleep(2)
        print("Eligiendo al ganador...")
        
        players= {PlayersName[0]: J1, PlayersName[1]: J2}
        print("/nEL ganador ha sido el ")
        time.sleep(3)
        print(max(players, key=players.get), "con un total de ", max(players.values()))
        time.sleep(3)
        
        continuar = input("¿Desea volver a jugar? 1) Si 2) No")
        del PlayersName[:] 
    