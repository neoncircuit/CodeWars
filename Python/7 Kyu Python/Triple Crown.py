def triple_crown(receivers):
    # Find the maximum values for each category
    max_yards = max(player["Receiving yards"] for player in receivers.values())
    max_touchdowns = max(player["Receiving touchdowns"] for player in receivers.values())
    max_receptions = max(player["Receptions"] for player in receivers.values())

    # Count how many players match the max in each category
    yards_count = sum(player["Receiving yards"] == max_yards for player in receivers.values())
    touchdowns_count = sum(player["Receiving touchdowns"] == max_touchdowns for player in receivers.values())
    receptions_count = sum(player["Receptions"] == max_receptions for player in receivers.values())

    # If any category has more than one max match, return "None of them"
    if yards_count > 1 or touchdowns_count > 1 or receptions_count > 1:
        return "None of them"

    # Find the player who matches all three max values
    for player, stats in receivers.items():
        if (stats["Receiving yards"] == max_yards and
            stats["Receiving touchdowns"] == max_touchdowns and
            stats["Receptions"] == max_receptions):
            return player

    # If no player matches all three, return "None of them"
    return "None of them"
