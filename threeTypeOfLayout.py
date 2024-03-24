from tkinter import *
import ttkbootstrap as ttk

# window
window = ttk.Window(themename='superhero')
window.title("Three Type of Layout")
window.geometry("600x400+1200+300")
window.config(bg='gray')

# widgets
label1 = ttk.Label(window, text='Label 1', background='red', foreground='white')
label2 = ttk.Label(window, text='Label 2', background='blue', foreground='white')
label3 = ttk.Label(window, text='Label 3', background='green', foreground='white')

# pack
# label1.pack(side='left', expand=True, fill='x')
# label2.pack(side='left', expand=True, fill='both')

# grid
# window.columnconfigure(0, weight=1)
# window.columnconfigure(1, weight=1)
# window.columnconfigure(2, weight=2)
# window.rowconfigure(0, weight=1)
# window.rowconfigure(1, weight=1)

# label1.grid(row=0, column=1, sticky='nsew')
# label2.grid(row=0, column=0, sticky='nsew')
# label3.grid(row=1, column=1, columnspan=2, sticky='nsew')

# place
label1.place(x=100, y=200, width=200, height=100)
label2.place(relx=0.5, rely=0.5, relwidth=1, anchor='se')




# run
window.mainloop()