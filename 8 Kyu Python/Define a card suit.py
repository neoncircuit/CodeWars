def define_suit(card):
    suits = {
        'S': 'spades',
        'D': 'diamonds',
        'H': 'hearts',
        'C': 'clubs'
    }
    return suits[card[-1]]