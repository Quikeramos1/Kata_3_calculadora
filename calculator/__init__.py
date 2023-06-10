import tkinter as tk
from .controls import Display, CalcButton, KeyBoard
from cromannumbers import RomanNumber

WIDTH = 272
HEIGHT = 300

operaciones = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "x": lambda a, b: a * b,
    "÷": lambda a, b: a / b

}

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculadora")
        self.geometry(f"{WIDTH}x{HEIGHT}")
        self.op1 = None
        self.op2 = None
        self.operation = None
        self.value = ""
        self.resultado = None

        self.display = Display(self)
        self.display.pack()
        
        KeyBoard(self, self.clic).pack()

        self.display.typing("")
        

    def clic(self, tecla):
        if tecla == "AC":
            self.value = ""
            self.op1 = self.op2 = self.operation = None
        elif tecla in operaciones:
            self.op1 = RomanNumber(self.value)
            self.operation = tecla
        elif tecla == "=":
            self.op2 = RomanNumber(self.value)
            resultado = operaciones[self.operation](self.op1, self.op2)
            self.value = resultado.simbolo

            
        

        else:  
            if self.operation is not None and self.op2 is None:
                self.value = ""
                self.op2 = ""
            self.value += tecla

          
        self.display.typing(self.value)
        

        

        
    
