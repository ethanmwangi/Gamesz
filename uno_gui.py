import tkinter as tk
from tkinter import messagebox
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

class UnoGameUI:
    def __init__(self, root):
        self.root = root
        self.root.title("UNO Game")
        self.deck = buildDeck()
        self.players = [self.drawCards(5), self.drawCards(5)]
        self.playerTurn = 0
        self.discard = [self.deck.pop()]
        self.colours = ["Red","Green","Yellow","Blue"]
        self.setup_ui()
        self.update_ui()

    def drawCards(self, n):
        return [self.deck.pop() for _ in range(n)]

    def setup_ui(self):
        self.top_label = tk.Label(self.root, text="UNO Game", font=("Arial", 16))
        self.top_label.pack()
        self.discard_label = tk.Label(self.root, text="", font=("Arial", 14))
        self.discard_label.pack()
        self.hand_frame = tk.Frame(self.root)
        self.hand_frame.pack()
        self.draw_button = tk.Button(self.root, text="Draw Card", command=self.draw_card)
        self.draw_button.pack(pady=10)
        self.info_label = tk.Label(self.root, text="", font=("Arial", 12))
        self.info_label.pack()

    def update_ui(self):
        for widget in self.hand_frame.winfo_children():
            widget.destroy()
        self.discard_label.config(text=f"Top of Discard: {self.discard[-1]}")
        self.info_label.config(text=f"Player {self.playerTurn+1}'s turn")
        hand = self.players[self.playerTurn]
        for idx, card in enumerate(hand):
            btn = tk.Button(self.hand_frame, text=card, width=15,
                            command=lambda i=idx: self.play_card(i))
            btn.pack(side=tk.LEFT, padx=2)

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
            self.playerTurn = (self.playerTurn + 1) % 2
            self.update_ui()
        else:
            messagebox.showwarning("Invalid Move", "You can't play that card!")

    def draw_card(self):
        if self.deck:
            self.players[self.playerTurn].append(self.deck.pop())
            self.playerTurn = (self.playerTurn + 1) % 2
            self.update_ui()
        else:
            messagebox.showinfo("Deck Empty", "No more cards to draw!")

if __name__ == "__main__":
    root = tk.Tk()
    game = UnoGameUI(root)
    root.mainloop()