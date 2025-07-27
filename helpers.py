from card import Card

#def create_all_cards():
    deck = []
    # Number cards (0-9, each color)
    for color in ["red", "blue", "green", "yellow"]:
        deck.append(Card(color, 0))  # One zero per color
        for _ in range(2):  # Two of each 1-9 per color
            for number in range(1, 10):
                deck.append(Card(color, number))
        # Action cards (two of each per color)
        for _ in range(2):
            deck.append(Card(color, special_ability="skip"))
            deck.append(Card(color, special_ability="reverse"))
            deck.append(Card(color, special_ability="+2"))
    # Wild cards (4 of each)
    for _ in range(4):
        deck.append(Card("black", special_ability="everything"))  # Wild
        deck.append(Card("black", special_ability="+4"))          # Wild Draw Four
    return deck