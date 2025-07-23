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

#playing/drawing card mechanics
    def start(self):
     while True:
        player = self.players[self.current_player]
        top_card = self.discard_pile[-1]
        print(f"\n{player.name}'s turn. Top card: {top_card}")
        print(f"Your hand: {[str(card) for card in player.cards]}")

        # Find valid moves
        valid_moves = [card for card in player.cards if self.is_valid_move(card, top_card)]

        if valid_moves:
            played_card = valid_moves[0]  # For now, auto-play the first valid card
            player.cards.remove(played_card)
            self.discard_pile.append(played_card)
            print(f"{player.name} played: {played_card}")
        else:
            # Draw a card if no valid move
            if self.deck:
                drawn_card = self.deck.pop()
                player.cards.append(drawn_card)
                print(f"{player.name} had no valid moves and drew a card.")
            else:
                print("Deck is empty! Skipping draw.")

        # Win condition
        if not player.cards:
            print(f"{player.name} wins!")
            break

        self.next_player()

# Example usage:
if __name__ == "__main__":
    game = Game(["Player A", "Player B", "Player C", "Player D"])
    game.start()


#valid move checking
def is_valid_move(self, card, top_card):
    # Card is valid if color or number or special matches, or if it's a wild card
    return (
        card.color == top_card.color or
        card.number == top_card.number or
        card.special_ability == top_card.special_ability or
        card.color == "black"  # wild cards
    )