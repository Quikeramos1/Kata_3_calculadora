import tkinter as tk
from tkinter.font import Font



class Display(tk.Frame):
    def __init__(self, location):
        super().__init__(location, width=272, height=50)
        self.pack_propagate(False)
        self.label = tk.Label(self, background="#000000", text="", foreground="white",
                              anchor=tk.E, padx=10, pady=10, font=Font(family="Arial", size="30"))
        self.label.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    def typing(self, text):
        self.label.config(text=text)

    
class CalcButton(tk.Frame):
    def __init__(self, location, tiny_wire, text):
        super().__init__(location, width=68, height=50)
        self.pack_propagate(False)
        self.button = tk.Button(self, text=text, command=tiny_wire)
        self.button.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    def clic(self):
        Display.typing(self,"Total")

 
