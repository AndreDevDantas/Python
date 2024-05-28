import tkinter as tk

root = tk.Tk()
root.geometry("400x300")
root.title("Lista de Tecnologias")
listbox = tk.Listbox()
itens = tk.StringVar()
itens.set(
    "Python "
    "C "
    "C++ "
    "JavaScript "
)
listbox = tk.Listbox(listvariable=itens)
listbox.pack()
root.mainloop()