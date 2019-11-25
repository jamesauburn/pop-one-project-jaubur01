import pytest
from cities import *

"""
Programs should be tested as thoroughly as possible using
the `pytest` unit testing framework. Functions that do input or output
are difficult to test. Therefore, those functions, should do as little
computation as possible, and functions that do computation, should do no
input or output.

In this assignment `main`, `read_cities`, `print_cities`, and
`print_map` result in input or output, so you do not need to
write unit tests for these. Also, you do not need to test `find_best_cycle`
because of random results.
Provide unit tests for all the  other functions, as well as any additional
computational functions you might write.
"""

def test_compute_total_distance():
    road_map1 = [("Kentucky", "Frankfort", 38.197274, -84.86311),\
                ("Delaware", "Dover", 39.161921, -75.526755),\
                ("Minnesota", "Saint Paul", 44.95, -93.094)]

    assert compute_total_distance(road_map1)==\
           pytest.approx(9.386+18.496+10.646, 0.01)

    #using the firgure above test the output fuctions correctly.
    #remenber not to compare floats.
    #assert float(computer_total_distance(???)) = float()

def test_swap_cities():
    road_map1 = [("Kentucky", "Frankfort", 38.197274, -84.86311),\
                ("Delaware", "Dover", 39.161921, -75.526755),\
                ("Minnesota", "Saint Paul", 44.95, -93.094)]
    assert road_map1 != swap_cities(road_map1, 0, 1)

    pass

def test_shift_cities():
    road_map2 = [("Kentucky", "Frankfort", 38.197274, -84.86311),\
                ("Delaware", "Dover", 39.161921, -75.526755),\
                ("Minnesota", "Saint Paul", 44.95, -93.094)]
    road_map3 = [("Minnesota", "Saint Paul", 44.95, -93.094),\
                ("Kentucky", "Frankfort", 38.197274, -84.86311),\
                ("Delaware", "Dover", 39.161921, -75.526755)]

    assert road_map3 == shift_cities(road_map2)

def test_compute_total_distance():
    road_map2 = [('a', 'a', 0, 0), ('a', 'a', 3, 4), ('a', 'a', 0, 0), ('a', 'a', 3, 4)]

    assert compute_total_distance(road_map2) == 20

def test_pythagoras():
    assert pythagoras(3, 4, 0, 0) == 5
    assert pythagoras(6, 8, 3, 4) == 5
"""
include test for all moduals that have been added.

def test_main():
    #DO NOT TEST
def test_read_cities():
    #DO NOT TEST
def test_print_cities():
    #DO NOT TEST
def test_print_map():
    #DO NOT TEST
def test_find_best_cycle():
    #DO NOT TEST
"""


'''
use assert statement
assert Blooean Expression

!do not try to == with float intergers!

'''
