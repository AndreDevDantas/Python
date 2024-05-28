import tkinter
from tkinter import ttk

#Instanciar a janela
janela = tkinter.Tk()

#declaração de variaveis
nome, telefone = tkinter.StringVar(), tkinter.StringVar()

def button_click():
    print(f"nome: {nome.get()}, telefone: {telefone.get()}")

ttk.Label(janela, text="Nome").grid(column=10, row=10)
ttk.Entry(janela, textvariable=nome).grid(colum=20, row=10)

ttk.Label(janela,text="Telefone").grid(column=10, row=20)