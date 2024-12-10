def whose_move(last_player, win):
    # Your Move...
    match (last_player, win):
        case ("black", True) | ("white", True):
            return last_player
        case ("black", False) | ("white", False):
            return "white" if last_player == "black" else "black"