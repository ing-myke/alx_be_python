polymorphism_demo.py
# polymorphism_demo.py

import math

class Shape:
    """A base class for geometric shapes."""
    def area(self):
        """
        Calculates the area of the shape.
        This method must be overridden by derived classes.
        """
        raise NotImplementedError("Subclasses must implement this method")

class Rectangle(Shape):
    """A derived class for a rectangle."""
    def __init__(self, length: float, width: float):
        self.length = length
        self.width = width

    def area(self) -> float:
        """
        Overrides the area() method to calculate the rectangle's area.
        """
        return self.length * self.width

class Circle(Shape):
    """A derived class for a circle."""
    def __init__(self, radius: float):
        self.radius = radius

    def area(self) -> float:
        """
        Overrides the area() method to calculate the circle's area.
        """
        return math.pi * self.radius**2
