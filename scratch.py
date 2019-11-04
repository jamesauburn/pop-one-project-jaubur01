#git commit -m"...""

#If you want to treat a list `lst` as circular (the first item
#  follows the last item), the item after `lst[i]` is not just `lst(i + 1)`,
#  but is `lst[(i + 1) % len(lst)]`.

#import random

#number_ = N * random.random()
#    """
#    Returns, as a floating point number, the sum of the distances of all
#    the connections in the `road_map`. Remember that it's a cycle, so that
#    (for example) in the initial `road_map`, Wyoming connects to Alabama...
#
#    #If you want to treat a list `lst` as circular (the first item
    #  follows the last item), the item after `lst[i]` is not just `lst(i + 1)`,
    #  but is `lst[(i + 1) % len(lst)]`.




rood_ = [('Alabama', 'Montgomery', 32.361538, -86.279118), ('Alaska', 'Juneau', 58.301935, -134.41974), ('Arizona', 'Phoenix', 33.448457, -112.073844)]

import math

compute_ = rood_ #!!!!!!!!!!!!!!!!!!!
    # !!!!!!!!!! compute = read_cities(road_map)
def pythag(A, B, a, b):
    distance_ = math.sqrt(((A - a) ** 2) + ((B - b) ** 2))
    return distance_

a = compute_[0][2]
b = compute_[0][3]

for x in range(0, len(compute_)):
    o = compute_[(x + 1) % len(compute_)]
    A, B = a, b 
    a, b = o[2], o[3]
    print(pythag(A, B, a, b))

#for i in compute_:
#    A = i[2]
#    B = i[3]
#    print(pythag(A, B, a, b))
#    a = A
#    b = B
#---
#compute_ = [('a', 'b', 'c', 'd'), ('e', 'f', 'g', 'h'), ('i', 'j', 'k', 'l')]
#a = compute_[0][2]
#b = compute_[0][3]
#s = len(compute_)



            #a = j[2]
            #b = j[3]
            #print(a)
            #print(b)
        #dist_list.append(pythag(A, B, a, b))

    #take cordinates from first and second
    #pythogorus to compute distances
    #return as an append to a new list
    # for the purpose of this return a sum of the list
