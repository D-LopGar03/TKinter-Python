import first
import tkinter as tk
from tkinter import ttk


def call_Page1(root):
    root.destroy()  # Cierra la ventana principal
    first.page1(root)

first.mostrar_Msgbox()

root = tk.Tk()
root.geometry('500x600+500+40')
root.config(background="black")
root.resizable(0, 0)
root.title("Menú")

label_Pregunta = tk.Label(root, text="¿Deseas comenzar con el tutorial?", font=("Impact", 20), fg="#00FFCD", bg="black")
label_Pregunta.place(x=65, y=50)

# Creamos un estilo para los botones

style = ttk.Style()
style.configure("RoundedButton.TButton", relief="raised", background="#50EC07", 
                foreground="#000000", borderwidth=5, font=("Consolas", 12), padding=2, bordercolor="#000000", focuscolor="#2ACA9C", focusthickness=1, 
                width="10", anchor="center")
style.map("RoundedButton.TButton", background=[('active', "#26E569"), ('pressed', "#000000")])

# Creamos los botones SI y NO

yes_button = ttk.Button(root, text="Sí", command=lambda:call_Page1(root), style='RoundedButton.TButton')
yes_button.place(x=195, y=250)

no_button = ttk.Button(root, text="No", command=lambda:root.quit(), style='RoundedButton.TButton')  # Cierra la aplicación si se selecciona "No"
no_button.place(x=195, y=350)

root.mainloop()
