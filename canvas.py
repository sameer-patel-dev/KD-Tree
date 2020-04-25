from kdtree import *
import tkinter as tk
from tkinter import *
from nn_search import *

root= tk.Tk()

#point_list=[(7,2), (5,4), (9,6), (4,7), (8,1), (2,3)]
point_list = []
canvas1 = tk.Canvas(root, width = 800, height = 500,  relief = 'raised')
canvas1.pack()
canvas1.configure(background='white')
label1 = tk.Label(root, text='Visualization of KD Tree')
label1.config(font=('helvetica', 14),bg="white")
canvas1.create_window(400, 25, window=label1)


label2 = tk.Label(root, text='Insert')
label2.config(font=('helvetica', 10),bg='white')
canvas1.create_window(120, 70, window=label2)

entry1 = tk.Entry (root) 
canvas1.create_window(120, 90, window=entry1)

label3 = tk.Label(root,text='Delete')
label3.config(font=('helvetica',10),bg='white')
canvas1.create_window(300, 70, window=label3)

entry3 = tk.Entry (root) 
canvas1.create_window(300, 90, window=entry3)


label4 = tk.Label(root,text='search')
label4.config(font=('helvetica',10),bg='white')
canvas1.create_window(480, 70, window=label4)

entry4 = tk.Entry (root) 
canvas1.create_window(480, 90, window=entry4)

def insert_to ():
    
    x1 = entry1.get()
    x2= x1.split(',')
    x3 = (int(x2[0]),int(x2[1]))
    point_list.append(x3)
    main(point_list)
    canvas1.create_rectangle(0, 140, 800, 500,outline="#fff", fill="#fff")
    img = PhotoImage(file="graph.png")      
    canvas1.create_image(400, 250,anchor =NW, image=img)
    root.mainloop()
    
button1 = tk.Button(text='Add', command=insert_to, bg='brown', fg='white', font=('helvetica', 9, 'bold'))
canvas1.create_window(120, 120, window=button1)


def delete_from():
    x1 = entry3.get()
    x2= x1.split(',')
    result =[]
    for i in point_list:
        if i[0]!=int(x2[0]) and i[1]!= int(x2[1]):
            result.append(i)
    main(result)
    canvas1.create_rectangle(0, 140, 800, 500,outline="#fff", fill="#fff")
    img = PhotoImage(file="graph.png")
    canvas1.create_image(400, 250,anchor =NW, image=img)
    root.mainloop()

button3 = tk.Button(text='Delete', command=delete_from, bg='brown', fg='white', font=('helvetica', 9, 'bold'))
canvas1.create_window(300, 120, window=button3)


def show_nearest():
    x1 = entry4.get()
    x2= x1.split(',')
    p = (int(x2[0]),int(x2[1]))
    tree=get_tree(point_list)
    
    find_nearest(tree, p)
    label4 = tk.Label(root,text='search')
   
    

button4 = tk.Button(text='search', command=show_nearest, bg='brown', fg='white', font=('helvetica', 9, 'bold'))
canvas1.create_window(480, 120, window=button4)


