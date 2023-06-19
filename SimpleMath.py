import random
import time

from Hal.Classes import Response
from Hal.Decorators import reg


class SimpleMath:
    @reg(name="Add")
    def add(self, a, b):
        """
        Adds two numbers and returns the result.
    
        Args:
            self: The object instance.
            a (number): The first number to be added.
            b (number): The second number to be added.
    
        Returns:
            number: The sum of the two numbers.
    
        Raises:
            None
    
        Examples:
            >>> obj = ClassName()
            >>> obj.add(3, 4)
            7
        """
        a = int(a)
        b = int(b)
        return Response(suceeded=True, data=a+b)

    @reg(name="Multiply")
    def multiply(self, a: "number", b: "number"):
        """
        Multiplies two numbers and returns the result.
    
        Args:
            self: The object instance.
            a (number): The first number to be multiplied.
            b (number): The second number to be multiplied.
    
        Returns:
            number: The product of the two numbers.
    
        Raises:
            None
    
        Examples:
            >>> obj = ClassName()
            >>> obj.multiply(3, 4)
            12
        """
        a = int(a)
        b = int(b)
        return Response(suceeded=True, data=a*b)

    @reg(name="Subtract")
    def subtract(self, a, b):
        """
        Subtracts one number from another and returns the result.
    
        Args:
            self: The object instance.
            a (number): The number to be subtracted from.
            b (number): The number to subtract.
    
        Returns:
            number: The difference between the two numbers.
    
        Raises:
            None
    
        Examples:
            >>> obj = ClassName()
            >>> obj.subtract(7, 3)
            4
        """
        a = int(a)
        b = int(b)
        return Response(suceeded=True, data=a-b)

    @reg(name="Divide")
    def divide(self, a, b):
        """
        Divides one number by another and returns the result.
    
        Args:
            self: The object instance.
            a (number): The dividend.
            b (number): The divisor.
    
        Returns:
            number: The quotient of the division.
    
        Raises:
            None
    
        Examples:
            >>> obj = ClassName()
            >>> obj.divide(10, 2)
            5.0
        """
        a = int(a)
        b = int(b)
        return Response(suceeded=True, data=a/b)
