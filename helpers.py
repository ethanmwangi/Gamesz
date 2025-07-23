from main import Card


def create_all_cards():
    deck = []
    for _ in range(4):
        for color in ["red", "blue", "green", "yellow"]:
            for number in range(1, 10):
                deck.append(Card(color, number))
            for special_ability in ["skip", "reverse", "+2", "+4"]:
                deck.append(Card(color, 10, special_ability))
    # Add special cards
    deck.append(Card(special_ability="+4"))
    deck.append(Card(special_ability="+4"))
    deck.append(Card(special_ability="everything"))
    deck.append(Card(special_ability="+4"))

    
    return deck