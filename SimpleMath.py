import random
import time

from Hal.Classes import Response
from Hal.Decorators import reg


class SimpleMath:
    @reg(name="Add")
    def add(self, a, b):
        """
        Adds two numbers and returns the result.

        :param self: The object instance.
        :param a: The first number to be added.
        :param b: The second number to be added.
        :type a: number
        :type b: number
        :return: The sum of the two numbers.
        :rtype: number
        :raises: None

        Example:
        >>> obj = ClassName()
        >>> obj.add(3, 4)
        7
        """
        a = int(a)
        b = int(b)
        return Response(succeeded=True, data=a+b)

    @reg(name="Multiply")
    def multiply(self, a, b):
        """
        Multiplies two numbers and returns the result.

        :param self: The object instance.
        :param a: The first number to be multiplied.
        :param b: The second number to be multiplied.
        :type a: number
        :type b: number
        :return: The product of the two numbers.
        :rtype: number
        :raises: None

        Example:
        >>> obj = ClassName()
        >>> obj.multiply(3, 4)
        12
        """
        a = int(a)
        b = int(b)
        return Response(succeeded=True, data=a*b)

    @reg(name="Subtract")
    def subtract(self, a, b):
        """
        Subtracts one number from another and returns the result.

        :param self: The object instance.
        :param a: The number to be subtracted from.
        :param b: The number to subtract.
        :type a: number
        :type b: number
        :return: The difference between the two numbers.
        :rtype: number
        :raises: None

        Example:
        >>> obj = ClassName()
        >>> obj.subtract(7, 3)
        4
        """
        a = int(a)
        b = int(b)
        return Response(succeeded=True, data=a-b)

    @reg(name="Divide")
    def divide(self, a, b):
        """
        Divides one number by another and returns the result.

        :param self: The object instance.
        :param a: The dividend.
        :param b: The divisor.
        :type a: number
        :type b: number
        :return: The quotient of the division.
        :rtype: number
        :raises: None

        Example:
        >>> obj = ClassName()
        >>> obj.divide(10, 2)
        5.0
        """
        a = int(a)
        b = int(b)
        return Response(succeeded=True, data=a/b)
