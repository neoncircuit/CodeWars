# Holiday VI - Shark Pontoon

## Instructions

Your friend invites you out to a cool floating pontoon around 1km off the beach. Among other things, the pontoon has a huge slide that drops you out right into the ocean, a small way from a set of stairs used to climb out.

As you plunge out of the slide into the water, you see a shark hovering in the darkness under the pontoon... Crap!

You need to work out if the shark will get to you before you can get to the pontoon. To make it easier... as you do the mental calculations in the water you either freeze when you realise you are dead, or swim when you realise you can make it!

You are given 5 variables;

- sharkDistance = distance from the shark to the pontoon. The shark will eat you if it reaches you before you escape to the pontoon.

- sharkSpeed = how fast it can move in metres/second.

- pontoonDistance = how far you need to swim to safety in metres.

- youSpeed = how fast you can swim in metres/second.

- dolphin = a boolean, if true, you can half the swimming speed of the shark as the dolphin will attack it.

- The pontoon, you, and the shark are all aligned in one dimension.

If you make it, return "Alive!", if not, return "Shark Bait!".



## Given Code
```python
def shark(pontoon_distance, shark_distance, you_speed, shark_speed, dolphin):
    pass # Don't get eaten!
```

## My Solution
```python
def shark(pontoon_distance, shark_distance, you_speed, shark_speed, dolphin=False):
    # Don't get eaten!
    if dolphin == True:
        shark_speed /= 2      
    return "Alive!" if pontoon_distance/you_speed < shark_distance/shark_speed else "Shark Bait!"
```
