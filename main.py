from helpers import create_all_cards
import random
from player import Player
from card import Card


def generate_card_for_players():
     cards = create_all_cards()
     random.shuffle(cards)
     return cards[0:7], cards[7:14], cards[14:21], cards[21:28]

a, b, c, d = generate_card_for_players()
player_a= Player("Player A", a)
player_b= Player("Player B", b)
player_c= Player("Player C", c)
player_d= Player("Player D", d)

print([str(card) for card in player_a.cards])
print([str(card) for card in player_b.cards])
print([str(card) for card in player_c.cards])
print([str(card) for card in player_d.cards])
