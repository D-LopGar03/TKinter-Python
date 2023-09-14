from tkinter import Scrollbar # Importamos la barra de desplazamiento vertical
import tkinter as tk
from tkinter import ttk
import fourth, sixth


def back_Pag4(root):
    root.destroy()
    fourth.page4(root)

def go_page6(root):
    root.destroy()
    sixth.page6(root)

def page5(root):
    root = tk.Tk()
    root.configure(bg="#8DFA3F")
    root.attributes('-fullscreen', True)

    root.title("TKinter essential") # Este atributo de la pantalla principal nos permite que al iniciar el programa este llene toda la pantalla 
    root.attributes('-fullscreen', True)

    # Crear el frame de la barra de navegación en la parte superior
    navbar_frame = tk.Frame(root, bg="black")
    navbar_frame.pack(side="top", fill="x")

    # Crear un widget Frame para contener el texto y la barra de desplazaadvance_Pag3miento
    frame = tk.Frame(root)
    frame.configure(bg="#8DFA3F")
    frame.pack(fill=tk.BOTH, expand=True)
    
    texto_largo ="""Una etiqueta en una interfaz gráfica de usuario (GUI) es un elemento de texto que se utiliza para nombrar y describir otros elementos de la interfaz, como botones o campos de entrada. \n\nSu propósito principal es proporcionar información y contexto a los usuarios sobre la función o el propósito de esos elementos en la GUI. \n\nEsto ayuda a los usuarios a comprender y utilizar la interfaz de manera más efectiva."""
    codigo = """\nimport tkinter as tk # CON LA PALABRA RESERVADA 'IMPORT' SE IMPORTAN LAS LIBRERÍAS

root = tk.Tk() # <- SE DECLARA LA VENTANA PRINCIPAL DEL PROGRAMA
root.title("TKinter essential") # <- LE DAMOS UN TÍTULO A LA VENTAiNA 

boton_ejemplo = tk.Button(root, text="SUMAR") 
# <- ESTAMOS DECLARANDO EL BOTÓN, con el primer parámetro lo que hacemos es asociarlo a la ventana para que tenga donde mostrarse y el segundo es el texto que queremos darle
boton_ejemplo.pack = (side="buttom")

label_ejemplo = tk.Label(root, text="SOY UNA ETIQUETA DE EJEMPLO")
labael.place(x = 100, y = 100)

root.mainloop()

"""
    label = tk.Label(frame, text="ETIQUETANDO CON LOS LABELS", font=("Impact", 20), fg="#067FFF", bg="#8DFA3F")
    label.pack(padx=10, pady=10)


    # Cargar imagen del disco.
    label_Etiqueta = tk.PhotoImage(file="images/label.png/")

    # Se modifica el tamaño de la imagen
    new_Image_tk = label_Etiqueta.subsample(3)

    # Insertarla en una etiqueta.
    img = tk.Label(frame, image=new_Image_tk, bg="#8DFA3F")
    img.pack(padx= 1, pady= 10)

    # Creando un label para explicar como funciona 

    label_Texto = tk.Label(frame, text=texto_largo)
    label_Texto.configure(bg="#8DFA3F")
    label_Texto.pack(padx = 5)   

    text_widget = tk.Text(frame, wrap='none', font=("Consolas", 10), fg="green", background="black")
    text_widget.place(x= 650, y= 250)
    text_widget.config(state="normal")
    text_widget.insert("1.0", codigo)
    text_widget.config(state="disabled")

    # Agregar una barra de desplazamiento vertical
    scrollbar = Scrollbar(frame, orient="vertical", command=text_widget.xview)
    scrollbar.pack(side="right", fill="y")

    style = ttk.Style()
    style.configure("RoundedButton.TButton", relief="raised", background="#ffffff", 
                    foreground="#000000", borderwidth=5, font=("Consolas", 12), padding=2, bordercolor="#000000", focuscolor="#2ACA9C", focusthickness=1, 
                    width="300", anchor="center")
    style.map("RoundedButton.TButton", background=[('active', "#26E569"), ('pressed', "#000000")])

    # Cargar la imagen de BOTÓN ATRÁS
    back_Pag3_Button = tk.PhotoImage(file="images/back.png")

    # Redimensionar la imagen de BOTÓN ATRÁS

    back_Pag3_Button_redimensionado = back_Pag3_Button.subsample(30,30)

    # Crear el botón con la imagen de BOTÓN ATRÁS
    back_Pag3_Button_Button = ttk.Button(navbar_frame, image=back_Pag3_Button_redimensionado, command=lambda:back_Pag4(root), style="RoundedButton.TButton")
    back_Pag3_Button_Button.pack(side="left", padx=10)

    # Cargar la imagen de BOTÓN ADELANTE
    go_Page6_Button = tk.PhotoImage(file="images/next.png")

    # Redimensionar la imagen de BOTÓN ADELANTE

    go_Page6_Button_redimensionado = go_Page6_Button.subsample(30,30)

    # Crear el botón con la imagen de BOTÓN ADELANTE
    go_Page6_Button_Button = ttk.Button(navbar_frame, image=go_Page6_Button_redimensionado, command=lambda:go_page6(root), style="RoundedButton.TButton")
    go_Page6_Button_Button.pack(side="left", padx=1.5)


    # Boton de salida, el cual se asocia al NAVBAR_FRAME
    exit_Button = tk.Button(navbar_frame, text = "X", command=root.destroy)
    exit_Button.pack(side="right", padx=2.5)

    root.mainloop()
