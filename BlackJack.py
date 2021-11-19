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

