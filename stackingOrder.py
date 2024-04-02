# 위젯은 배치할 때가 아니라 생성될 때 항상 다른 위젯 위에 배치된다
# 위젯을 모든 위젯 또는 다른 위젯의 위에 올리 수 있다.

from tkinter import *
import ttkbootstrap as ttk

# window
window = ttk.Window(themename="superhero")
window.title("Stacking order")
window.geometry("400x400+1200+300")

# widgets
label1 = ttk.Label(window, text='Label 1', background='green')
label2 = ttk.Label(window, text='Label 2', background='red')

# label1.lift() # 위젯을 위로 올림 == label1.tkraise()
# label2.lower() # 위젯을 아래로 내림
# label1.tkraise(aboveThis=label2) # 위젯을 지정한 위젯 위에 올림

button1 = ttk.Button(window, text='raise label 1', command=lambda : label1.tkraise(aboveThis=label2))
button2 = ttk.Button(window, text='raise label 2', command=lambda : label2.tkraise())

# layout
label1.place(x=50, y=100, width=200, height=150)
label2.place(x=150, y=60, width=140, height=100)

button1.place(relx=0.75, rely=1, anchor='se')
button2.place(relx=1, rely=1, anchor='se')

# exercise
# add a third label and button 
label3 = ttk.Label(window, text='Label 3', background='blue')
label3.place(x=20, y=80, width=200, height=100)

button3 = ttk.Button(window, text='raise label 3', bootstyle='success',command=lambda : label3.tkraise())
button3.place(relx=0.5, rely=1, anchor='se')

# run
window.mainloop()