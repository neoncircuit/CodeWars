# UEFA EURO 2016

## Instructions

Finish the uefaEuro2016() function so it return string just like in the examples below:

```
uefa_euro_2016(['Germany', 'Ukraine'],[2, 0]) # "At match Germany - Ukraine, Germany won!"
uefa_euro_2016(['Belgium', 'Italy'],[0, 2]) # "At match Belgium - Italy, Italy won!"
uefa_euro_2016(['Portugal', 'Iceland'],[1, 1]) # "At match Portugal - Iceland, teams played draw."
```

## Given Code
```python
def uefa_euro_2016(teams, scores):
    pass
```

## My Solution
```python
def uefa_euro_2016(teams, scores):
    match scores:
        case [winner_score, loser_score] if winner_score > loser_score:
            return f"At match {teams[0]} - {teams[1]}, {teams[0]} won!"
        case [loser_score, winner_score] if winner_score > loser_score:
            return f"At match {teams[0]} - {teams[1]}, {teams[1]} won!"
        case _:
            return f"At match {teams[0]} - {teams[1]}, teams played draw."
```
