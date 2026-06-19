def is_loch_ness_monster(string):
    phrases = ["tree fiddy", "3.50", "three fifty"]
    for i in phrases:
        if i in string:
            return True
    return False
