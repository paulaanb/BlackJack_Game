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

#Base del juego
class BlackJack():
    def __init__(self):
        self.turn = []
        self.deckofcards = list(cards.key())
        self.dealer = []
    def giveCards(self, amount, bunch):
        for i in range(amount):
            shuffle(self.deckofcards)
            card = self.deckofcards.pop()
            bunch.append(card)
    def calculate(self, bunch):
        score = 0
        for i in range(len(bunch)):
            try:
                score += card[bunch[i]]
            except: 
                return print("Ha habido un error en el código")
        return score
    def begingame(self):
        print("¡Vamos a empezar a jugar al BlackJack! \n El dealer se dispone a darle sus cartas.")
        blackjack().giveCards(2, self.hand)
        blackjack().giveCards(1, self.dealer)
        print("Su mano en esta partida es:\n" + self.hand[0] + '' + self.hand[1] + "\nScore:" + str(blackjack().calculatehand(self.hand)) + "\nDealer:" + self.dealer[0] + "\nScore" + str(blackjack().calculatehand)))
        decision = input("Ahora debe elegir lo que desea hacer, si continuar la partida o plantarse (Stick/Continue):")
        if str(decision).lower()== "stick":
            blackjack().stick(self.hand)
        elif str(decision).lower() == "continue":
            blackjack().continue()
    def stick(self, bunch):
        shuffle(self.deckofcards)
        card= 