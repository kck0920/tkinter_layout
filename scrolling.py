# There are 3 widgets that can be scrolled:
# Canvas, Text and Treeview
# Canvas is the most useful once since it can display widgets.

import ttkbootstrap as ttk
from random import randint, choice

# setup
window = ttk.Window()
window.title("Scrolling") 
window.geometry("600x400+800+400")

# Canvas
# canvas = ttk.Canvas(window, bg='red', scrollregion=(0, 0, 2000, 5000))
# canvas.create_line(0, 0, 2000, 5000, fill='green', width=10)
# for i in range(100):
#     l = randint(0,2000)
#     t = randint(0,5000)
#     r = l + randint(10,500)
#     b = t + randint(10,500)
#     color = choice(('red', 'blue', 'green', 'yellow', 'purple'))
#     canvas.create_rectangle(l,t,r,b,fill=color)
# canvas.pack(fill='both', expand=True)

# # mousewheel scrolling
# canvas.bind('<MouseWheel>', lambda e: canvas.yview_scroll(int(-1*(e.delta/60)), 'units'))


# # scrollbar
# scrollbar = ttk.Scrollbar(window, orient='vertical', command=canvas.yview)
# canvas.configure(yscrollcommand=scrollbar.set)
# scrollbar.place(relx=1, rely=0, relheight=1, anchor='ne')

# # exercise
# # create a horizontal scrollbar at the bottom and use it to scroll the canvas left and right
# scrollbar_bottom = ttk.Scrollbar(window, orient='horizontal', command=canvas.xview)
# canvas.configure(xscrollcommand=scrollbar.set)
# scrollbar_bottom.place(relx=0, rely=1, relwidth=1, anchor='sw')

# # also add an event to scroll left / right on Ctrl + mousewheel
# canvas.bind('<Control-MouseWheel>', lambda e: canvas.xview_scroll(int(-1*(e.delta/60)), 'units'))

# text
# text = ttk.Text(window)
# for i in range(1, 200):
#     text.insert(f'{i}.0', f'text: {i} \n')

# scrollbar_text = ttk.Scrollbar(window, orient='vertical', command=text.yview)
# text.configure(yscrollcommand=scrollbar_text.set)
# scrollbar_text.place(relx=1, rely=0, relheight=1, anchor='ne')

# treeview
table = ttk.Treeview(window, columns=(1,2), show='headings')
table.heading(1, text='First name')
table.heading(2, text='Last name')
first_names = ['John', 'Jane', 'Bob', 'Alice', 'Tom', 'Sue']
last_names = ['Smith', 'Johnson', 'Brown', 'Davis', 'Miller', 'Wilson']
for i in range(100):
    table.insert(parent='', index = ttk.END, values = (choice(first_names), choice(last_names)))
table.pack(fill='both', expand=True)

scrollbar_table = ttk.Scrollbar(window, orient='vertical', command=table.yview)
table.configure(yscrollcommand=scrollbar_table.set)
scrollbar_table.place(relx=1, rely=0, relheight=1, anchor='ne')

# run window
window.mainloop()