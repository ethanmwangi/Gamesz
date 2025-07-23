class Card:
    def __init__(self, color="black", number=0, special_ability=None):
        self.color = color
        self.number = number
        self.special_ability = special_ability

    def __str__(self):
        return f" {self.number} {self.special_ability}"

    def __repr__(self):
        return f"{self.number} {self.color} {self.special_ability}"
        