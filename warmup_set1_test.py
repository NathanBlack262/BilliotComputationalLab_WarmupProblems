import unittest
import math

filename = "nblack_warmupset1.py"
target = __import__(filename)

circle_area = target.circle_area
square_side = target.square_side
rectangle_area = target.rectangle_area
rectangle_perimeter = target.rectangle_perimeter
distance = target.distance
heavier_than_fluorine = target.heavier_than_fluorine
double_evens_triple_odds = target.double_evens_triple_odds
is_exothermic = target.is_exothermic
is_spontaneous = target.is_spontaneous
usable_innmr = target.usable_innmr



class Test_WarmupSet1(unittest.TestCase):
    pass