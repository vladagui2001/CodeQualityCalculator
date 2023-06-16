import tkinter as tk

# Configuración de la ventana principal
root = tk.Tk()
root.title("Calculadora")

def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(number))

def button_clear():
    entry.delete(0, tk.END)



root.mainloop()
