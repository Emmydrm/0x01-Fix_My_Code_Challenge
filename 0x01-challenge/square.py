#!/usr/bin/python3
"""This module contains the class square"""

class Square():
    
    side_length = 0

    def __init__(self, *args, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area(self):
        """ Area of the square """
        return self.side_length * self.side_length

    def perimeter(self):
        return 4 * self.side_length

    def __str__(self):
        return "{}/{}".format(self.side_length, self.side_length)

if __name__ == "__main__":
    s = Square(side_length=12)
    print(s)
    print(s.area())
    print(s.perimeter())
