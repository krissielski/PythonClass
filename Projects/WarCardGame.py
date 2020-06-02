### Python Class Project:  War, the card game
import random

number_of_decks   = 1
number_of_players = 2

suits = ( 'D', 'H', 'S', 'C' )
ranks = ( '2','3','4','5','6','7','8','9','T','J','Q','K','A' )


###################################################################
class Card:
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return str(self.rank) + str(self.suit) 

    
###################################################################
class Deck:

    def __init__(self):

        self.mydeck = []

        for deck in range( number_of_decks ):
            for suit in suits:
                for rank in ranks:
                    self.mydeck.append( Card(suit,rank) )

    def Shuffle(self):
        random.shuffle( self.mydeck )


    def Draw(self):
        self.mydeck.pop(0)


    def __len__(self):
       return len(self.mydeck)
    
    def __str__(self):
        s = ""
        for card in self.mydeck:
            s += str(card) + " "
        return s



###################################################################
class Hand:

    def __init__(self):

        pass

    def AddCard(self,card):
        pass

    def GetCard(self):
        pass


    def __len__(self):
        pass

    def __str__(self):
        pass


###################################################################
class Game:


    def __init__(self):

        self.deck = Deck()


    def Play(self):

        print( str(self.deck)  )

        self.deck.Shuffle()

        print( str(self.deck)  )


        for i in range( len(self.deck) ):
            self.deck.Draw()
            print( str(self.deck)  )




################
####  MAIN  ####
################

def main():
    print("In Main!")
    
    #...Do Something...

    game = Game()

    game.Play()



 #   deck = Deck()

 #   print(deck)


    print("Done!")


if __name__ == '__main__':
    main()


