#importamos tkinter y le asignamos la variable tk
import tkinter as tk

#creo una funcion que necesitaremos luego para mostrar en pantalla "hola + el texto que introduzcamos"

def imprimir_saludo():
    print("Por aqui pasa")
    label.config(text=f"Hola, {valor_nombre.get()}")

#Creamos las ventanas
root = tk.Tk()

#ponemos un titulo de ventana
root.title("App de Quike")

#ahora le damos dimension a la ventana 800x600 y localizacion en pantalla 400+200
root.geometry("800x600+400+200")

#Ahora vamos a instalar controles que sean etiquetas con un borde de 2 pixeles y un relieve que sobresale

label = tk.Label(root, text="", bd=2,relief=tk.RAISED, width=50)

#le doy una posición en la ventana, en esta ocasion con valores predeterminados
label.pack()


#ahora vamos a instalar otro control, en este caso sera uno de entrada (Tipo input)

valor_nombre = tk.StringVar() #esto lo creo para poder almacenar lo que introduzcamos en el control de input

nombre = tk.Entry(root, textvariable=valor_nombre)
nombre.pack()

#ahora creamos un botón con un texto "Púlsame" y una acción command que viene de una funcion creada anteriormente ""imprimir_saludo"

boton = tk.Button(root, text ="Púlsame", command=imprimir_saludo)
boton.pack()

#ejecuta la ventana de la aplicación
root.mainloop()