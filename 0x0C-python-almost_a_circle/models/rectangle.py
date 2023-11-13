#!/usr/bin/python3

"""Class Rectangle"""


from models.base import Base


class Rectangle(Base):
    """
    Class Rectangle:
        A rectangle class that inherites from Base class.

    Args:
        Base: The base class.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Class constructor.

        Args:
            id = Instances counter.
            width: Rectangle width.
            height: Rectangle height.
            x: Rectangle Vertical position.
            y: Rectangle Horizontal position.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Private attribute property."""
        return self.__width

    @width.setter
    def width(self, value):
        """
        Private attribute setter.

        Args:
            value: The attribute new value.

        Raises:
            TypeError: If the value is not int.
            ValueError: If the attribute is less than or equal zero.
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Private attribute property."""
        return self.__height

    @height.setter
    def height(self, value):
        """
        Private attribute setter.

        Args:
            value: The attribute new value.

        Raises:
            TypeError: If the value is not int.
            ValueError: If the attribute is less than or equal zero.
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Private attribute property."""
        return self.__x

    @x.setter
    def x(self, value):
        """
        Private attribute setter.

        Args:
            value: The attribute new value.

        Raises:
            TypeError: If the value is not int.
            ValueError: If the attribute is less than or equal zero.
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Private attribute property."""
        return self.__y

    @y.setter
    def y(self, value):
        """
        Private attribute setter.

        Args:
            value: The attribute new value.

        Raises:
            TypeError: If the value is not int.
            ValueError: If the attribute is less than or equal zero.
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Public class method that returns The area value of the rectangle."""
        return self.__width * self.__height

    def display(self):
        """Public class method that prints rectangle instance with #."""
        for k in range(self.y):
            print()
        for i in range(self.height):
            print(" " * self.x, end="")
            print("#" * self.width)

    def __str__(self):
        """Overriding __str__ method."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height
        )

    def update(self, *args, **kwargs):
        """
        Public class method to update the rectangle values.

        Args:
            args: The passed values to assign.
            kwargs: The passed values with it's keywords to assign.
        """
        if len(args) > 0:
            try:
                self.id = args[0]
                self.width = args[1]
                self.height = args[2]
                self.x = args[3]
                self.y = args[4]
            except IndexError:
                pass
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "width":
                    self.width = value
                elif key == "height":
                    self.height = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """Puclic class method that returns the dict representation."""
        keys = ["id", "width", "height", "x", "y"]
        self_dict = {}

        for key in keys:
            self_dict[key] = getattr(self, key)

        return self_dict
