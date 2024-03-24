# Pack becomes much easier to use when you combine it with frames
# You always create layouts in a single direction
# But some items are frames that contain their own layout

from tkinter import *
import ttkbootstrap as ttk

# window
window = ttk.Window(themename="superhero")
window.title("Pack + Frames")
window.geometry("450x700+1200+300")

# Top frame
top_frame = ttk.Frame(window)


# widget
label1 = ttk.Label(top_frame, text='First label', background='red')
label2 = ttk.Label(top_frame, text='label2', background='blue')
label3 = ttk.Label(window, text='Another label', background='green')

# bottom frame
bottom_frame = ttk.Frame(window)
button1 = ttk.Button(bottom_frame, text='A Button')
label4 = ttk.Label(bottom_frame, text='Last of the labels', background='orange')
button2 = ttk.Button(bottom_frame, text='Anther Button')

# exercise widgets
exercise_frame = ttk.Frame(bottom_frame)
button3 = ttk.Button(exercise_frame, text='Button3')
button4 = ttk.Button(exercise_frame, text='Button4')
button5 = ttk.Button(exercise_frame, text='Button5')

# top layout
label1.pack(fill='both', expand=True)
label2.pack(fill='both', expand=True)
top_frame.pack(fill='both', expand=True)

# middle layout
label3.pack(expand=True)

# bottom layout
button1.pack(side='left', padx=2, expand=True, fill='both')
label4.pack(side='left', padx=2, expand=True, fill='both')
button2.pack(side='left', padx=2, expand=True, fill='both')
bottom_frame.pack(padx=20, pady=20, fill='both', expand=True)

# exercise
# create 3 more buttons and another frame
# the frame should be on the right inside of the bottom frame
# and the buttons should be stacked vertically inside of it.

# exercise layout
button3.pack(padx=2, expand=True, fill='both')
button4.pack(padx=2, expand=True, fill='both')
button5.pack(padx=2, expand=True, fill='both')
exercise_frame.pack(side='left', fill='both', expand=True)

# run
window.mainloop()