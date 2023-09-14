from tkinter import Scrollbar # Importamos la barra de desplazamiento vertical
import tkinter as tk
from tkinter import ttk
import first, third

def back_Pag1(root):
    root.destroy()
    first.page1(root)

def go_page3(root):
    root.destroy()
    third.page3(root)


def page2(root):
    root = tk.Tk()
    root.configure(bg="#E5CB28")
    root.attributes('-fullscreen', True)

    root.title("TKinter essential") # Este atributo de la pantalla principal nos permite que al iniciar el programa este llene toda la pantalla 
    root.attributes('-fullscreen', True)

    # Crear el frame de la barra de navegación en la parte superior
    navbar_frame = tk.Frame(root, bg="black")
    navbar_frame.pack(side="top", fill="x")

    label = tk.Label(root, text="Empezando por lo principal, el contenedor", font=("Impact", 20), fg="red")
    label.pack(padx=10, pady=10)

    # Crear un widget Frame para contener el texto y la barra de desplazaadvance_Pag3miento
    frame = tk.Frame(root)
    frame.configure(bg="#E5CB28")
    frame.pack(fill=tk.BOTH, expand=True)
    
    texto_largo ="""root = Tk() en Python, específicamente en el contexto de la biblioteca gráfica Tkinter, crea la ventana principal de una aplicación de interfaz gráfica de usuario (GUI).\n
Tk(): Esto crea una ventana principal de Tkinter, que es la base de la interfaz gráfica.\n
root = Tk(): Asigna la instancia de la ventana principal a la variable root. Esta variable se usa para trabajar con la ventana principal, como agregar elementos y definir la funcionalidad de la GUI.\n
En resumen, root = Tk() es el primer paso para iniciar una aplicación GUI con Tkinter en Python, creando la ventana principal en la que se construirá la interfaz de usuario.""" 
   

    codigo = """\nimport tkinter as tk # CON LA PALABRA RESERVADA 'IMPORT' SE IMPORTAN LAS LIBRERÍAS

root = tk.Tk() # <- SE DECLARA LA VENTANA PRINCIPAL DEL PROGRAMA



"""

    # Esto es el campo de texto donde aparece la variable texto_largo

    text_widget = tk.Text(frame, wrap=tk.WORD) # Este es para indicar al programa que debe de crear un campo de texto
    text_widget.place(x= 650, y= 100) # Indicamos donde queremos el elemento TEXT AREA
    text_widget.config(state="normal") # Permite la escritura del texto anterior
    text_widget.insert("1.0", texto_largo) # Inserta el texto y el "1.0" es para que se mantenga visible el TEXT AREA, de lo contario desaparece
    text_widget.config(state="disabled") # No deja editar el cuadro de texto, con el fin de solo ser lectura

    text_widget2 = tk.Text(frame, wrap=tk.WORD, font=("Consolas", 10), fg="green", background="black")
    text_widget2.place(x= 50, y= 100, width="550", height="100")
    text_widget2.config(state="normal")
    text_widget2.insert("1.0", codigo)
    text_widget.config(state="disabled")

    # Agregar una barra de desplazamiento vertical
    scrollbar = Scrollbar(frame, orient="vertical", command=text_widget.yview)
    scrollbar.pack(side="right", fill="y")

    # Configurar la vista del Text para usar la barra de desplazamiento
    text_widget.config, text_widget.config(yscrollcommand=scrollbar.set)

    style = ttk.Style()
    style.configure("RoundedButton.TButton", relief="raised", background="#ffffff", 
                    foreground="#000000", borderwidth=5, font=("Consolas", 12), padding=2, bordercolor="#000000", focuscolor="#2ACA9C", focusthickness=1, 
                    width="300", anchor="center")
    style.map("RoundedButton.TButton", background=[('active', "#26E569"), ('pressed', "#000000")])

    # Cargar la imagen de BOTÓN ATRÁS
    back_Pag1_Button = tk.PhotoImage(file="images/back.png")

    # Redimensionar la imagen de BOTÓN ATRÁS

    back_Pag1_Button_redimensionado = back_Pag1_Button.subsample(30,30)

    # Crear el botón con la imagen de BOTÓN ATRÁS
    back_Pag1_Button_Button = ttk.Button(navbar_frame, image=back_Pag1_Button_redimensionado, command=lambda:back_Pag1(root), style="RoundedButton.TButton")
    back_Pag1_Button_Button.pack(side="left", padx=10)

    # Cargar la imagen de BOTÓN ADELANTE
    advance_Pag3 = tk.PhotoImage(file="images/next.png")

    # Redimensionar la imagen de BOTÓN ADELANTE

    advance_Pag3_redimensionado = advance_Pag3.subsample(30,30)

    # Crear el botón con la imagen de BOTÓN ADELANTE
    advance_Pag3_Button = ttk.Button(navbar_frame, image=advance_Pag3_redimensionado, command=lambda:go_page3(root), style="RoundedButton.TButton")
    advance_Pag3_Button.pack(side="left", padx=1.5)


    # Boton de salida, el cual se asocia al NAVBAR_FRAME
    exit_Button = tk.Button(navbar_frame, text = "X", command=root.destroy)
    exit_Button.pack(side="right", padx=2.5)

    root.mainloop()
