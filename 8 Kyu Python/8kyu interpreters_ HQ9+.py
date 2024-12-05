def HQ9(code):
    match code:
        case "H":
            return "Hello World!"
        case "Q":
            return code
        case "9":
            return "\n".join(beer_song())

def beer_song():
    verses = []
    for i in range(99, 0, -1):
        if i > 1:
            verses.append(f"{i} bottles of beer on the wall, {i} bottles of beer.")
            verses.append(f"Take one down and pass it around, {i - 1} {'bottle' if i - 1 == 1 else 'bottles'} of beer on the wall.")
        else:
            verses.append(f"1 bottle of beer on the wall, 1 bottle of beer.")
            verses.append("Take one down and pass it around, no more bottles of beer on the wall.")
    verses.append("No more bottles of beer on the wall, no more bottles of beer.")
    verses.append("Go to the store and buy some more, 99 bottles of beer on the wall.")
    return verses
