import math


def circle_area(radius):
    '''
    Returns the area of a circle, given its radius. Use math.pi to represent pi.
    '''
    return math.pi * radius ** 2

def square_side(perimeter):
    '''
    Returns the side of a square, given its perimeter.
    '''
    return perimeter / 4

def rectangle_area(length,width):
    '''
    Returns the area of a rectangle, given its length and width.
    '''
    return length * width

def rectangle_perimeter(length,width):
    '''
    Returns the perimeter of a rectangle, given its length and width.
    '''
    return 2 * (length + width)

def distance(x1, y1, x2, y2):
    '''
    Returns the distance between two points, given their Cartesian coordinates (x1, y1) and (x2, y2)
    '''
    return math.sqrt((y2-y1)**2 + (x2-x1)**2)

def heavier_than_fluorine(mass_num):
    '''
    Returns True if mass_num is heavier than fluorine, and False otherwise.
    '''
    if mass_num > 18.998:
        return True
    else:
        return False

def double_evens_triple_odds(num):
    '''
    If num is even, return twice the value of num. If num is odd, return thrice the value of num.
    ''' 
    if num % 2 == 0:
        return 2*num
    else:
        return 3*num

def is_exothermic(enthalpy):
    '''
    Returns True if a reaction is exothermic, and False if not.
    '''
    if enthalpy < 0:
        return True
    else:
        return False

def is_spontaneous(enthalpy, entropy, temperature):
    '''
    Returns True if a reaction is spontaneous, and False if not. Assume that all three values are given in agreeing units
    (Kelvin, Joules)
    '''
    gibbs_free_energy = enthalpy - entropy * temperature
    if gibbs_free_energy < 0:
        return True
    else:
        return False


def usable_innmr(atomic_number, atomic_mass):
    '''
    Returns True if an atomic isotope is usable in NMR (i.e., has a nuclear spin), and False if not.
    '''
    if atomic_number % 2 == 1 or atomic_mass % 2 == 1:
        return True
    else:
        return False





