# 클래스 내부의 클래스를 사용하여 위젯을 상속하고 거기에 사용자 정의 부분을 추가하면 복잡한 레이아웃이 생성될 수 있다
# 결국엔 많은 클래스를 만들게 된다.
# 즉, 기능적인 접근 방식이란 점을 설명하기에는 약간 짜증나는 클래스가 많을 수 있다.
# 함수 내부에 위젯을 생성하고 반환하면 레이아수에 대해 더 제안적이비나 더 작은 구성 요소를 만들 때 더 쉽게 정리할 수 있다.

import ttkbootstrap as ttk

def create_segment(parent, label_text, button_text):
    frame = ttk.Frame(master=parent)

    # grid layout
    frame.rowconfigure(0, weight=1)
    frame.columnconfigure((0, 1, 2), weight=1, uniform='a')

    # widgets
    ttk.Label(frame, text=label_text).grid(row=0, column=0, sticky='nsew')
    ttk.Button(frame, text=button_text).grid(row=0, column=1, sticky='nsew')

    return frame


class Segment(ttk.Frame):
    def __init__(self, parent, label_text, button_text, exercise_text):
        super().__init__(master=parent)

        # gird layout
        self.rowconfigure(0, weight=1)
        self.columnconfigure((0, 1, 2), weight=1, uniform='a')

        # widgets
        ttk.Label(self, text=label_text).grid(row=0, column=0, sticky='nsew')
        ttk.Button(self, text=button_text).grid(row=0, column=1, sticky='nsew')
        self.create_exercise_box(exercise_text).grid(
            row=0, column=3, sticky='nsew')

        self.pack(expand=True, fill='both', padx=10, pady=10)

    def create_exercise_box(self, text):
        frame = ttk.Frame(master=self)
        ttk.Entry(frame).pack(expand=True, fill='both')
        ttk.Button(frame, text=text).pack(expand=True, fill='both', pady=10)
        return frame


# window
root = ttk.Window()
root.title('Understanding tkinter layout')
root.geometry('400x600+800+400')

# widgets => class
Segment(root, 'label', 'button', 'test')
Segment(root, 'test', 'click', 'something else')
Segment(root, 'hello', 'test', '123')
Segment(root, 'bye', 'launch', '^^')
Segment(root, 'last one', 'exit', 'end')

# widgets => function
# create_segment(root, 'label', 'button').pack(expand=True, fill='both', padx=10, pady=10)
# create_segment(root, 'test', 'click').pack(expand=True, fill='both', padx=10, pady=10)
# create_segment(root, 'hello', 'test').pack(expand=True, fill='both', padx=10, pady=10)
# create_segment(root, 'bye', 'launch').pack(expand=True, fill='both', padx=10, pady=10)
# create_segment(root, 'last one', 'exit').pack(expand=True, fill='both', padx=10, pady=10)

# run
root.mainloop()
