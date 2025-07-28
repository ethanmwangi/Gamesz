##Generate the Uno deck
import random
def buildDeck(): 
   deck = []
 #example card :Red 7 , Green 8
   Colours = ["Red", "Blue", "Green", "Yellow"]
   values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "Draw two", "Skip", "Reverse"]
   wilds = ["Wild", "Wild Draw Four"]
   for colour in Colours:
         for value in values:
              cardVal = " {} {}".format(colour, value)
              deck.append(cardVal)
              if value !=0:
                    deck.append(cardVal)
   for i in range(4):
        deck.append(wilds[0])
        deck.append(wilds[1])   
   
   return deck

#shuffles a list of items passed into it

def shuffleDeck(deck):
     for cardPos in range(len(deck)):
          randPos = random.randint(0,107)
          deck[cardPos], deck[randPos] = deck[randPos], deck[cardPos]
     return deck

#draw card fucntion
def drawCards(numCards):
     cardsDrawn = []
     for x in range(numCards):
          cardsDrawn.append(UnoDeck.pop(0))
     return cardsDrawn

def showHand(player, playerHand):
     print("player {}".format(player+1))
     print("Your Hand")
     print("-------------------")
     for card in playerHand:
          print(card)
     print("")

def canPlay(discarCard, playerHand):
     splitCard = discarCard.split('',-1)
     colour = splitCard[0]
     cardVallue = splitCard[1]

unoDeck = buildDeck() 
UnoDeck = shuffleDeck(unoDeck)
discards = []
print(unoDeck)
            

players = []
numPlayers = int(input("How many players ? "))
while numPlayers < 2 or numPlayers > 4:
     numPlayers = int(input("Invalid number of players. Please enter a number between 2 and 4: "))
for players in range(numPlayers):
    players.append(drawCards(5))

print(players)

playerTurn = 0
playerDirection = 1
playing = True
discards.append(UnoDeck.pop(0))  # Draw the first card to start the game
 
while playing:
     showHand(playerTurn, players[playerTurn])
     print("Card on top of discard pile : {}" .format(discards[-1]))

