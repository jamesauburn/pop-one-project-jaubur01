def read_cities(file_name):
    """
    Read in the cities from the given `file_name`, and return
    them as a list of four-tuples:

      [(state, city, latitude, longitude), ...]

    Use this as your initial `road_map`, that is, the cycle

      Alabama -> Alaska -> Arizona -> ... -> Wyoming -> Alabama.
    """

    read_ = open('file_name').read()
    read_ = [i.split('\t') for i in read_.split('\n')] # Convert to list of list
    for i in read_:
        i[2:4] = [float(j) for j in i[2:4]] # Convert co-ordinates to floats
    read_ = [tuple(i) for i in read_] # Convert to list of tuples
    return read_

def print_cities(road_map):
    """
    Prints a list of cities, along with their locations.
    Print only one or two digits after the decimal point.
    """
    print_ = read_cities(road_map)
    print_ = [(j[0], round((j[1]), 2), round(j[2], 2)) for j in [i[1:4] for i in print_]]
    return print_

def compute_total_distance(road_map):
    """
    Returns, as a floating point number, the sum of the distances of all
    the connections in the `road_map`. Remember that it's a cycle, so that
    (for example) in the initial `road_map`, Wyoming connects to Alabama...
    """
    #If you want to treat a list `lst` as circular (the first item
    #  follows the last item), the item after `lst[i]` is not just `lst(i + 1)`,
    #  but is `lst[(i + 1) % len(lst)]`.

    rood_ = [('Alabama', 'Montgomery', 32.361538, -86.279118), ('Alaska', 'Juneau', 58.301935, -134.41974), ('Arizona', 'Phoenix', 33.448457, -112.073844)]

    import math

    compute_ = rood_ #!!!!!!!!!!!!!!!!!!!
    # !!!!!!!!!! compute = read_cities(road_map)
    def pythag(A, B, a, b):
        distance_ = math.sqrt(((A - a) ** 2) + ((B - b) ** 2))
        return distance_

    dist_calc_ = []
    A = 0
    B = 0
    a = 0
    b = 0

    for i in compute_:
        A = i[2]
        B = i[3]
        print(pythag(A, B, a, b))
        a = A
        b = B

            #a = j[2]
            #b = j[3]
            #print(a)
            #print(b)
        #dist_list.append(pythag(A, B, a, b))

    #take cordinates from first and second
    #pythogorus to compute distances
    #return as an append to a new list
    # for the purpose of this return a sum of the list
    #create dict of city and distance

    pass

def swap_cities(road_map, index1, index2):
    """
    Take the city at location `index` in the `road_map`, and the
    city at location `index2`, swap their positions in the `road_map`,
    compute the new total distance, and return the tuple

        (new_road_map, new_total_distance)

    Allow for the possibility that `index1=index2`,
    and handle this case correctly.
    """
    pass

def shift_cities(road_map):
    """
    For every index i in the `road_map`, the city at the position i moves
    to the position i+1. The city at the last position moves to the position
    0. Return the new road map.
    """
    pass

def find_best_cycle(road_map):
    """
    Using a combination of `swap_cities` and `shift_cities`,
    try `10000` swaps/shifts, and each time keep the best cycle found so far.
    After `10000` swaps/shifts, return the best cycle found so far.
    Use randomly generated indices for swapping.
    """
    pass

def print_map(road_map):
    """
    Prints, in an easily understandable format, the cities and
    their connections, along with the cost for each connection
    and the total cost.
    """
    pass

def main():
    """
    Reads in, and prints out, the city data, then creates the "best"
    cycle and prints it out.
    """
    pass

if __name__ == "__main__": #keep this in
    main()
