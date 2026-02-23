# Tube strike options calculator

## The sweaty bus ride
There is a tube strike today so instead of getting the London Underground home you have decided to take the bus. It's a hot day and you have been sitting on the bus for over an hour, but the bus is hardly moving. Your arm is sticking to the window and sweat drips off your nose as you try to read your neighbour's book when you say to yourself, "This is ridiculous. I could have walked faster than this!" Suddenly you have an idea for an app that helps people decide whether to walk or take the bus home when the London Underground is on strike.
You rush home (relatively speaking) and begin to define the function that will underpin your app.

## Function specification
You must create a function which takes three parameters; walking distance home, distance the bus must travel, and the combined distance of walking from the office to the bus stop and from the bus stop to your house. All distances are in kilometres.
So for example, if your home is 5km away by foot, and the bus that takes you home travels 6km, but you have to walk 500 metres to the bus stop to catch it and 500 metres to your house once the bus arrives (i.e. 1km in total), which is faster, walking or taking the bus?

Example - Which of these is faster?:

- Start---Walk 5km--->End
- Start---Walk 500m---Bus 6km---Walk 500m--->End

Walking speed and bus driving speed have been given to you as two pre-loaded variables (`$global_variables` in Ruby).

`walk` = 5 (km/hr) `bus` = 8 (km/hr)

The function must return the fastest option, either "Walk" or "Bus". If the walk is going to be over 2 hours, the function should recommend that you take the bus. If the walk is going to be under 10 minutes, the function should recommend that you walk. If both options are going to take the same amount of time, the function should recommend that you walk

# Given Code

```python
def calculator(distance, bus_drive, bus_walk):
    pass # Your code here
```

# My Solution

```python
def calculator(distance: int, bus_drive: int, bus_walk: int) -> str:
    # Your code here
    walk_time: float = distance / 5 
    bus_time: float = (bus_walk / 5) + (bus_drive / 8)
    
    if walk_time > 2:
        return "Bus" 
    elif (walk_time < 1/6) or (walk_time <= bus_time): 
        return "Walk"
    else:
        return "Bus"
```

# Complexity Analysis

**Time Complexity:** O(1)

**Space Complexity:** O(1)

**Explanation:**
**Time: O(1)** - Constant time complexity. The code performs a fixed number of operations regardless of input size. No loops or recursive calls that depend on input size were detected.

**Space: O(1)** - Constant space complexity. The code uses a fixed amount of memory regardless of input size.
