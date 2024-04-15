import tkinter as tk
from rx.subject import Subject


class SliderExample:
    def __init__(self, master):
        self.master = master
        self.master.title("Slider Example")

        self.valueSubject = Subject()

        self.slider = tk.Scale(master, from_=1, to=200, orient=tk.HORIZONTAL, command=self.changeValue)
        self.slider.pack()

        self.canvas = tk.Canvas(master, width=250, height=250)
        self.canvas.pack()

        self.square = self.canvas.create_rectangle(50, 50, 50, 50, fill="blue")

    def changeValue(self, value):
        value = int(value)
        self.canvas.coords(self.square, 50, 50, 50 + value, 50 + value)
        # Отправляем значение через сигнал
        self.valueSubject.on_next(value)


def print_value(value):
    print("Value changed:", value)


def main():
    root = tk.Tk()
    app = SliderExample(root)

    # Подписываемся на сигнал и вызываем функцию print_value при получении сигнала
    app.valueSubject.subscribe(print_value)

    root.mainloop()


if __name__ == "__main__":
    main()


'''
import tkinter as tk


class SliderExample:
    def __init__(self, master):
        self.master = master
        self.master.title("Slider Example")

        self.slider = tk.Scale(master, from_=1, to=200, orient=tk.HORIZONTAL, command=self.changeValue)
        self.slider.pack()

        self.canvas = tk.Canvas(master, width=250, height=250)
        self.canvas.pack()

        self.square = self.canvas.create_rectangle(50, 50, 150, 150, fill="blue")

    def changeValue(self, value):
        value = int(value)
        self.canvas.coords(self.square, 50, 50, 50 + value, 50 + value)
        # Добавляем сигнал после изменения значения
        self.onValueChanged(value)

    def onValueChanged(self, value):
        # Вместо вывода значения на печать, здесь можно добавить код, который будет реагировать на изменение значения
        print("Value changed:", value)


def main():
    root = tk.Tk()
    app = SliderExample(root)
    root.mainloop()


if __name__ == "__main__":
    main()
'''