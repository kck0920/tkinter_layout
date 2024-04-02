# 위젯을 실제로 숨기거나 표시하는 것이 아니라 레이아웃에 위젯을 제거하고 추가한다.

from tkinter import *
import ttkbootstrap as ttk

# window
window = ttk.Window(themename="superhero")
window.title("Hide widgets")
window.geometry("600x400+1200+300")

# place
    
def toggle_label_visibility():
    global label_visible

    if label_visible:
        label.place_forget()  # 위젯을 제거한다. 위젯을 제거하면 위젯의 위치가 변경되어 위젯이 다시 표시된다.  
        label_visible = False
    else:
        label.place(relx=0.5, rely=0.5, anchor='center')
        abel_visible = True

button = ttk.Button(window, text='toggle Label', command=toggle_label_visibility, bootstyle='info')
button.place(relx=0.5, rely=0.965, anchor='center')

label_visible = True
label = ttk.Label(window, text='A label')
label.place(relx=0.5, rely=0.5, anchor='center')

# grid

# def on_button_click():

#     def toggle_label_grid():
#         global label_visible
        
#         if label_visible:
#             label.grid_forget()
#             label_visible = False
#         else:
#             label.grid(row=0, column=1)
#             label_visible = True
    
#     toggle_label_grid()
            

# window.columnconfigure((0,1), weight=1, uniform='a')
# window.rowconfigure(0, weight=1, uniform='a') 

# button = ttk.Button(window, text='toggle Label', command=on_button_click, bootstyle='info')
# button.grid(row=0, column=0)

# label_visible = True
# label = ttk.Label(window, text='A label')
# label.grid(row=0, column=1)


# pack
# def toggle_label_pack():
#     global label_visible
    
#     if label_visible:
#         label.pack_forget()
#         label_visible = False
#         frame.pack(expand=True, before=button)
#     else:
#         label.pack(expand=True, before=button)
#         label_visible = True
#         frame.pack_forget()



# label_visible = True
# label = ttk.Label(window, text='A label', background='red')
# label.pack(expand=True)

# button = ttk.Button(window, text='toggle Label', command=toggle_label_pack, bootstyle='info')
# button.pack()

# frame = ttk.Frame(window)

# run
window.mainloop()
