from tkinter import Scrollbar # Importamos la barra de desplazamiento vertical
import tkinter as tk
from tkinter import ttk
import fifth

def back_Pag5(root):
    root.destroy()
    fifth.page5(root)

def page6(root):
    def cambiar_titulo():
        entrada = entrada_datos.get()
        label.config(text=entrada)
    root = tk.Tk()
    root.configure(bg="#A20AF4")
    root.attributes('-fullscreen', True)

    root.title("TKinter essential") # Este atributo de la pantalla principal nos permite que al iniciar el programa este llene toda la pantalla 
    root.attributes('-fullscreen', True)

    # Crear el frame de la barra de navegación en la parte superior
    navbar_frame = tk.Frame(root, bg="black")
    navbar_frame.pack(side="top", fill="x")

    # Crear un widget Frame para contener el texto y la barra de desplazaadvance_Pag3miento
    frame = tk.Frame(root)
    frame.configure(bg="#A20AF4")
    frame.pack(fill=tk.BOTH, expand=True)
    
    texto_largo ="""Por último vamos a hablar de los Entry box, o cajas de entrada\n\n
Un "entry box" es un elemento de una interfaz gráfica de usuario (GUI) que permite a los usuarios ingresar datos o texto, como nombres, números o contraseñas, en una casilla de entrada de texto."""
    codigo = """\nimport tkinter as tk # CON LA PALABRA RESERVADA 'IMPORT' SE IMPORTAN LAS LIBRERÍAS

root = tk.Tk() # <- SE DECLARA LA VENTANA PRINCIPAL DEL PROGRAMA
root.title("TKinter essential") # <- LE DAMOS UN TÍTULO A LA VENTAiNA 

boton_ejemplo = tk.Button(root, text="SUMAR") 
# <- ESTAMOS DECLARANDO EL BOTÓN, con el primer parámetro lo que hacemos es asociarlo a la ventana para que tenga donde mostrarse y el segundo es el texto que queremos darle
boton_ejemplo.pack = (side="buttom")

label_ejemplo = tk.Label(root, text="SOY UNA ETIQUETA DE EJEMPLO")
labael.place(x = 100, y = 100)

entry_Box_Ejemplo = tk.Entry(root, width=62)
entry_Box_Ejemplo.place(x=300, y=100)

root.mainloop()

"""
    label = tk.Label(frame, text="LA ENTRADA DE DATOS", font=("Impact", 20), fg="#000000", bg="#A20AF4")
    label.pack(padx=10, pady=10)
    
    entrada_datos = ttk.Entry(frame, width=62)
    entrada_datos.pack(padx=10, pady=11)

    boton = tk.Button(frame, text="Ingresa un dato", command=cambiar_titulo)
    boton.pack(padx=9, pady=10)
   
    text_widget = tk.Text(frame, wrap=tk.WORD) # Este es para indicar al programa que debe de crear un campo de texto
    text_widget.place(x= 50, y= 250, width="550", height="250") # Indicamos donde queremos el elemento TEXT AREA
    text_widget.config(state="normal") # Permite la escritura del texto anterior
    text_widget.insert("1.0", texto_largo) # Inserta el texto y el "1.0" es para que se mantenga visible el TEXT AREA, de lo contario desaparece
    text_widget.config(state="disabled") # No deja editar el cuadro de texto, con el fin de solo ser lectura

    text_widget2 = tk.Text(frame, wrap='none', font=("Consolas", 10), fg="green", background="black")
    text_widget2.place(x= 650, y= 250)
    text_widget2.config(state="normal")
    text_widget2.insert("1.0", codigo)
    text_widget2.config(state="disabled")

    # Agregar una barra de desplazamiento vertical
    scrollbar = Scrollbar(frame, orient="vertical", command=text_widget2.xview)
    scrollbar.pack(side="right", fill="y")

    style = ttk.Style()
    style.configure("RoundedButton.TButton", relief="raised", background="#ffffff", 
                    foreground="#000000", borderwidth=5, font=("Consolas", 12), padding=2, bordercolor="#000000", focuscolor="#2ACA9C", focusthickness=1, 
                    width="300", anchor="center")
    style.map("RoundedButton.TButton", background=[('active', "#26E569"), ('pressed', "#000000")])

    # Cargar la imagen de BOTÓN ATRÁS
    back_Pag4_Button = tk.PhotoImage(file="images/back.png")

    # Redimensionar la imagen de BOTÓN ATRÁS

    back_Pag4_Button_redimensionado = back_Pag4_Button.subsample(30,30)

    # Crear el botón con la imagen de BOTÓN ATRÁS
    back_Pag4_Button_Button = ttk.Button(navbar_frame, image=back_Pag4_Button_redimensionado, command=lambda:back_Pag5(root), style="RoundedButton.TButton")
    back_Pag4_Button_Button.pack(side="left", padx=10)

    # Boton de salida, el cual se asocia al NAVBAR_FRAME
    exit_Button = tk.Button(navbar_frame, text = "X", command=root.destroy)
    exit_Button.pack(side="right", padx=2.5)

    root.mainloop()
