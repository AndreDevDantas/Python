import tkinter as tk
contador = 0
def contador_label(lblRotulo):
    def funcao_contar():
        global contador
        contador += 1
        lblRotulo.config(text = str(contador))
        lblRotulo.after(1000, funcao_contar)
    funcao_contar()

janela = tk.Tk()
janela.title("Contagem Segundos")
lblrotulo = tk.Label(janela, fg = "red")
lblrotulo.pack()
contador_label(lblrotulo)
btnAcao = tk.Button(janela, text = "Clique aqui para interromper a contagem", width=50, fg="yellow", bg="black", command= janela.destroy)
btnAcao.pack()
janela.mainloop()
