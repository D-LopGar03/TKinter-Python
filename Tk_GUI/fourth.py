from tkinter import Scrollbar # Importamos la barra de desplazamiento vertical
import tkinter as tk
from tkinter import ttk
import third, fifth


def back_Pag3(root):
    root.destroy()
    third.page3(root)

def go_page5(root):
    root.destroy()
    fifth.page5(root)

def show_Frames(frame, texto_largo, codigo, boton_ejemplo):
    # Esto es el campo de texto donde aparece la variable texto_largo

    text_widget = tk.Text(frame, wrap=tk.WORD, background="white") # Este es para indicar al programa que debe de crear un campo de texto
    text_widget.place(x= 50, y= 100, width="550", height="250") # Indicamos donde queremos el elemento TEXT AREA
    text_widget.config(state="normal") # Permite la escritura del texto anterior
    text_widget.insert("1.0", texto_largo) # Inserta el texto y el "1.0" es para que se mantenga visible el TEXT AREA, de lo contario desaparece
    text_widget.config(state="disabled") # No deja editar el cuadro de texto, con el fin de solo ser lectura

    text_widget2 = tk.Text(frame, wrap='none', font=("Consolas", 10), fg="green", background="black")
    text_widget2.place(x= 650, y= 100)
    text_widget2.config(state="normal")
    text_widget2.insert("1.0", codigo)
    text_widget2.config(state="disabled")

    # Agregar una barra de desplazamiento vertical
    scrollbar = Scrollbar(frame, orient="vertical", command=text_widget.yview)
    scrollbar.pack(side="right", fill="y")

    # Configurar la vista del Text para usar la barra de desplazamiento
    text_widget.config, text_widget.config(yscrollcommand=scrollbar.set)
    boton_ejemplo.config(state=tk.DISABLED)
        

def page4(root):
    root = tk.Tk()
    root.configure(bg="#FF5733")
    root.attributes('-fullscreen', True)

    root.title("TKinter essential") # Este atributo de la pantalla principal nos permite que al iniciar el programa este llene toda la pantalla 
    root.attributes('-fullscreen', True)

    # Crear el frame de la barra de navegación en la parte superior
    navbar_frame = tk.Frame(root, bg="black")
    navbar_frame.pack(side="top", fill="x")

    # Crear un widget Frame para contener el texto y la barra de desplazaadvance_Pag3miento
    frame = tk.Frame(root)
    frame.configure(bg="#FF5733")
    frame.pack(fill=tk.BOTH, expand=True)
    
    texto_largo ="""\n\nUn botón en una interfaz gráfica de usuario, normalmente llamada GUI, típicamente se muestra como un área rectangular con un texto o una imagen en su interior y, cuando un usuario hace clic en él, desencadena una función o acción asociada.
    \n\nPara declarar un botón se debe de llamar a la clase 'Button' de la librería TK, este debe de ser almacenado en una variable, no importa el nombre, pero preferiblemente que sea un nombre descriptivo.
"""
    codigo = """\nimport tkinter as tk # CON LA PALABRA RESERVADA 'IMPORT' SE IMPORTAN LAS LIBRERÍAS

root = tk.Tk() # <- SE DECLARA LA VENTANA PRINCIPAL DEL PROGRAMA
root.title("TKinter essential") # <- LE DAMOS UN TÍTULO A LA VENTAiNA 

boton_ejemplo = tk.Button(root, text="SUMAR") 
# <- ESTAMOS DECLARANDO EL BOTÓN, con el primer parámetro lo que hacemos es asociarlo a la ventana para que tenga donde mostrarse y el segundo es el texto que queremos darle
boton_ejemplo.pack = (side="buttom")

root.mainloop()

"""
    boton_ejemplo = tk.Button(frame, text="Haciendo clic en los botones", font=("Impact", 20), fg="red", command=lambda:show_Frames(frame, texto_largo, codigo, boton_ejemplo))
    boton_ejemplo.pack(padx=10, pady=10)

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
    back_Pag3_Button_Button = ttk.Button(navbar_frame, image=back_Pag3_Button_redimensionado, command=lambda:back_Pag3(root), style="RoundedButton.TButton")
    back_Pag3_Button_Button.pack(side="left", padx=10)

    # Cargar la imagen de BOTÓN ADELANTE
    go_Page5_Button = tk.PhotoImage(file="images/next.png")

    # Redimensionar la imagen de BOTÓN ADELANTE

    go_Page5_Button_redimensionado = go_Page5_Button.subsample(30,30)

    # Crear el botón con la imagen de BOTÓN ADELANTE
    go_Page5_Button_Button = ttk.Button(navbar_frame, image=go_Page5_Button_redimensionado, command=lambda:go_page5(root), style="RoundedButton.TButton")
    go_Page5_Button_Button.pack(side="left", padx=1.5)


    # Boton de salida, el cual se asocia al NAVBAR_FRAME
    exit_Button = tk.Button(navbar_frame, text = "X", command=root.destroy)
    exit_Button.pack(side="right", padx=2.5)

    root.mainloop()
