import tkinter as tk
janela = tk.Tk()
janela.geometry('300x50')
janela.title('Jokenpo 3')
botao = tk.Button(janela, text = 'Fechar Janela', width = 25, height = 30, command = janela.destroy)


botao.pack()
janela.mainloop()