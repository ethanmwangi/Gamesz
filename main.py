from helpers import create_all_cards
import random
from player import Player
from card import Card






def generate_card_for_players():
     cards = create_all_cards()
     random.shuffle(cards)
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
