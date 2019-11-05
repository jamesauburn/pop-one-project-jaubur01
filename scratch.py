
#for i in read_:
    #road_map.write(read_) #needs to be check if required
import copy, math, random
from collections import deque


rood_ = [('Alabama', 'Montgomery', 32.361538, -86.279118), ('Alaska', 'Juneau', 58.301935, -134.41974), ('Arizona', 'Phoenix', 33.448457, -112.073844), ('Rlabama', 'Bontgomery', 32.361538, -86.279118), ('Blabama', 'Rontgomery', 32.361538, -86.279118), ('Blabama', 'Rontgomery', 32.361538, -86.279118)]


"""
    Using a combination of `swap_cities` and `shift_cities`,
    try `10000` swaps/shifts, and each time keep the best cycle found so far.
    After `10000` swaps/shifts, return the best cycle found so far.
    Use randomly generated indices for swapping.
"""

road_map = rood_
new_road_map = rood_

road_map[-1:].append(road_map[:-1])
new_road_map = new_road_map.append(new_road_map.pop(0))

print(road_map)
print(new_road_map)


"""
f string
for sustituation
formart = f"This is a {value} string"
!!!use this for trying to do the visulisation in a grid
    if it is possible to use these outside strings.



 #to be added to the user input file name. Import to add to debug
exceptions
input_ = input('Enter: ')
try:
    infile = open(file_name, 'r')
    line = infile.readline()
    while line !='':
            print(line.rstrip())
            line = infile.readline())
except: FileNotFoundError:
    print('The file name you have enetered does not exist. :(')
    end
---
others to check
that indexes are within the rangeof the data set
chexk that all digits entered are positive
check that
    'except Exceptions as e:
        print('You have an error: 'e)'
Do i need to add a check and balance for the square root function
    can use raise to rasie an exception
finally catches all other errors. If by itself use except:

"""
