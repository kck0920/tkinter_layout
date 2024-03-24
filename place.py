# Widgets are placed by specifying the left, top, width, and height
# These numbers can be absolute or relative

from tkinter import *
import ttkbootstrap as ttk

# window
window = ttk.Window(themename="superhero")
window.title("Place intro")
window.geometry("400x600+1200+300")

#widgets
label1 = ttk.Label(window, text='Label 1', background='red')
label2 = ttk.Label(window, text='Label 2', background='blue')
label3 = ttk.Label(window, text='Label 3', background='green')
button = ttk.Button(window, text='Button', bootstyle='info')

# layout
label1.place(x=300, y=100, width=100, height=200)
label2.place(relx=0.2, rely=0.1, relwidth=0.3, relheight=0.5)
label3.place(x=80, y=60, width=160, height=300)
button.place(relx=1, rely=1, anchor='se')

# frame
frame = ttk.Frame(window)
frame_label = ttk.Label(frame, text='Frame label', background='yellow', foreground='black')
frame_button = ttk.Button(frame, text='Frame Button', bootstyle='success')

# frame_layout
frame.place(relx=0, rely=0, relwidth=0.3, relheight=1)
frame_label.place(relx=0, rely=0, relwidth=1, relheight=0.5)
frame_button.place(relx=0, rely=0.5, relwidth=1, relheight=0.5)

# exercise
exercise_label = ttk.Label(window, text='Exercise Label', background='orange')
# exercise layout
exercise_label.place(relx=0.5, rely=0.5, relwidth=0.5, height=200, anchor='center')

# exercise
# create a label and place it right in the center of the window
# the label should be half as wide as the window and be 200px tall


# run
window.mainloop()