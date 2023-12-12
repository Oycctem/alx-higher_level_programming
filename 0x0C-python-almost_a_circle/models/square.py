#!/usr/bin/python3
"""Rectangle Class Definition"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square Class Representation"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a Square"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get or set the size of the square"""
        return self.width

    @size.setter
    def size(self, value):
        """Set the size of the square"""
        self.width = value
        self.height = value

    def __str__(self):
        """Return string representation of the square"""
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(self.id,
                                                         self.x,
                                                         self.y,
                                                         self.width)

    def update(self, *args, **kwargs):
        """Update the attributes of the square"""
        if args:
            for i, arg in enumerate(args):
                setattr(self, ["id", "size", "x", "y"][i], arg)
        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def to_dictionary(self):
        """Return a dictionary representation of the square"""
        return {"id": self.id, "size": self.width, "x": self.x, "y": self.y}

