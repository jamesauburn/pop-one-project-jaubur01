#git commit -m"...""

#If you want to treat a list `lst` as circular (the first item
#  follows the last item), the item after `lst[i]` is not just `lst(i + 1)`,
#  but is `lst[(i + 1) % len(lst)]`.

#import random
#for i in read_:
    #road_map.write(read_) #needs to be check
import copy, math


rood_ = [('Alabama', 'Montgomery', 32.361538, -86.279118), ('Alaska', 'Juneau', 58.301935, -134.41974), ('Arizona', 'Phoenix', 33.448457, -112.073844)]
print(rood_)

shift_ = rood_

#shift the index of i
#end point going to the front

for i in range(0, len(shift_)):
    o = shift_[(i + 1) % len(shift_)]
    o[i] = o[i]+1

print(shift_)






f string
for sustituation
formart = f"This is a {value} string"


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
