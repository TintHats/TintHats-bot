 import tkinter as tk
import random

numero_secreto = random.randint(1, 100)
intentos = 0

def adivinar():
    global intentos, numero_secreto
    
    intento = int(entrada.get())
    intentos += 1
    entrada.delete(0, tk.END)
    
    if intento < numero_secreto:
        mensaje.config(text="¡Muy bajo! Intenta más alto", fg="red")
    elif intento > numero_secreto:
        mensaje.config(text="¡Muy alto! Intenta más bajo", fg="red")
    else:
        mensaje.config(text="🎉 ¡CORRECTO en " + str(intentos) + " intentos!", fg="green")

def nuevo_juego():
    global numero_secreto, intentos
    numero_secreto = random.randint(1, 100)
    intentos = 0
    mensaje.config(text="¡Adivina el número!", fg="white")

ventana = tk.Tk()
ventana.title("Adivina el número")
ventana.geometry("400x300")
ventana.config(bg="black")

tk.Label(ventana, text="Adivina el número (1-100)", font=("Arial", 16), bg="black", fg="white").pack(pady=20)

entrada = tk.Entry(ventana, font=("Arial", 18))
entrada.pack(pady=10)

tk.Button(ventana, text="Adivinar", font=("Arial", 14), command=adivinar).pack(pady=5)
tk.Button(ventana, text="Nuevo juego", font=("Arial", 14), command=nuevo_juego).pack(pady=5)

mensaje = tk.Label(ventana, text="¡Adivina el número!", font=("Arial", 14), bg="black", fg="white")
mensaje.pack(pady=20)

ventana.mainloop()