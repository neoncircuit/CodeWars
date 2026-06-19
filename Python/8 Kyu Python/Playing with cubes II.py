class Cube(object):
    # This cube needs help
    # Define a constructor which takes one integer, or handles no args
    def __init__(self, side: int = 0) -> int:
        self.set_side(side)
    
    def get_side(self) -> int:
        """Return the side of the Cube"""
        return self.__side

    def set_side(self, new_side: int) -> int:
        """Set the value of the Cube's side."""
        self.__side = abs(new_side)