#!/usr/bin/env python

"""Custom error for calculator program"""


class InsufficientOperands(Exception):
    """Raised when less than the two required operands are provided"""
    pass
