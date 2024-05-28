import tkinter as tk
janela = tk.Tk()
janela.title("Jokenpo")
label = tk.Label(janela, text = 'Exemplo Rótulo', background = 'black', foreground = 'white')

#Abreviando
label2 = tk.Label (janela, text = 'Exemplo 2', bg = 'blue', fg = 'red')

label.pack()
label2.pack()
janela.mainloop()
