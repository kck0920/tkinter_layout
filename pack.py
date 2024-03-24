from tkinter import *
import ttkbootstrap as ttk

# window
window = ttk.Window(themename="superhero")
window.title("Pack Intro")
window.geometry("400x700+1200+300")

# widget
label1 = ttk.Label(window, text='First label', background='red')
label2 = ttk.Label(window, text='Second label', background='blue')
label3 = ttk.Label(window, text='Last of the labels', background='green')
button = ttk.Button(window, text='Button')

# pack option
# side: top, bottom, left, right
# expand: True, False
# fill: x, y, both, none
# anchor: n, s, e, w, ne, se, nw, sw
# padx, pady, ipadx, ipady
# in_ = window.winfo_children()
# By default, a widget will only be as big as its contents.
label1.pack(side='top', expand=True, fill='both')
label2.pack(side='left', expand=True, fill='both')
label3.pack(side='top', expand=True, fill='both')
button.pack(side='top', expand=True, fill='both')

# run
window.mainloop()