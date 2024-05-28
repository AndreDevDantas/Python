import tkinter as tk
janela = tk.Tk()
texto = tk.Text(janela, height=2, width=30)
texto.pack()
texto.insert(tk.END, "Este é um texto \ncom duas linhas")

janela.mainloop()