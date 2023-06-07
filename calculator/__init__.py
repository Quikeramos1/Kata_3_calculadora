import tkinter as tk
from .controls import Display, CalcButton

WIDTH = 272
HEIGHT = 300

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculadora")
        self.geometry(f"{WIDTH}x{HEIGHT}")

        self.display = Display(self)
        self.display.pack()

        self.display.typing("198.368.681.654")

        CalcButton(self, self.clic1, "1").pack()
        CalcButton(self, text="2", tiny_wire=self.clic2).pack()
        CalcButton(self, text="3", tiny_wire=self.clic3).pack()
        CalcButton(self, text="4", tiny_wire=self.clic4).pack()

        self.display2 = Display(self)
        self.display2.pack()
        

    def clic1(self):
        self.display.typing("1")

    def clic2(self):
        self.display2.typing("2")  

    def clic3(self):
        self.display.typing("3")  

    def clic4(self):
        self.display2.typing("4")  
