### Python Class Project:  War, the card game
import random

number_of_decks   = 1
number_of_players = 2

suits = ( 'D', 'H') #, 'S', 'C' )
ranks = ( '2','3','4','5','6','7','8','9','T','J','Q','K','A' )

#rank to integer
r2i = { '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':11, 'Q':12, 'K':13, 'A':14 }



###################################################################
class Card:
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return str(self.rank) + str(self.suit) 

    def GetVal(self):
        return(  r2i[self.rank] )




    
###################################################################
class Deck:

    def __init__(self, num_decks):

        self.mydeck = []

        for deck in range( num_decks ):
            for suit in suits:
                for rank in ranks:
                    self.mydeck.append( Card(suit,rank) )

    def Shuffle(self):
        random.shuffle( self.mydeck )


    def Draw(self):
        return self.mydeck.pop(0)


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
        self.myhand = []


    def AddCard(self,card):
        self.myhand.append(card)

    def GetCard(self):
        return self.myhand.pop(0)

    def GetNumCards(self):
        return len( self.myhand)
        
    def __len__(self):
        return len( self.myhand)

    def __str__(self):
        s = ""
        for card in self.myhand:
            s += str(card) + " "
        return s


###################################################################
class Game:


    def __init__(self):

        self.deck = Deck( number_of_decks )

        # #DO NOT DO THIS
        # self.player1 = Hand()
        # self.player2 = Hand()

        self.players = []

        for i in range(number_of_players ):
            self.players.append( Hand() )





    def Play(self):

        print( str(self.deck)  )
        self.deck.Shuffle()
        print( str(self.deck)  )


        #Deal to players
        for i in range(  int( len(self.deck) / number_of_players)  ):
            for j in range (number_of_players):
                self.players[j].AddCard(  self.deck.Draw()   )

        #Debug output
        for i in range(number_of_players):
            print(i,"=",str(self.players[i]) )


        # for i in range( len(self.deck) ):
        #     self.deck.Draw()
        #     print( str(self.deck)  )


        turn = 1

        while( True ):


            print("*********************************")
            print("Turn ",turn)

            p0 = self.players[0].GetCard()
            p1 = self.players[1].GetCard()

            print( p0.rank, p1.rank )
            print( p0.GetVal(), p1.GetVal() )


            if( p0.GetVal() > p1.GetVal() ):
                #P0 Wins
                print(str(p0),str(p1),  "   P0 Wins")

                self.players[0].AddCard(p0)
                self.players[0].AddCard(p1)


            elif( p0.GetVal() < p1.GetVal() ):
                #P1 Wins
                print(str(p0),str(p1),  "   P1 Wins")

                self.players[1].AddCard(p0)
                self.players[1].AddCard(p1)

            else:
                #Tie
                print(str(p0),str(p1),  "   TIE!!")


            #Debug output
            for i in range(number_of_players):
                print(i,"=",str(self.players[i]) )


            input("Hit Enter....")

            turn += 1







################
####  MAIN  ####
################

def main():
    print("In Main!")

    game = Game()
    game.Play()

    # HAND test
    # hand = Hand()
    # card = Card('h','2')
    # print("++++++++++++++++++++++")
    # print(">>>", str( hand) )
    # hand.AddCard(card)
    # print( ">>>",str( hand) )
    # hand.GetCard()
    # print( ">>>",str( hand) )



    print("Done!")


if __name__ == '__main__':
    main()


