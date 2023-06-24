import random
import time

from Hal.Classes import Response
from Hal.Decorators import reg


class SimpleMath:
    @reg(name="Add")
    def add(self, a, b):
        """
        Adds two numbers and returns the result.

        :param integer a: The first number to be added.
        :param integer b: The second number to be added.
        :return: The sum of the two numbers.
        :rtype: number
        :raises: None

        Example:
        >>> obj = ClassName()
        >>> obj.add(3, 4)
        7
        """
        a = integer(a)
        b = integer(b)
        return Response(succeeded=True, data=a+b)

    @reg(name="Multiply")
    def multiply(self, a, b):
        """
        Multiplies two numbers and returns the result.

        :param self: The object instance.
        :param integer a: The first number to be multiplied.
        :param integer b: The second number to be multiplied.
        :return: The product of the two numbers.
        :rtype: number
        :raises: None

        Example:
        >>> obj = ClassName()
        >>> obj.multiply(3, 4)
        12
        """
        a = integer(a)
        b = integer(b)
        return Response(succeeded=True, data=a*b)

    @reg(name="Subtract")
    def subtract(self, a, b):
        """
        Subtracts one number from another and returns the result.

        :param self: The object instance.
        :param integer a: The number to be subtracted from.
        :param integer b: The number to subtract.
        :return: The difference between the two numbers.
        :rtype: number
        :raises: None

        Example:
        >>> obj = ClassName()
        >>> obj.subtract(7, 3)
        4
        """
        a = integer(a)
        b = integer(b)
        return Response(succeeded=True, data=a-b)

    @reg(name="Divide")
    def divide(self, a, b):
        """
        Divides one number by another and returns the result.

        :param self: The object instance.
        :param integer a: The dividend.
        :param integer b: The divisor.
        :return: The quotient of the division.
        :rtype: number
        :raises: None

        Example:
        >>> obj = ClassName()
        >>> obj.divide(10, 2)
        5.0
        """
        a = integer(a)
        b = integer(b)
        return Response(succeeded=True, data=a/b)
