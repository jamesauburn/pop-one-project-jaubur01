import math, copy, random
import sys, time

def read_cities(file_name):
    """
    Read in the cities from the given `file_name`, and return
    them as a list of four-tuples:

      [(state, city, latitude, longitude), ...]

    Use this as your initial `road_map`, that is, the cycle

      Alabama -> Alaska -> Arizona -> ... -> Wyoming -> Alabama.
    """

    read_ = open(file_name, 'r').read()
    read_.strip()
    road_map_split = [i.split('\t') for i in read_.split('\n')]
    road_map_float = [(j[0], j[1], float(j[2]), float(j[3])) for j in road_map_split]
    road_map_tuple = [tuple(i) for i in road_map_float]

    return road_map_tuple

def print_cities(road_map):
    """
    Prints a list of cities, along with their locations.
    Print only one or two digits after the decimal point.
    """
    hold_ = [(j[0], round(j[2], 1), round(j[3], 1)) for j in road_map]

    new_ = 'City\t\t\t| Lat\t| Long\n-----------------------------------------\n' # can this be move to print_cities?
    for i in hold_:
        new_ += make_long(i[1], 16) + '\t| ' + str(i[1]) + '\t| ' + str(i[2]) + '\n'

    return print(new_)


def compute_total_distance(road_map):
    """
    Returns, as a floating point number, the sum of the distances of all
    the connections in the `road_map`. Remember that it's a cycle, so that
    (for example) in the initial `road_map`, Wyoming connects to Alabama...
    """
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
    road_ = copy.copy(road_map) #This copy is necessary
    road_[index1], road_[index2] = road_[index2], road_[index1]
    new_total_distance = compute_total_distance(road_)

    return (road_, new_total_distance) #this needs to be tested (not sure what)


def shift_cities(road_map):
    """
    For every index i in the `road_map`, the city at the position i moves
    to the position i+1. The city at the last position moves to the position
    0. Return the new road map.
    """
    #is is neccessary to not return the same variable?
    road_map.insert(0, road_map[-1])
    road_map.pop()

    return road_map

def find_best_cycle(road_map):
    """
    Using a combination of `swap_cities` and `shift_cities`,
    try `10000` swaps/shifts, and each time keep the best cycle found so far.
    After `10000` swaps/shifts, return the best cycle found so far.
    Use randomly generated indices for swapping.
    """
    best_ = math.inf
    hold_ = None
    itter_ = 100000
    load_ = ['o....', '.o...', '..o..', '...o.', '....o', '.o...', '..o..', '...o.',]


    while itter_ != 0:
        num_ = random.randint(0, len(road_map)-1)
        num_2 = random.randint(0, len(road_map)-1)
        shifted_ = shift_cities(road_map)
        swapped_ = swap_cities(shifted_, num_, num_2)

        if swapped_[1] < best_:
            best_ = swapped_[1]
            hold_ = copy.copy(swapped_[0]) #does this need to be copy.copy
        itter_ -= 1
        road_map = swapped_[0]

        print(load_[0], '\b')
        print

    spinner = spinning_cursor()
    for _ in range(50):
        sys.stdout.write(next(spinner))
        sys.stdout.flush()
        time.sleep(0.1)
        sys.stdout.write('\b')

    return hold_

def spinning_cursor():
    while True:
        for cursor in '|/-\\':
            yield cursor

def print_map(road_map):
    """
    Prints, in an easily understandable format, the cities and
    their connections, along with the cost for each connection
    and the total cost.
    """
    #what is the cost? the ditance?
    #can this be in a plot format?

    total_ = 0
    div_ = '\n-----------------------------------------------\n'
    new_ = 'City Connection\t\t\t\t| Cost' + div_

    for i in range(0, len(road_map)):
        next_ = road_map[(i + 1) % len(road_map)]
        cost_ = pythagoras(road_map[i][2], road_map[i][3], next_[2], next_[3])
        new_ += make_long(road_map[i][0] + ' -> ' + next_[0], 32) + '\t| ' + str(round(cost_, 1)) + '\n' # this cost is wrong. I have done the distance from 0 not from each point.
        total_ += cost_
    new_ += div_ + 'The total cost is ' + str(round(total_,1 )) + div_

    return print(new_)
    """
    print all coordinates on a grip and label accordingly.
    plot the route prior to the analysis and a plot for after.
    """

def pass_criteria(file_name):
    try:
        read_ = open(file_name, 'r').read()
    except FileNotFoundError:
        print('This file cannot be found.')
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

def make_long(i, j): # use this to print in a aethetic format.
    if len(i) > j:
        return i
    else:
        return make_long(i + ' ', j)

def visulisation(road_map):

    pass

def main():
    """
    Reads in, and prints out, the city data, then creates the "best"
    cycle and prints it out.
    """

    print('Traveling Salesman - James Auburn - 13168179 - PoP Term 1 Project')
    valid_input = False
    while valid_input == False:
        print('Please enter the name of your file (include file extension): ', end='')
        file_name = input()
        valid_input = pass_criteria(file_name)

    road_map = read_cities(file_name)
    #print_cities(road_map)
    print_map(road_map)
    #print_cities(find_best_cycle(road_map)) #is this required?
    print_map(find_best_cycle(road_map))
    #should this be printed in a nice text format. Each city on each line ect. No brackets or tuples brackets.

if __name__ == "__main__": #keep this in
    main()
