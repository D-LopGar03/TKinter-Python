from tkinter import Scrollbar # Importamos la barra de desplazamiento vertical
import tkinter as tk
from tkinter import ttk
import second, fourth


def back_Pag2(root):
    root.destroy()
    second.page2(root)

def go_page4(root):
    root.destroy()
    fourth.page4(root)
    

def page3(root):
    root = tk.Tk()
    root.configure(bg="#70B8F6")
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
    frame.configure(bg="#70B8F6")
    frame.pack(fill=tk.BOTH, expand=True)
    
    texto_largo ="""\n\nSin embargo nuestro programa no podría funcionar de manera correcta porque nos falta un elemento fundamental, el método mainloop(), este lo que hace es no permitir que la ventana se ejecute y sin que nosotros lo veamos se cierre de manera inmediata, además hay algo muy interesante y es que podemos darle propiedades a nuestra ventana, tanto color, como un tamaño; en este momento te encuentras viendo la ventana a pantalla completa y todo eso se maneja a partir de los atributos de la misma ventana.
    
"""

    codigo = """\nimport tkinter as tk # CON LA PALABRA RESERVADA 'IMPORT' SE IMPORTAN LAS LIBRERÍAS

root = tk.Tk() # <- SE DECLARA LA VENTANA PRINCIPAL DEL PROGRAMA

# DANDO PROPIEDADES A LA VENTANA
root.configure(bg="white") # LE DAMOS COLOR A LA VENTANA, TOMA UNA GRAN VARIEDAD, TANTO EN LENGUAJE HUMANO COMO CÓDIGO HTML
root.resizable(0, 0)
root.geometry("800x450")
root.config(bg="black")
root.title("")


    # ACÁ ES DONDE VAN TODOS LOS ÍTEMS QUE ESTÁS VIENDO EN ESTE MISMO INSTANTE                                  

root.mainloop() # <- ESTE ES EL CICLO PRINCIPAL PARA QUE LA VENTANA NO SE CIERRE DE INMEDIATO


"""

    # Esto es el campo de texto donde aparece la variable texto_largo

    text_widget = tk.Text(frame, wrap=tk.WORD) # Este es para indicar al programa que debe de crear un campo de texto
    text_widget.place(x= 50, y= 100, width="550", height="250") # Indicamos donde queremos el elemento TEXT AREA
    text_widget.config(state="normal") # Permite la escritura del texto anterior
    text_widget.insert("1.0", texto_largo) # Inserta el texto y el "1.0" es para que se mantenga visible el TEXT AREA, de lo contario desaparece
    text_widget.config(state="disabled") # No deja editar el cuadro de texto, con el fin de solo ser lectura

    text_widget2 = tk.Text(frame, wrap='none', font=("Consolas", 10), fg="green", background="black")
    text_widget2.place(x= 650, y= 100, width="550", height="350")
    text_widget2.config(state="normal")
    text_widget2.insert("1.0", codigo)
    text_widget.config(state="disabled")

    # AGREGAR BARRA DE DESPLAZAMIENTO HORIZONTAL 
    
    scrollbar_in_x = Scrollbar(text_widget2, orient="horizontal", command=text_widget2.xview_moveto(2))
    scrollbar_in_x.pack(side="bottom", fill="x")

    # Configurar la vista del Text para usar la barra de desplazamiento
    text_widget2.config(xscrollcommand=scrollbar_in_x.set)

    style = ttk.Style()
    style.configure("RoundedButton.TButton", relief="raised", background="#ffffff", 
                    foreground="#000000", borderwidth=5, font=("Consolas", 12), padding=2, bordercolor="#000000", focuscolor="#2ACA9C", focusthickness=1, 
                    width="300", anchor="center")
    style.map("RoundedButton.TButton", background=[('active', "#26E569"), ('pressed', "#000000")])

    # Cargar la imagen de BOTÓN ATRÁS
    back_Pag2_Button = tk.PhotoImage(file="images/back.png")

    # Redimensionar la imagen de BOTÓN ATRÁS

    back_Pag2_Button_redimensionado = back_Pag2_Button.subsample(30,30)

    # Crear el botón con la imagen de BOTÓN ATRÁS
    back_Pag2_Button_Button = ttk.Button(navbar_frame, image=back_Pag2_Button_redimensionado, command=lambda:back_Pag2(root), style="RoundedButton.TButton")
    back_Pag2_Button_Button.pack(side="left", padx=10)

    # Cargar la imagen de BOTÓN ADELANTE
    advance_Pag3 = tk.PhotoImage(file="images/next.png")

    # Redimensionar la imagen de BOTÓN ADELANTE

    advance_Pag3_redimensionado = advance_Pag3.subsample(30,30)

    # Crear el botón con la imagen de BOTÓN ADELANTE
    advance_Pag3_Button = ttk.Button(navbar_frame, image=advance_Pag3_redimensionado, command=lambda:go_page4(root), style="RoundedButton.TButton")
    advance_Pag3_Button.pack(side="left", padx=1.5)



    # Boton de salida, el cual se asocia al NAVBAR_FRAME
    exit_Button = tk.Button(navbar_frame, text = "X", command=root.destroy)
    exit_Button.pack(side="right", padx=2.5)

    root.mainloop()
