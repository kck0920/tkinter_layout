# You can set the number of rows & columns
# You can set the width / height of each column / row
# Then you place widgets in a column & row
# Widgets can occupy multiple cells and have padding
# Like with pack, the grid only determines how much space a widget can occupy
# Sticky determines what are will be filled in the cell

from tkinter import *
import ttkbootstrap as ttk

# window
window = ttk.Window(themename="darkly")
window.title("Grid intro")
window.geometry("600x400+1200+300")
entry = ttk.Entry(window)

# widget
label1 = ttk.Label(window, text='Label 1', background='red')
label2 = ttk.Label(window, text='Label 2', background='blue')
label3 = ttk.Label(window, text='Label 3', background='green')
label4 = ttk.Label(window, text='Label 4', background='yellow', foreground='black')
button1 = ttk.Button(window, text='Button 1')
button2 = ttk.Button(window, text='Button 2')

# define a grid
window.columnconfigure((0,1,2), weight=1, uniform='a')
# window.columnconfigure(1, weight=1)
# window.columnconfigure(2, weight=1)
window.columnconfigure(3, weight=2, uniform='a')
window.rowconfigure(0, weight=1, uniform='a')
window.rowconfigure(1, weight=1, uniform='a')
window.rowconfigure(2, weight=1, uniform='a')
window.rowconfigure(3, weight=3, uniform='a')


# place a widget in a grid
label1.grid(row=0, column=0, sticky='nsew')
label2.grid(row=1, column=1, rowspan=3, sticky='nsew')
label3.grid(row=1, column=0, columnspan=3, sticky='nsew', padx=20, pady=10)
label4.grid(row=3, column=3, sticky='se')

# exercise
# add the buttons and the entry field to the grid
button1.grid(row=0, column=3, columnspan=2, sticky='nsew')
button2.grid(row=2, column=2, sticky='nsew')
entry.grid(row=2, column=3, rowspan=2)
# run
window.mainloop()