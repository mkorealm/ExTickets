import os
import tkinter as tk
import openpyxl

from tkinter import ttk

script_dir = os.path.dirname(__file__)

wb = openpyxl.load_workbook(filename=script_dir + "\\Данные.XLSX")
column = wb.worksheets[0]
lst = []
for row in column:
    lst.append(row[0].value)
print(lst)


class Windows(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.wm_title("Королев Максим 41ИС-19")

        container = tk.Frame(self, height=400, width=600)
        container.pack(side="top", fill="both", expand=True)

        self.frames = {}
        for F in (Main, First, Second):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(column=0, row=0, sticky="nsew")

        self.show_frame(Main)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class Main(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        lbl = tk.Label(self, text=f"Класс {__class__.__name__}")
        lbl.pack()

        btn = tk.Button(self, text="Перейти на следующую страницу", command=lambda: controller.show_frame(First))
        btn.pack()


class First(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        lbl = tk.Label(self, text=f"Класс {__class__.__name__}")
        lbl.pack()

        btn = tk.Button(self, text="Перейти на следующую страницу", command=lambda: controller.show_frame(Second))
        btn.pack()


class Second(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        lbl = tk.Label(self, text=f"Класс {__class__.__name__}")
        lbl.pack()
