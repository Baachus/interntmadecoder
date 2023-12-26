"""OOP inheritance examples"""

class Shape:
    """
    A class to represent a shape
    """
    def __init__(self, color: str) -> None:
        """
        Initialize a person with a first and last name
        """
        self.__color = color

    @property
    def color(self):
        """Getter for color"""
        return self.__color

    @color.setter
    def color(self, color):
        """Setter for color"""
        self.__color = color

    def description(self) -> None:
        """Prints the color of the shape"""
        print(f"This shape is {self.color}")

class Square(Shape):
    """
    A class to represent a square
    """
    def __init__(self, color: str, side_length: int):
        super().__init__(color)
        self.__side_length = side_length

    @property
    def side_length(self):
        """Getter for side_length"""
        return self.__side_length

    @side_length.setter
    def side_length(self, side_length):
        """Setter for side_length"""
        self.__side_length = side_length

    def description(self) -> None:
        """Prints the square information"""
        print(f"This square is {self.color} and has a side length of {self.side_length}")

circle = Shape("blue")
square = Square("red", 327)

circle.description()
square.description()
