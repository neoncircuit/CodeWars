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