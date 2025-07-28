import tkinter as tk
from tkinter import messagebox, simpledialog
import random

def buildDeck():
    deck = []
    colours = ["Red","Green","Yellow","Blue"]
    values = [0,1,2,3,4,5,6,7,8,9,"Draw Two", "Skip", "Reverse"]
    # Only add Wild Draw Four, not regular Wild
    for colour in colours:
        for value in values:
            cardVal = f"{colour} {value}"
            deck.append(cardVal)
            if value != 0:
                deck.append(cardVal)
    for i in range(4):
        deck.append("Wild Draw Four")
    random.shuffle(deck)
    return deck

CARD_COLORS = {
    "Red": "#ff4d4d",
    "Green": "#4dff4d",
    "Yellow": "#ffff66",
    "Blue": "#4d4dff",
    "Wild": "#cccccc"
}

class UnoGameUI:
    def __init__(self, root):
        self.root = root
        self.root.title("UNO Game")
        self.root.configure(bg="#222831")

        # Ask for number of players
        self.num_players = 0
        while self.num_players not in [2, 3, 4]:
            self.num_players = simpledialog.askinteger("Players", "How many players? (2-4)", minvalue=2, maxvalue=4)
            if self.num_players is None:
                self.root.destroy()
                return

        self.deck = buildDeck()
        self.players = [self.drawCards(5) for _ in range(self.num_players)]
        self.playerTurn = 0
        self.discard = [self.deck.pop()]
        self.colours = ["Red","Green","Yellow","Blue"]
        self.direction = 1
        self.setup_ui()
        self.update_ui()

    def drawCards(self, n):
        return [self.deck.pop() for _ in range(n)]

    def setup_ui(self):
        self.top_label = tk.Label(self.root, text="UNO Game", font=("Arial", 18, "bold"), bg="#222831", fg="#fff")
        self.top_label.pack(pady=10)
        self.discard_label = tk.Label(self.root, text="", font=("Arial", 14), bg="#222831", fg="#fff")
        self.discard_label.pack(pady=5)
        self.hand_frame = tk.Frame(self.root, bg="#393e46")
        self.hand_frame.pack(pady=10)
        self.draw_button = tk.Button(self.root, text="Draw Card", command=self.draw_card, font=("Arial", 12, "bold"), bg="#00adb5", fg="#fff")
        self.draw_button.pack(pady=10)
        self.info_label = tk.Label(self.root, text="", font=("Arial", 12), bg="#222831", fg="#fff")
        self.info_label.pack(pady=5)

    def update_ui(self):
        for widget in self.hand_frame.winfo_children():
            widget.destroy()
        self.discard_label.config(text=f"Top of Discard: {self.discard[-1]}")
        self.info_label.config(text=f"Player {self.playerTurn+1}'s turn")
        hand = self.players[self.playerTurn]
        row = 0
        col = 0
        for idx, card in enumerate(hand):
            card_color = card.split(" ", 1)[0]
            btn_color = CARD_COLORS.get(card_color, "#cccccc")
            btn = tk.Button(
                self.hand_frame, text=card, width=15, height=2,
                font=("Arial", 11, "bold"),
                bg=btn_color, fg="#222831" if card_color != "Yellow" else "#222831",
                command=lambda i=idx: self.play_card(i)
            )
            btn.grid(row=row, column=col, padx=4, pady=4)
            col += 1
            if col >= 7:
                col = 0
                row += 1

    def play_card(self, idx):
        card = self.players[self.playerTurn][idx]
        top_card = self.discard[-1]
        card_color, card_val = card.split(" ", 1)
        top_color, top_val = top_card.split(" ", 1)
        skip_next = False
        draw_count = 0
        reverse = False

        if "Wild Draw Four" in card:
            color_choice = simpledialog.askstring(
                "Wild Draw Four", "Choose a color (Red, Green, Yellow, Blue):"
            )
            if color_choice is None or color_choice.capitalize() not in self.colours:
                messagebox.showwarning("Invalid Color", "You must choose a valid color!")
                return
            chosen_color = color_choice.capitalize()
            new_card = f"{chosen_color} Wild Draw Four"
            self.discard.append(new_card)
            self.players[self.playerTurn].pop(idx)
            draw_count = 4
            skip_next = True
        # Wild logic removed

        elif card_color == top_color or card_val == top_val:
            self.discard.append(self.players[self.playerTurn].pop(idx))
            if card_val == "Draw Two":
                draw_count = 2
                skip_next = True
            elif card_val == "Skip":
                skip_next = True
            elif card_val == "Reverse":
                if self.num_players == 2:
                    skip_next = True  # In 2-player, Reverse acts as Skip
                else:
                    self.direction *= -1
                    self.playerTurn = (self.playerTurn + self.direction) % self.num_players
                    self.update_ui()
                    return
        else:
            messagebox.showwarning("Invalid Move", "You can't play that card!")
            return

        if len(self.players[self.playerTurn]) == 0:
            messagebox.showinfo("UNO", f"Player {self.playerTurn+1} wins!")
            self.root.quit()
            return

        # Handle drawing and skipping for Draw Two, Wild Draw Four, Skip, and Reverse
        if skip_next:
            next_player = (self.playerTurn + self.direction) % self.num_players
            for _ in range(draw_count):
                if self.deck:
                    self.players[next_player].append(self.deck.pop())
            # Skip the next player's turn
            self.playerTurn = (self.playerTurn + 2 * self.direction) % self.num_players
        else:
            self.playerTurn = (self.playerTurn + self.direction) % self.num_players

        self.update_ui()

    def draw_card(self):
        if self.deck:
            self.players[self.playerTurn].append(self.deck.pop())
            self.playerTurn = (self.playerTurn + self.direction) % self.num_players
            self.update_ui()
        else:
            messagebox.showinfo("Deck Empty", "No more cards to draw!")

if __name__ == "__main__":
    root = tk.Tk()
    game = UnoGameUI(root)
    root.mainloop()