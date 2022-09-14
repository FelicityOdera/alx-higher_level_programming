#!/usr/bin/python3
"""
a class Square that defines a square by: 4-square.py
"""


class Square:
    """
    position should be use by using space when position[1] > 0
    """
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        self.__size = value
        if type(self.__size) is not int:
            raise TypeError("size must be an integer")
        if self.__size < 0:
            raise ValueError("size must be >= 0")

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        self.__position = value
        if not isinstance(self.position, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(self.position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(self.position[0]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(self.position[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if self.position[0] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        if self.position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.__size > 0:
            if self.position[1] > 0:
                for line in range(self.position[1]):
                    print("")
            for i in range(self.size):
                if self.position[0] > 0:
                    for white_spaces in range(self.position[0]):
                        print("#", end="")
                for j in range(self.size):
                    print("#", end="")
                print("")
        else:
            print("")
