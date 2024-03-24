# Widget can have a custom size
# But that size will be overwritten by the layout methods
# ttk.Label(parent, text='label', width=50).pack(fill='x')


from tkinter import *
import ttkbootstrap as ttk

# window
window = ttk.Window(themename="superhero")
window.title("Layout intro")
window.geometry("400x300+1200+300")

# widget
label1 = ttk.Label(window, text='Label 1', background='green')
label2 = ttk.Label(window, text='Label 2', background='red', width=50)  # 여기서 width는 무시된다

# layout
# label1.pack()
# label2.pack(fill='x')

# grid
window.columnconfigure((0,1), weight=1, uniform='a')
window.rowconfigure((0,1), weight=1, uniform='a')

label1.grid(row=0, column=0)
label2.grid(row=1, column=0, sticky='nsew')

# run
window.mainloop()