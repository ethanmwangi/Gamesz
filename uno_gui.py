import tkinter as tk
from tkinter import messagebox, simpledialog
import random

def buildDeck():
    deck = []
    colours = ["Red","Green","Yellow","Blue"]
    values = [0,1,2,3,4,5,6,7,8,9,"Draw Two", "Skip", "Reverse"]
    wilds = ["Wild","Wild Draw Four"]
    for colour in colours:
        for value in values:
            cardVal = f"{colour} {value}"
            deck.append(cardVal)
            if value != 0:
                deck.append(cardVal)
    for i in range(4):
        deck.append(wilds[0])
        deck.append(wilds[1])
    random.shuffle(deck)
    return deck

# For button colors
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
        self.root.configure(bg="#222831")  # Set background color

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
        for idx, card in enumerate(hand):
            card_color = card.split(" ", 1)[0]
            btn_color = CARD_COLORS.get(card_color, "#cccccc")
            btn = tk.Button(
                self.hand_frame, text=card, width=15, height=2,
                font=("Arial", 11, "bold"),
                bg=btn_color, fg="#222831" if card_color != "Yellow" else "#222831",
                command=lambda i=idx: self.play_card(i)
            )
            btn.pack(side=tk.LEFT, padx=4, pady=4)

    def play_card(self, idx):
        card = self.players[self.playerTurn][idx]
        top_card = self.discard[-1]
        card_color, card_val = card.split(" ", 1)
        top_color, top_val = top_card.split(" ", 1)
        if "Wild" in card or card_color == top_color or card_val == top_val:
            self.discard.append(self.players[self.playerTurn].pop(idx))
            if len(self.players[self.playerTurn]) == 0:
                messagebox.showinfo("UNO", f"Player {self.playerTurn+1} wins!")
                self.root.quit()
                return
            self.playerTurn = (self.playerTurn + 1) % self.num_players
            self.update_ui()
        else:
            messagebox.showwarning("Invalid Move", "You can't play that card!")

    def draw_card(self):
        if self.deck:
            self.players[self.playerTurn].append(self.deck.pop())
            self.playerTurn = (self.playerTurn + 1) % self.num_players
            self.update_ui()
        else:
            messagebox.showinfo("Deck Empty", "No more cards to draw!")

if __name__ == "__main__":
    root = tk.Tk()
    game = UnoGameUI(root)
    root.mainloop()