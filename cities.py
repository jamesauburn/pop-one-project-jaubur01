import math, copy, random
#from collections import deque

def read_cities(file_name):
    """
    Read in the cities from the given `file_name`, and return
    them as a list of four-tuples:

      [(state, city, latitude, longitude), ...]

    Use this as your initial `road_map`, that is, the cycle

      Alabama -> Alaska -> Arizona -> ... -> Wyoming -> Alabama.
    """
    """
    understand what can be input into the function.
        impliment solid method of cleaning and sorting the files
    need to add at least 5 tests for each function that needs to be tested.

        strip the ends using rstrip
        break down into \n and \t
        convert to list of tuples
        try accept criteria to accept is the data is input correctly.
    """
    #consider using rstrip
    #Do i need to add a user input for the file name?
    #Introduce try and execept to account for user error
    read_ = open(file_name, 'r').read() #check is read and readline makes a difference
    road_map_split = [i.split('\t') for i in read_.split('\n')] # Convert to list of list
    for i in road_map_split:
        i[2:4] = [float(j) for j in i[2:4]] # Convert co-ordinates to floats
    road_map_tuple = [tuple(i) for i in road_map_split] # Convert to list of tuples
    #do i need to close the file?
    return road_map_tuple

def print_cities(road_map):
    """
    Prints a list of cities, along with their locations.
    Print only one or two digits after the decimal point.
    """

    return print([(j[0], round((j[1]), 2), round(j[2], 2)) for j in [i[1:4] for i in road_map]])


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

    return sum_ #this needs to be check to see if the output is actually correct

def swap_cities(road_map, index1, index2):
    """
    Take the city at location `index` in the `road_map`, and the
    city at location `index2`, swap their positions in the `road_map`,
    compute the new total distance, and return the tuple

        (new_road_map, new_total_distance)

    Allow for the possibility that `index1=index2`,
    and handle this case correctly.
    """
    new_road_map = copy.copy(road_map) # can this be copy.copy copy.deepcopy
    new_road_map[index1], new_road_map[index2] = new_road_map[index2], new_road_map[index1]
    new_total_distance = compute_total_distance(new_road_map)
    return (new_road_map, new_total_distance) #this needs to be tested
        #does this need to be printed or return. The objext is being computed therefore will need to be a new list.

def shift_cities(road_map):
    """
    For every index i in the `road_map`, the city at the position i moves
    to the position i+1. The city at the last position moves to the position
    0. Return the new road map.
    """
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
    itter_ = 10000

    while itter_ != 0:
        num_ = random.randint(0, len(road_map)-1)
        num_2 = random.randint(0, len(road_map)-1) # need to utalise the output from swap citired, not redo the caluclation
        shifted_ = shift_cities(road_map)
        swapped_ = swap_cities(shifted_, num_, num_2)

        if swapped_[1] < best_:
            best_ = swapped_[1]
            hold_ = copy.copy(swapped_[0]) #working - shifted_
        itter_ -= 1

    return print_cities(hold_)
    #return best_ #this is not correct. I need to return the best route.


def print_map(road_map):
    """
    Prints, in an easily understandable format, the cities and
    their connections, along with the cost for each connection
    and the total cost.
    """
    #what is the cost?
    lst = list()
    for i in road_map:
        lst.append(road_map[i][2])

    """

    print all coordinates on a grip and label accordingly.
    plot the route prior to the analysis and a plot for after.
    """

    pass

def pass_criteria(file_name):

    #should this be done in the openfile location. should it require the user to inclue the file exension.
    try:
        read_ = open(file_name, 'r').read()
    except FileNotFoundError:
        print('This file cannot be found.')
        return False

    if not file_name.endswith('.txt'):
        print('Your file extension needs to be .txt.')
        print('Please enter the file name: ', end="")
        return False
    elif len(read_) == 0:
        print('This file contains no data.')
        return False
    else:
        return True

    #!!! to add to tests
    #strip '' from either side?
    #

def pythagoras(A, B, a, b):
    return math.sqrt(((A - a) ** 2) + ((B - b) ** 2))

def visulisation(road_map):



def main():
    """
    Reads in, and prints out, the city data, then creates the "best"
    cycle and prints it out.
    """
    print('Traveling Salesman - James Auburn - 13168179 - PoP Term 1 Project')
    valid_input = False
    while valid_input == False:
        print('Please enter the name of your file: ', end="")
        file_name = input()
        valid_input = pass_criteria(file_name)

    road_map = read_cities(file_name)
    print_map(road_map)
    #should this be printed in a nice text format. Each city on each line ect. No brackets or tuples brackets.


if __name__ == "__main__": #keep this in
    main()
