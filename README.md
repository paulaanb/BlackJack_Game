# BlackJack_Game
Mi dirección de Github para este repositorio es el siguiente: [Github] (https://github.com/paulaanb/BlackJack_Game)
En este trabajo hemos creado un juego llamado blackjack, cuyo objetivo es intentar conseguir con la suma de tus cartas el valor 21, pudiendo acercarse a dicho número o pasarse, en cuyo caso se habrá perdido.
En este caso he creado tres códigos diferentes, a elegir el deseado. Hay un código que cuenta con 2 librerías , random y time, para seleccionar un número de carta al azar y para darle pausa al juego.
Para no hacer tres diagramas de flujo diferentes, me dispuse a hacer uno centralizado que englobase todo. Se puede ver a continuación:
<img width="769" alt="Captura de pantalla 2021-11-23 a las 16 49 37" src="https://user-images.githubusercontent.com/91721496/143057185-1d0e881f-dc5a-4d42-91aa-584fb631fe04.png">


Dicho esto, los códigos son los siguientes:

```
-Código 1(BlackJackGame):

#Importamos Libreria
from random import randint
from random import shuffle

#Definimos los valores de las cartas
def valores (val):
    if val=='A':
        return 1
    elif val=='2':
        return 2
    elif val=='3':
        return 3
    elif val=='4':
        return 4
    elif val=='5':
        return 5
    elif val=='6':
        return 6
    elif val=='7':
        return 7
    elif val=='8':
        return 8
    elif val=='9':
        return 9
    elif val=='J'or val=='K'or val=='Q':
       return 10

#Definimos los valores 'especiales'
def valoresEspeciales (lista):
        if dimensionLista(lista)<48:
            if lista==[]:
                lista.append('A')
                return valoresEspeciales(lista)
            elif lista[-1]=='A':
                lista.append('2')
                return valoresEspeciales(lista)
            elif lista[-1]=='9':
                lista.append('J')
                return valoresEspeciales(lista)
            elif lista[-1]=='J':
                lista.append('Q')
                return valoresEspeciales(lista)
            elif lista[-1]=='Q':
                lista.append('K')
                return valoresEspeciales(lista)
            elif lista[-1]=='K':
                lista.append('A')
                return valoresEspeciales(lista)
            elif int(lista[-1])<9:
                lista.append(str(int(lista[-1])+1))
                return valoresEspeciales(lista)
        else:
            return lista
            
#Definimos la dimension de la lista            
def dimensionLista(lista):
    if lista==[]:
        return 0
    else:
        return 1 + dimensionLista(lista[1:])
    
#Definimos la cantidad de cartas a repartir
def repartirCartas(num,lista,s):
        if num==21:
            return num
        if num==-1:
            return -1 
        elif num<21:
            print ("\nVamos a comenzar a jugar al Blackjack, por favor, inserte 'Si' para poder recibir cartas y 'No' para finalizar el juego.")
            if input()== "No":
                print ("\nAhora es el turno del CPU")
                if turnoCPU(0,num,lista)==0:
                    return -1
                else:
                    return num
            else:
                shuffle(lista)
                if lista[0]=='A':
                    if num+11>21:
                        print("\nSu nueva carta es: ")
                        print(lista[0])
                        print("\nSu número total de cartas es:")
                        print(num+valores(lista[0]))
                        return repartirCartas(num+valores(lista[0]),lista,s)
                    else:
                        print("\nSu nueva carta es: ")
                        print (lista[0])
                        print ("\nSu número total de cartas es:")
                        print (num+valores(lista[0]))
                        return repartirCartas(num+11,lista,s+1)
                print("\Su nueva carta es: ")
                print (lista[0])
                print ("\nSu número total de cartas:")
                print (num+valores(lista[0]))
                return repartirCartas(num+valores(lista[0]),lista,s)
        elif num>21 and num==0:
            return -1
        elif num>21 and num>0:
            print ("\nEl total de cartas reducidas genera una nueva suma de cartas de = ",num-10)
            return repartirCartas(num-10,lista,s-1)
 
 #Definimos el turno del CPU            
def turnoCPU(num,user,lista):
        if (num<21)&(num>user):
            print("¡Enhorabuena! Obtuvo más punto que la banca, ha ganado la partida.")
        if num==21:
            print("¡Enhorabuena! Usted a logrado un Blackjack, ha ganado la partida.")
        if num > 21:
            print("Lo lamento, su valor es mayor de 21, el ganandor ha sido la banca.")
        if num<21:
            shuffle(lista)
            print("\nSu nueva carta es: ")
            print(lista[0])
            print ("Su número total de cartas es:")
            print (num+valores(lista[0]))
            return turnoCPU(num+valores(lista[0]),user,lista)

#Establecemos los comandos y final del juego
def main():
    print ("Juego BlackJack")

    if repartirCartas(0,valoresEspeciales(lista=[]),0)==(-1):
        print("\n¡Ha perdido!¡Inténtelo otra vez!")
    else:
        print("\n¡Enhorabuena!¡Ha ganado!")
if __name__ == "__main__":
    main()


-Código 2(SimpleBlackJack):

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


-Código 3(BlackJack):

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

