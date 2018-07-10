import adder, subtracter, multiplier, divider
from calculator import Calculator

calculator = Calculator(adder.Adder(), subtracter.Subtracter(), multiplier.Multiplier(), divider.Divider())
