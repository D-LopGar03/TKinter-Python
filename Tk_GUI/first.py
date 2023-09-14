import tkinter as tk # Se importa la librería de TKinter para poder iniciar con el proyecto
from tkinter import messagebox as mbox # Lo usamos para poder obtener un mensaje de advertencia en la pantalla
from tkinter import Scrollbar # Importamos la barra de desplazamiento vertical
from tkinter import ttk # Con esta librería manipulamos las imágenes
import second

def mostrar_Msgbox():
    mbox.showinfo(message="En este tutorial te voy a enseñar a manejar lo esencial de TKinter para que puedas desarrollar tu lógica de programación mientras dejas volar tu imaginación.", title="TKinter essentials")  # Mostramos un mensaje en pantalla

def go_page2(root):
    root.destroy()
    second.page2(root)

def page1(root):

    root = tk.Tk()  # Esta línea y la del final que dice root.mainloop() son las que hacen que aparezca la parte gráfica en la pantalla

    # root.configure(width = 1080, height = 1040) Esta línea hace que la interfaz se vea con una altura(Y) y anchura(X) específica

    root.title("TKinter essential") 
    root.attributes('-fullscreen', True) # Este atributo de la pantalla principal nos permite que al iniciar el programa este llene toda la pantalla 
    root.configure(background="#AAFF00")

    # Crear el frame de la barra de navegación en la parte superior
    navbar_frame = tk.Frame(root, bg="black")
    navbar_frame.pack(side="top", fill="x")

    label = tk.Label(root, text="Lo esencial de TKinter", font=("Impact", 20), fg="red", bg="#AAFF00")
    label.pack(padx=10, pady=10)


    # Crear un widget Frame para contener el texto y la barra de desplazamiento
    frame = tk.Frame(root)
    frame.configure(background="#AAFF00")
    frame.pack(fill=tk.BOTH, expand=True)

    # Cargar imagen del disco.
    tkinter_logo = tk.PhotoImage(file="images/tkinter.png/")

    # Se modifica el tamaño de la imagen
    new_Image_tk = tkinter_logo.subsample(3)

    # Insertarla en una etiqueta.
    img = ttk.Label(image=new_Image_tk, background="#AAFF00")
    img.place(x = 850, y = 200)

    style = ttk.Style()
    style.configure("RoundedButton.TButton", relief="raised", background="#ffffff", 
                    foreground="#000000", borderwidth=5, font=("Consolas", 12), padding=2, bordercolor="#000000", focuscolor="#2ACA9C", focusthickness=1, 
                    width="300", anchor="center")
    style.map("RoundedButton.TButton", background=[('active', "#26E569"), ('pressed', "#000000")])

    # Cargar la imagen de BOTÓN ADELANTE
    advance_Pag2 = tk.PhotoImage(file="images/next.png")

    # Redimensionar la imagen de BOTÓN ADELANTE

    advance_Pag2_redimensionado = advance_Pag2.subsample(30,30)

    # Crear el botón con la imagen de BOTÓN ADELANTE
    advance_Pag2_Button = ttk.Button(navbar_frame, image=advance_Pag2_redimensionado, command=lambda:go_page2(root), style="RoundedButton.TButton")
    advance_Pag2_Button.pack(side="left", padx=2.5)


    # Agregar un widget Label para mostrar el contenido del artículo (texto largo)

    texto_largo1 ="""Tk es una herramienta para desarrollar aplicaciones de escritorio multiplataforma, esto es, aplicaciones nativas con una interfaz gráfica para sistemas operativos Windows, Linux, Mac y otros.\n\nTécnicamente, Tk es una biblioteca de código abierto escrita en C y desarrollada en sus orígenes para el lenguaje de programación Tcl; de ahí que usualmente nos refiramos a ella como Tcl/Tk.\n\nDesde sus primeras versiones Python incluye en su biblioteca o librería estándar el módulo tkinter, que permite interactuar con Tk para desarrollar aplicaciones de escritorio en Python.\n\nLa curva de aprendizaje de Tk es relativamente pequeña si la comparamos con otras bibliotecas del rubro (como Qt), de modo que cualquier programador con una mínima base de Python puede comenzar rápidamente a crear aplicaciones gráficas profesionales y luego distribuirlas vía herramientas como cx_Freeze o PyInstaller, que se integran muy bien con Tk.
    """ 
    # Esto es el campo de texto donde aparece la variable texto_largo

    text_widget = tk.Text(frame, wrap=tk.WORD) # Este es para indicar al programa que debe de crear un campo de texto
    text_widget.place(x = 50, y = 50) # Indicamos donde queremos el elemento TEXT AREA
    text_widget.config(state="normal") # Permite la escritura del texto anterior
    text_widget.insert("1.0", texto_largo1) # Inserta el texto y el "1.0" es para que se mantenga visible el TEXT AREA, de lo contario desaparece
    text_widget.config(state="disabled") # No deja editar el cuadro de texto, con el fin de solo ser lectura

    # Agregar una barra de desplazamiento vertical
    scrollbar = Scrollbar(frame, orient="vertical", command=text_widget.yview)
    scrollbar.pack(side="right", fill="y")

    # Configurar la vista del Text para usar la barra de desplazamiento
    text_widget.config(yscrollcommand=scrollbar.set)

    # Agregar una barra de desplazamiento verticaldestroy

    # Botón para salir del programa

    exit_Button = tk.Button(navbar_frame, text = "X", command=root.destroy)
    exit_Button.pack(side="right", padx=1.5)

    root.mainloop() # Bucle infinito que no deja que desaparezca la interfaz

