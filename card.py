#class Card:
    def __init__(self, color="black", number=0, special_ability=None):
        self.color = color
        self.number = number
        self.special_ability = special_ability

    def __str__(self):
        parts = []
        if self.color and self.color != "black":
            parts.append(self.color)
        # Only show number if it's not zero or if it's a zero card
        if self.number or (self.number == 0 and not self.special_ability):
            parts.append(str(self.number))
        if self.special_ability:
            parts.append(self.special_ability)
        # For wild cards (black), show only special ability
        if self.color == "black" and self.special_ability:
            return f"{self.special_ability} (wild)"
        return " ".join(parts)

    def __repr__(self):
        return self.__str__()

if __name__ == "__main__":
    print(Card("blue", 7))           # Output: blue 7
    print(Card("red", 5))            # Output: red 5
    print(Card("yellow",))