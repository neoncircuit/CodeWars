# Grasshopper - Create the rooms

## Instructions

## Escape the room

You are creating an "Escape the room" game. The first step is to create a hash table ( `dict` in Python) called rooms that contains all of the `rooms` of the game. There should be at least 3 rooms inside it, each room being a hash table with at least 3 properties (e.g. `name`, `description`, `completed`).

## Given Code
```python
rooms = {}
```

## My Solution
```python
def create_room(name, description):
    return {
        "name": name,
        "description": description,
        "completed": False
    }

rooms = {
    "room1": create_room("Room 1", "Description Room 1."),
    "room2": create_room("Room 2", "Description Room 2."),
    "room3": create_room("Room 3", "Description Room 3.")
}
```
