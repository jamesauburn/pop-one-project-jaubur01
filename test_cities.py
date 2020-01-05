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

    road_map2 = [('a', 'a', 0, 0), ('a', 'a', 3, 4), ('a', 'a', 0, 0), ('a', 'a', 3, 4)]

    road_map3 = []

    road_map4 = [('a', 'a', 3, 4)]

    assert compute_total_distance(road_map1)==\
           pytest.approx(9.386+18.496+10.646, 0.01)

    assert compute_total_distance(road_map2) == 20

    assert compute_total_distance(road_map2) != 15

    assert compute_total_distance(road_map3) == 0

    assert compute_total_distance(road_map4) == 0

    #using the firgure above test the output fuctions correctly.
    #remenber not to compare floats.
    #assert float(compute_total_distance(???)) = float()


def test_swap_cities():
    road_map1 = [("Kentucky", "Frankfort", 38.197274, -84.86311),\
                ("Delaware", "Dover", 39.161921, -75.526755),\
                ("Minnesota", "Saint Paul", 44.95, -93.094)]

    road_map2 = swap_cities(road_map1, 0, 1)

    road_map3 = swap_cities(road_map1, 0, 0)

    road_map4 = []

    assert road_map1 != road_map2[0]

    assert road_map1 == road_map3[0]

    #with pytest.raises(Exception):
    #    swap_cities(road_map1, 0, 3)
    assert swap_cities(road_map1, 0, -4) == 'Index out of range'

    #with pytest.raises(Exception):
    #    swap_cities(road_map1, 0, -4)
    assert swap_cities(road_map1, 0, 3) == 'Index out of range'

    assert swap_cities(road_map4, 0, 1) == 'Index out of range'


def test_shift_cities():
    road_map1 = []

    road_map2 = [("Kentucky", "Frankfort", 38.197274, -84.86311)]

    road_map3 = [("Kentucky", "Frankfort", 38.197274, -84.86311),\
                ("Delaware", "Dover", 39.161921, -75.526755),\
                ("Minnesota", "Saint Paul", 44.95, -93.094)]

    road_map4 = [("Minnesota", "Saint Paul", 44.95, -93.094),\
                ("Kentucky", "Frankfort", 38.197274, -84.86311),\
                ("Delaware", "Dover", 39.161921, -75.526755)]

    #with pytest.raises(Exception):
    #    shift_cities(road_map1)
    assert shift_cities(road_map1) == 'Empty list'

    assert road_map2 == shift_cities(road_map2)

    assert road_map4 == shift_cities(road_map3)

    assert road_map4 != shift_cities(road_map4)

    assert road_map3 != shift_cities(road_map3)


def test_pass_criteria():

    assert pass_criteria('python.txt') == False

    assert pass_criteria('city-data') == False

    assert pass_criteria('cities.py') == False

    assert pass_criteria('') == False

    assert pass_criteria('city-data.txt') == True


def test_pythagoras():

    assert pythagoras(3, 4, 0, 0) == 5

    assert pythagoras(6, 8, 3, 4) == 5

    assert pythagoras(0, 0, 0, 0) == 0

    assert pythagoras(-3, -4, 0, 0) == 5

    assert pythagoras(-6, -8, -3, -4) == 5

    assert pythagoras(0, 0, 0, 0) == 0

    assert pythagoras(6, 8, -3, -4) == 15

    assert pythagoras(1, 2, 3, 4)==\
           pytest.approx(2.828427)

    assert pythagoras(-1, -2, 3, 4)==\
           pytest.approx(7.2111)

    assert pythagoras(-1, -2, -3, -4)==\
           pytest.approx(2.828427)


def test_makelong():
    test_ = 'abc'
    test_2 = (1, 2, 3)

    assert len(make_long(test_, 5)) == 5

    assert len(make_long(test_, 3)) == 3

    assert len(make_long(test_, 1)) == 3

    assert len(make_long(test_, -4)) == 3

    assert make_long(test_2, 10) == 'Input invalid'
