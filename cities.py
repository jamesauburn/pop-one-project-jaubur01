import math
import copy
import random
import sys
import os
import subprocess


def read_cities(file_name):
    """
    Read in the cities from the given `file_name`, and return
    them as a list of four-tuples:

      [(state, city, latitude, longitude), ...]

    Use this as your initial `road_map`, that is, the cycle

      Alabama -> Alaska -> Arizona -> ... -> Wyoming -> Alabama.
    """
    road_map = open(file_name, 'r').read()
    road_map.strip()
    road_map = [i.split('\t') for i in road_map.split('\n')]
    road_map = [(j[0], j[1], float(j[2]), float(j[3])) for j in road_map]

    return road_map

def print_cities(road_map):
    """
    Prints a list of cities, along with their locations.
    Print only one or two digits after the decimal point.
    """
    hold_ = [(j[1], round(j[2], 1), round(j[3], 1)) for j in road_map]

    new_ = 'City Location\t\t\t| Lat\t| Long\n-----------------------------------------\n'
    for i in hold_:
        new_ += make_long(i[0], 24) + '\t| ' + str(i[1]) + '\t| ' + str(i[2]) + '\n'

    print(new_)


def compute_total_distance(road_map):
    """
    Returns, as a floating point number, the sum of the distances of all
    the connections in the `road_map`. Remember that it's a cycle, so that
    (for example) in the initial `road_map`, Wyoming connects to Alabama...
    """
    if len(road_map) == 0:
        return 0

    a = road_map[0][2]
    b = road_map[0][3]
    sum_ = 0

    for i in range(0, len(road_map)):
        next_ = road_map[(i + 1) % len(road_map)]
        A, B = a, b
        a, b = next_[2], next_[3]
        sum_ += pythagoras(A, B, a, b)

    return sum_

def swap_cities(road_map, index1, index2):
    """
    Take the city at location `index` in the `road_map`, and the
    city at location `index2`, swap their positions in the `road_map`,
    compute the new total distance, and return the tuple

        (new_road_map, new_total_distance)

    Allow for the possibility that `index1=index2`,
    and handle this case correctly.
    """
    try:
        road_map_swap = copy.copy(road_map)
        road_map_swap[index1], road_map_swap[index2] = road_map_swap[index2], road_map_swap[index1]
        new_total_distance = compute_total_distance(road_map_swap)
        return (road_map_swap, new_total_distance)
    except IndexError as error:
        return 'Index out of range'

def shift_cities(road_map):
    """
    For every index i in the `road_map`, the city at the position i moves
    to the position i+1. The city at the last position moves to the position
    0. Return the new road map.
    """
    try:
        road_map_shift = copy.copy(road_map)
        road_map_shift.insert(0, road_map_shift[-1])
        road_map_shift.pop()
        return road_map_shift
    except IndexError as error:
        return 'Empty list'

def find_best_cycle(road_map):
    """
    Using a combination of `swap_cities` and `shift_cities`,
    try `10000` swaps/shifts, and each time keep the best cycle found so far.
    After `10000` swaps/shifts, return the best cycle found so far.
    Use randomly generated indices for swapping.
    """
    best_ = math.inf
    itter_ = 100000
    road_map_best = copy.copy(road_map)

    while itter_ != 0:
        num_ =  random.randint(0, len(road_map_best)/2)
        num_2 = random.randint(len(road_map_best)/2, len(road_map_best)-1)
        swapped_ = swap_cities(road_map_best, num_, num_2)

        if swapped_[1] < best_:
            best_ = swapped_[1]
            road_map_best = swapped_[0]
            print(swapped_[1])
        road_map_best = shift_cities(road_map_best)
        itter_ -= 1

    return road_map_best


def print_map(road_map):
    """
    Prints, in an easily understandable format, the cities and
    their connections, along with the cost for each connection
    and the total cost.
    """
    total_ = 0
    div_ = '\n-----------------------------------------------\n'
    new_ = 'City Connection\t\t\t\t| Cost' + div_

    for i in range(0, len(road_map)):
        next_ = road_map[(i + 1) % len(road_map)]
        cost_ = pythagoras(road_map[i][2], road_map[i][3], next_[2], next_[3])
        new_ += make_long(road_map[i][1] + ' -> ' + next_[1], 32) + '\t| ' + str(round(cost_, 1)) + '\n'
        total_ += cost_
    new_ += div_ + 'The total cost is ' + str(round(total_,1 )) + div_

    print(new_)


def pass_criteria(file_name):
    try:
        read_ = open(file_name, 'r').read()
    except FileNotFoundError:
        print('This file cannot be found. Please ensure it is in the working directory or the file path has been specified.')
        return False

    if not file_name.endswith('.txt'):
        print("Your file extension needs to be '.txt'.")
        return False
    elif len(read_) == 0:
        print('This file contains no data.')
        return False
    else:
        return True


def pythagoras(A, B, a, b):
    return math.sqrt(((A - a) ** 2) + ((B - b) ** 2))


def make_long(i, j):
    try:
        if len(i) > j-1:
            return i
        else:
            return make_long(i + ' ', j)
    except TypeError as error:
        return 'Input invalid'


def vis(road_map):

    road_map_rounded = [[j[0], j[1], round(j[2]), round(j[3])] for j in road_map]

    x = []
    y = []

    for i in road_map_rounded:
        x.append(round(i[2]))
        y.append(round(i[3]))

    print('    ', end='')
    for j in range(min(y), max(y)+1, 2):
        print(make_long(str(j), 5), end='|')
    print('\n___|', end='')
    for j in range(min(y), max(y)+1, 2):
        print('_^|__|', end='')
    print('\n', end='')

    for i in range(max(x), min(x)-1, -1):   # lat   = +/- 90     = x     = +90 -> -90
        print(make_long(str(i), 2), '|', end='')
        for j in range(min(y), max(y)+1):   # long  = -/+ 180    = y     = -180 -> 180
            for p, q in enumerate(road_map_rounded):
                if i == q[2] and j == q[3]:
                    hold_ = make_long(str(p + 1), 2) + '|'
                    break
                else:
                    hold_ = '__|'
            print(hold_, end='')
        print('__|')

    print('\nNOTE: The following locations are located at the same ID due to their close proximity:')

    count_ = 0
    for p, q in enumerate(road_map_rounded):
        count_ = 0
        for j in road_map_rounded:
            if q[2] == j[2] and q[3] == j[3]:
                count_ += 1
            if count_ >= 2:
                print(make_long(q[1], 24) + '| ' + str(p+1))
                count_ -= 1
    print('-----------------------------')
    new_ = '\nIndex:' + '\n' + make_long('City', 24) + '| ID\n-----------------------------\n'
    for p, q in enumerate(road_map_rounded):
        new_ += make_long(q[1], 24) + '| ' + str(p + 1) + '\n'

    print(new_)


def main():
    """
    Reads in, and prints out, the city data, then creates the "best"
    cycle and prints it out.
    """

    print('\nTraveling Salesman - James Auburn - 13168179 - PoP Term 1 Project\nPlease enter the name of your file (include file extension): ', end='')
    file_name = input()
    while pass_criteria(file_name) is False:
        file_name = input()

    road_map = read_cities(file_name)
    print_cities(road_map)
    best_road_map = find_best_cycle(road_map)
    print_map(best_road_map)
    vis(best_road_map)

if __name__ == "__main__": #keep this in
    main()
