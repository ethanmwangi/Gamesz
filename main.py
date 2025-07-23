from helpers import create_all_cards
import random

class Card:
    def __init__(self, color="black", number=0, special_ability=None):
        self.color = color
        self.number = number
        self.special_ability = special_ability

    def __str__(self):
        return f"{self.color} {self.number} {self.special_ability}"



class Player:
    def __init__(self, name, cards):
       self.name = name
       self.cards 


def generate_card_for_players():
     cards = random.shuffle(create_all_cards)
     return cards[0:13], cards[13:26], cards[26:39], cards[39:52]

a, b, c, d = generate_card_for_players()
player_a= Player("Player A", a)
player_b= Player("Player B", b)
player_c= Player("Player C", c)
player_d= Player("Player D", d)

print(player_a.cards)
print(player_b.cards)
print(player_c.cards)
print(player_d.cards)
