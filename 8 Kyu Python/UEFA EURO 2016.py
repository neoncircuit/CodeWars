def uefa_euro_2016(teams, scores):
    match scores:
        case [winner_score, loser_score] if winner_score > loser_score:
            return f"At match {teams[0]} - {teams[1]}, {teams[0]} won!"
        case [loser_score, winner_score] if winner_score > loser_score:
            return f"At match {teams[0]} - {teams[1]}, {teams[1]} won!"
        case _:
            return f"At match {teams[0]} - {teams[1]}, teams played draw."