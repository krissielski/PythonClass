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
class War:

    def __init__(self):
        self.mywar = []

    def AddCard(self,card):
        self.mywar.append(card)

    def GetCard(self):
        return self.mywar.pop(0)

    def SeeCard(self):
        return self.mywar[-1]      
  
    def GetNumCards(self):
        return len( self.mywar)
        
    def __len__(self):
        return len( self.mywar)

    def __str__(self):
        s = ""
        for card in self.mywar:
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

            cards = {}
            cards['hand'] = Hand()
            cards['war']  = War()
            self.players.append( cards  )

            #self.players
            #   player number
            #       ['hand']
            #       ['war']


    def Play(self):

        print( str(self.deck)  )
        self.deck.Shuffle()
        print( str(self.deck)  )


        #Deal to players
        for i in range(  int( len(self.deck) / number_of_players)  ):
            for j in range (number_of_players):
                #self.players[j].AddCard(  self.deck.Draw()   ) #Not anymore

                self.players[j]['hand'].AddCard( self.deck.Draw() )



        #Debug output
        for i in range(number_of_players):
            print(i,"=",str(self.players[i]['hand']) )


        # for i in range( len(self.deck) ):
        #     self.deck.Draw()
        #     print( str(self.deck)  )


        turn = 1

        while( True ):


            print("*********************************")
            print("Turn ",turn)

            #Was
            #p0 = self.players[0].GetCard()
            #p1 = self.players[1].GetCard()

            #Is now
            #Move card from Hand to War for each player
            for i in range(number_of_players):
                self.players[i]['war'].AddCard(  self.players[i]['hand'].GetCard() ) 


            #Debug
            print( self.players[0]['war'].SeeCard() , self.players[1]['war'].SeeCard() )

            print("0 = ", self.players[0]['war'] )
            print("1 = ", self.players[1]['war'] )



            #Pull out card to make if statements easier
            p0 = self.players[0]['war'].SeeCard()
            p1 = self.players[1]['war'].SeeCard()
  


            if( p0.GetVal() > p1.GetVal() ):
                #P0 Wins
                print(str(p0),str(p1),  "   P0 Wins")

                self.players[0]['hand'].AddCard(  self.players[0]['war'].GetCard()  )
                self.players[0]['hand'].AddCard(  self.players[1]['war'].GetCard()  )


            elif( p0.GetVal() < p1.GetVal() ):
                #P1 Wins
                print(str(p0),str(p1),  "   P1 Wins")

                self.players[1]['hand'].AddCard(  self.players[0]['war'].GetCard()  )
                self.players[1]['hand'].AddCard(  self.players[1]['war'].GetCard()  )

            else:
                #Tie
                print(str(p0),str(p1),  "   TIE!!")
                #add more cards

                # Next:
                # while( not someone Wins):

                #     if 0 > 1
                #     elif 0<1
                #     else tie 





            #Debug output
            for i in range(number_of_players):
                print(i,"=",str(self.players[i]['hand']) )


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


