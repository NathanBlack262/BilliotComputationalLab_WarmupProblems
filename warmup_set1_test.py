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
    def test_circle_area(self):
        result1 = circle_area(4)
        result2 = circle_area(10)
        result3 = circle_area(19)
        self.assertAlmostEqual(result1, math.pi * 4**2)
        self.assertAlmostEqual(result2, math.pi * 10**2)
        self.assertAlmostEqual(result3, math.pi * 19**2)
    
    def test_square_side(self):
        result1 = square_side(4)
        result2 = square_side(10.2)
        result3 = square_side(68)
        self.assertAlmostEqual(result1, 4/4)
        self.assertAlmostEqual(result2, 10.2/4)
        self.assertAlmostEqual(result3, 68/4)
    
    def test_rectangle_area(self):
        result1 = rectangle_area(3,4)
        result2 = rectangle_area(10,4.9)
        result3 = rectangle_area(6.8,7.2)
        self.assertAlmostEqual(result1, 3*4)
        self.assertAlmostEqual(result2, 10*4.9)
        self.assertAlmostEqual(result3, 6.8*7.2)

    def test_rectangle_perimeter(self):
        result1 = rectangle_perimeter(3,4)
        result2 = rectangle_perimeter(10,4.9)
        result3 = rectangle_perimeter(6.8,7.2)
        self.assertAlmostEqual(result1, 2*(3+4))
        self.assertAlmostEqual(result2, 2*(10*4.9))
        self.assertAlmostEqual(result3, 2*(6.8*7.2))

    def test_distance(self):
        result1 = distance(0,0,5,12)
        result2 = distance(0,0,3,4)
        result3 = distance(2,9,10,24)
        self.assertAlmostEqual(result1, math.sqrt((12-0)**2 + (5-0)**2))
        self.assertAlmostEqual(result2, math.sqrt((4-0)**2 + (3-0)**2))
        self.assertAlmostEqual(result3, math.sqrt((24-9)**2 + (9-2)**2))

    def test_heavier_than_fluorine(self):
        result1 = heavier_than_fluorine(14)
        result2 = heavier_than_fluorine(20)
        result3 = heavier_than_fluorine(127)
        self.assertAlmostEqual(result1, False)
        self.assertAlmostEqual(result2, True)
        self.assertAlmostEqual(result3, True)

    def test_double_evens_triple_odds(self):
        result1 = double_evens_triple_odds(8)
        result2 = double_evens_triple_odds(6)
        result3 = double_evens_triple_odds(7)
        self.assertAlmostEqual(result1, 16)
        self.assertAlmostEqual(result2, 12)
        self.assertAlmostEqual(result3, 21)

    def test_is_exothermic(self):
        result1 = is_exothermic(4)
        result2 = is_exothermic(-12.9)
        result3 = is_exothermic(19.3)
        self.assertAlmostEqual(result1, False)
        self.assertAlmostEqual(result2, True)
        self.assertAlmostEqual(result3, False)

    def test_is_spontaneous(self):
        result1 = is_spontaneous(4,9,4)
        result2 = is_spontaneous(-3,9,4)
        result3 = is_spontaneous(9,1,4)
        self.assertAlmostEqual(result1, True)
        self.assertAlmostEqual(result2, True)
        self.assertAlmostEqual(result3, False)

    def test_usable_nmr(self):
        result1 = usable_innmr(3,9)
        result2 = usable_innmr(4,8)
        result3 = usable_innmr(4,11)
        self.assertAlmostEqual(result1, True)
        self.assertAlmostEqual(result2, False)
        self.assertAlmostEqual(result3, True)




