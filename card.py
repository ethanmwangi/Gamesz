class Card:
    def __init__(self, color="black", number=0, special_ability=None):
        self.color = color
        self.number = number
        self.special_ability = special_ability

    def __str__(self):
        parts = []
        if self.color:
            parts.append(self.color)
        if self .number:
            parts.append(str(self.number))
        if self.special_ability:
            parts.append(self.special_ability)
            return " ".join(parts)

    def __repr__(self):
        return self.__str__()