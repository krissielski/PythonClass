### Python Class Project:  War, the card game


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
        return str(self.suit) + str(self.rank) 

    
###################################################################
class Deck:

    def __init__(self):

        self.mydeck = []

        for deck in range( number_of_decks ):
            for suit in suits:
                for rank in ranks:
                    self.mydeck.append( Card(suit,rank) )


    def shuffle(self):
        pass

    def draw(self):
        pass

    
    def __str__(self):
        s = ""
        for card in self.mydeck:
            s += str(card) + " "
        return s



###################################################################
class Hand:

    pass

###################################################################
class Game:

    pass


################
####  MAIN  ####
################

def main():
    print("In Main!")
    
    #...Do Something...

    deck = Deck()

    print(deck)


    print("Done!")


if __name__ == '__main__':
    main()


