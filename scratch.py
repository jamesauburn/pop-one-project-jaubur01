"""
need to prove robusness of program
need to produce visualisation
review the need for copy.copy throughout the document.
Provide unit tests for all the  other functions, as well as any additional
computational functions you might write.
"""
#for i in read_:
    #road_map.write(read_) #needs to be check if required

import copy, math, random
import tkinter as tk

road_map = [('Alabama', 'Montgomery', 32.361538, -86.279118), ('Alaska', 'Juneau', 58.301935, -134.41974), ('Arizona', 'Phoenix', 33.448457, -112.073844), ('Rlabama', 'Bontgomery', 32.361538, -86.279118), ('Blabama', 'Rontgomery', 32.361538, -86.279118), ('Blabama', 'Rontgomery', 32.361538, -86.279118)]




"""
window_ = tk.Tk()
window_.geometry('1000x400')
window_.title('Traveling Salesman.')


lbl_0 = tk.Label(window_, text='James Auburn', font=('Helvetica', 16, 'bold')).grid(column=0, row=0)
lbl_0 = tk.Label(window_, text='ID : 13168179', font=('Helvetica', 16, 'bold')).grid(column=1, row=0)

lbl_1 = tk.Label(window_, text='Enter your file name:', font=('Helvetica', 12)).grid(column=0, row=2)
txt_1 = tk.Entry(window_, width=10).grid(column=1, row=2)
def clicked():
    lbl_1.configure(text= txt_1.get()).grid(column=0, row=6)
btn_1 = tk.Button(window_, text='Submit.', font=('Helvetica', 12), command=clicked).grid(column=2, row=2) #This button isnt working.
#lbl_pass = Label(window_, text='fail.').grid(column=3, row=1)
#lbl_fail = Label(window_, text='pass.').grid(column=3, row=2)

lbl_3 = tk.Label(window_, text='Find best route.', font=('Helvetica', 12)).grid(column=0, row=3)
btn_2 = tk.Button(window_, text='Route', font=('Helvetica', 12), command=clicked).grid(column=1, row=3)

#create progress bar for itterations
window_.mainloop()
"""


"""
import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def say_hi(self):
        print("hi there, everyone!")

root = tk.Tk()
app = Application(master=root)
app.mainloop()
"""
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
