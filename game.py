import random
from helpers import create_all_cards
from player import Player
from card import Card

class Game:
    def __init__(self, player_names):
        self.deck = create_all_cards()
        random.shuffle(self.deck)
        self.players = [Player(name, self.draw_cards(13)) for name in player_names]
        self.discard_pile = [self.deck.pop()]
        self.current_player = 0
        self.direction = 1  # 1 for clockwise, -1 for counterclockwise

    def draw_cards(self, num):
        return [self.deck.pop() for _ in range(num)]

    def next_player(self):
        self.current_player = (self.current_player + self.direction) % len(self.players)

    def start(self):
        while True:
            player = self.players[self.current_player]
            print(f"\n{player.name}'s turn. Top card: {self.discard_pile[-1]}")
            print(f"Your hand: {[str(card) for card in player.cards]}")
            # Here you would add logic for playing/drawing cards
            # For now, just move to the next player
            self.next_player()
            # Win condition check (to be implemented)

# Example usage:
if __name__ == "__main__":
    game = Game(["Player A", "Player B", "Player C", "Player D"])
    game.start()