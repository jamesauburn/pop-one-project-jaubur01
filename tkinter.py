import tkinter as tk
from tkinter import filedialog
import os


"""
root_ = tk.Tk()

root.mainloop()

canva = root.Canvas(root, height=400, wdith=400, bg='#26342')
"""


"""
#!!!TKINTER

window_ = tk.Tk()
window_.geometry('500x500')
window_.title('Traveling Salesman')

def clicked():
    lbl_1.configure(text= txt_1.get()).grid(column=0, row=6)
    messagebox.showinfo('Message title','Message content') #for content
    messagebox.showerror('Message title', 'Message content') # for error on loading.

def open_clicked():
    file = filedialog.askopenfilename(filetypes = (("Text files","*.txt"),("all files","*.*")))

def find_clicked():
    pass

lbl_1 = tk.Label(window_, text='Enter your file name:', anchor='w', font=('Helvetica', 12)).grid(column=0, row=0)
txt_1 = tk.Entry(window_, width=16).grid(column=1, row=0)
btn_1 = tk.Button(window_, text='Find the best route!', font=('Helvetica', 12), command=clicked).grid(column=2, row=0) #This button isnt working.

lbl_1 = tk.Label(window_, text='Find the shortest route!', anchor='w', font=('Helvetica', 12)).grid(row=0)

btn_1 = tk.Button(window_, text='Open', font=('Helvetica', 12), command=open_clicked).grid(row=1, sticky='w') #This button isnt working.

#lbl_pass = Label(window_, text='fail.').grid(column=3, row=1)
#lbl_fail = Label(window_, text='pass.').grid(column=3, row=2)

bar1 = Progressbar(window_, length=200, style='black.Horizontal.TProgressbar', value='70').grid(row=8)



#create progress bar for itterations
window_.mainloop()


#add a link above each column for the heasing labels.
#add copy to clipboard button.
"""

"""
import pandas as pd
import numpy as np
import geoviews as gv
import geoviews.tile_sources as gvts
from geoviews import dim, opts
gv.extension('bokeh')

import matplotlib.pyplot as plt

road_map = [('Alabama', 'Montgomery', 32.361538, -86.279118), ('Alaska', 'Juneau', 58.301935, -134.41974), ('Arizona', 'Phoenix', 33.448457, -112.073844), ('Rlabama', 'Bontgomery', 32.361538, -86.279118), ('Blabama', 'Rontgomery', 32.361538, -86.279118), ('Blabama', 'Rontgomery', 32.361538, -86.279118)]



x = []
y = []

for i in road_map:
    x.append(i[2])
    y.append(i[3])

print(x)
print(y)

print(plt.plot(x, y))
"""
