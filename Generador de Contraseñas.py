import random
import string
import tkinter as tk
from tkinter import messagebox

def generar_contrasena(longitud):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contrasena = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contrasena

def generar_contrasena_click():
    try:
        longitud = int(entry_longitud.get())
        contrasena_generada = generar_contrasena(longitud)
        resultado.config(text="Contraseña generada: " + contrasena_generada)
    except ValueError:
        messagebox.showerror("Error", "Por favor ingresa un valor numérico válido")

# Crear la ventana
ventana = tk.Tk()
ventana.title("Generador de Contraseñas")

# Etiqueta y entrada para la longitud de la contraseña
etiqueta_longitud = tk.Label(ventana, text="Longitud de la contraseña:")
etiqueta_longitud.pack()

entry_longitud = tk.Entry(ventana)
entry_longitud.pack()

# Botón para generar contraseña
boton_generar = tk.Button(ventana, text="Generar Contraseña", command=generar_contrasena_click)
boton_generar.pack()

# Etiqueta para mostrar el resultado
resultado = tk.Label(ventana, text="")
resultado.pack()

# Iniciar el bucle principal de la ventana
ventana.mainloop()