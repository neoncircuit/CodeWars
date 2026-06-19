def are_you_playing_banjo(name: str) -> str:
    # Implement me!
    plays_banjo: str = f"{name} plays banjo"
    plays_banjo_not: str = f"{name} does not play banjo"
    return plays_banjo if (name.lower().startswith("r")) else plays_banjo_not