
#for i in read_:
    #road_map.write(read_) #needs to be check if required

import copy, math, random
import tkinter as tk

road_map = [('Alabama', 'Montgomery', 32.361538, -86.279118), ('Alaska', 'Juneau', 58.301935, -134.41974), ('Arizona', 'Phoenix', 33.448457, -112.073844), ('Rlabama', 'Bontgomery', 32.361538, -86.279118), ('Blabama', 'Rontgomery', 32.361538, -86.279118), ('Blabama', 'Rontgomery', 32.361538, -86.279118)]

def pythagoras(A, B, a, b):
    return math.sqrt(((A - a) ** 2) + ((B - b) ** 2))

def make_long(i): # use this to print in a pleasant format.
    if len(i) > 32:
        return i
    else:
        return make_long(i + ' ')

def print_map(road_map):


    hold_ = [(j[1], round(j[2], 1), round(j[3], 1)) for j in road_map]
    print(hold_)
    
    new_ = 'City\t\t\t\t\tLat\tLong\tCost\n' # can this be move to print_cities?
    for i in range(0, len(hold_)):
        next_ = hold_[(i + 1) % len(hold_)]
        new_ += make_long(hold_[i][0] + ' -> ' + next_[0]) + '\t' + str(hold_[i][1]) + '\t' + str(hold_[i][2]) + '\t' + str(round(pythagoras(hold_[i][1], hold_[i][2], 0, 0), 1)) + '\n' # this cost is wrong. I have done the distance from 0 not from each point.
    
    """
    #make loop to make format  x -> Y x y cost
    for i in range(0, len(road_map)):
        next_ = road_map[(i + 1) % len(road_map)]
        A, B = a, b
        a, b = next_[2], next_[3]
        sum_ += pythagoras(A, B, a, b)
    """
    
    
    return new_

print(print_map(road_map))





"""
road_map_split = [['Alabama', 'Montgomery', '32.361538', '-86.279118'], ['Alaska', 'Juneau', '58.301935', '-34.41974'], ['Arizona', 'Phoenix', '33.448457', '-112.073844'], ['Rlabama', 'Bontgomery', '32.361538', '-86.279118'], ['Blabama', 'Rontgomery', '32.361538', '-86.279118'], ['Blabama', 'Rontgomery', '32.361538', '-86.279118']]

print(road_map_split)

""
for i in road_map_split:
        i[2:4] = [float(j) for j in i[2:4]] # Convert co-ordinates to floats
""

hold_ = [(j[0], j[1], float(j[2]), float(j[3])) for j in road_map_split]

print(hold_)
"""








"""
!!!TKINTER

window_ = tk.Tk()
window_.geometry('1000x400')
window_.title('Traveling Salesman')

def clicked():
    lbl_1.configure(text= txt_1.get()).grid(column=0, row=6)

lbl_0 = tk.Label(window_, text='James Auburn', anchor='w', font=('Helvetica', 16, 'bold')).grid(column=0, row=0)
lbl_0 = tk.Label(window_, text='ID : 13168179', anchor='w', font=('Helvetica', 16, 'bold')).grid(column=1, row=0)

lbl_1 = tk.Label(window_, text='Enter your file name:', anchor='w', font=('Helvetica', 12)).grid(column=0, row=2)
txt_1 = tk.Entry(window_, width=40).grid(column=1, row=2)
btn_1 = tk.Button(window_, text='Submit', font=('Helvetica', 12), command=clicked).grid(column=2, row=2) #This button isnt working.

#lbl_pass = Label(window_, text='fail.').grid(column=3, row=1)
#lbl_fail = Label(window_, text='pass.').grid(column=3, row=2)

btn_2 = tk.Button(window_, text='Find new Route.', anchor='w', font=('Helvetica', 12), command=clicked).grid(column=1, row=3)

#create progress bar for itterations
window_.mainloop()


#add a link above each column for the heasing labels.
#add copy to clipboard button.


"""
