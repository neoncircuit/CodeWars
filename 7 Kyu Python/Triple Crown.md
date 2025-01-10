# Triple Crown

## Instructions

Welcome to the world of the National Football League!

In the NFL the Triple Crown is given when a receiver has the most receiving yards, the most receiving touchdowns and the most receptions in a single season.

This year Cooper Kupp managed to get it, however it is quite rare because the last one was in 2005 by Steve Smith.

Now you will receive a dictionary with the following keys (will always contain each):

- Cooper Kupp

- Justin Jefferson

- Davante Adams

Each key will have another dictionary as their values with the following keys:

- Receiving yards (value between 1500-2000)

- Receiving touchdowns (value between 10-20)

- Receptions (value between 90-120)

If one receiver has the most in each category you have to return his name. If there is no receiver with the most values in all categories you should return 'None of them'.

Example:

```
{
  'Cooper Kupp': 
    {
    'Receiving yards': 1786, 
    'Receiving touchdowns': 18, 
    'Receptions': 117
    },
  'Justin Jefferson': 
    {
    'Receiving yards': 1700, 
    'Receiving touchdowns': 17, 
    'Receptions': 115
    },
  'Davante Adams': 
    {
    'Receiving yards': 1650, 
    'Receiving touchdowns': 16, 
    'Receptions': 110
    }
}

# The output should be 'Cooper Kupp' since he has more receiving yards, more receiving touchdowns and more receptions as well
```

Example with two receivers sharing values in at least one category:

```
{
  'Cooper Kupp': 
    {
    'Receiving yards': 1900, 
    'Receiving touchdowns': 18, 
    'Receptions': 117
    },
  'Justin Jefferson': 
    {
    'Receiving yards': 1800, 
    'Receiving touchdowns': 17, 
    'Receptions': 116
    },
  'Davante Adams': 
    {
    'Receiving yards': 1900, 
    'Receiving touchdowns': 18, 
    'Receptions': 110
    }
}

# The output should be 'None of them' since they are tied on receiving yards and receiving touchdowns
```

## Given Code
```python
def triple_crown(receivers):
    pass
```

## My Solution
```python
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

```
