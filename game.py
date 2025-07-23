import random
from helpers import create_all_cards
from player import Player
from card import Card

class Game:
    def __init__(self, player_names):
        self.deck = create_all_cards()
        random.shuffle(self.deck)
        self.players = [Player(name, self.draw_cards(7)) for name in player_names]
        self.discard_pile = [self.deck.pop()]
        self.current_player = 0
        self.direction = 1  

    def draw_cards(self, num):
        return [self.deck.pop() for _ in range(num)]

    def next_player(self):
        self.current_player = (self.current_player + self.direction) % len(self.players)

    def is_valid_move(self, card, top_card):
        # Card is valid if color or number or special matches, or if it's a wild card
        return (
            card.color == top_card.color or
            card.number == top_card.number or
            card.special_ability == top_card.special_ability or
            card.color == "black"  # wild cards
        )

    def start(self):
        while True:
            player = self.players[self.current_player]
            top_card = self.discard_pile[-1]
            print(f"\n{player.name}'s turn. Top card: {top_card}")
            print("Your hand:")
            for idx, card in enumerate(player.cards):
                print(f"{idx}: {card}")

            # Find valid moves
            valid_moves = [card for card in player.cards if self.is_valid_move(card, top_card)]

            if valid_moves:
                print("Valid moves:")
                for idx, card in enumerate(player.cards):
                    if card in valid_moves:
                        print(f"{idx}: {card}")
                while True:
                    choice = input("Enter the number of the card you want to play, or 'd' to draw: ")
                    if choice.lower() == 'd':
                        break
                    if choice.isdigit():
                        choice = int(choice)
                        if 0 <= choice < len(player.cards) and player.cards[choice] in valid_moves:
                            played_card = player.cards.pop(choice)
                            self.discard_pile.append(played_card)
                            print(f"{player.name} played: {played_card}")
                            break
                    print("Invalid choice. Try again.")
                else:
                    # If player chose to draw
                    if self.deck:
                        drawn_card = self.deck.pop()
                        player.cards.append(drawn_card)
                        print(f"{player.name} drew a card.")
                    else:
                        print("Deck is empty! Skipping draw.")
            else:
                # No valid moves, must draw
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