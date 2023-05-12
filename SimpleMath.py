import random
import time

from Hal.Classes import Response
from Hal.Decorators import reg


class SimpleMath:
    @reg(name="Add")
    def add(self, a: "number", b: "number"):
        a = int(a)
        b = int(b)
        return Response(suceeded=True, data=a+b)

    @reg(name="Multiply")
    def multiply(self, a: "number", b: "number"):
        a = int(a)
        b = int(b)
        return Response(suceeded=True, data=a*b)

    @reg(name="Subtract")
    def subtract(self, a: "number", b: "number"):
        a = int(a)
        b = int(b)
        return Response(suceeded=True, data=a-b)

    @reg(name="Divide")
    def divide(self, a: "number", b: "number_not_zero"):
        a = int(a)
        b = int(b)
        return Response(suceeded=True, data=a/b)
