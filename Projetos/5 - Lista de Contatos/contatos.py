import sqlite3 as conn
from os import path, getcwd
import tkinter as tk
 
dbpath = path.join(getcwd(), "banco", "telefones.sqlite")
 
def criar_db():
  with conn.connect(dbpath) as cx:
    query = """
      create table contatos (
        id integer primary key autoincrement,
        nome text not null,
        telefone text not null
      );
    """
    cursor = cx.cursor()
    cursor.execute(query)
 
def inserir(data = ()):
  with conn.connect(dbpath) as cx:
    query = "insert into contatos (nome, telefone) values (?,?);"
    cursor = cx.cursor()
    cursor.execute(query, data)
    print("dados inseridos com sucesso")
 
def alterar(data = ()):
  with conn.connect(dbpath) as cx:
    query = "update contatos set nome = ?, telefone = ? where id = ?;"
    cursor = cx.cursor()
    cursor.execute(query, data)
    print("dados alterados com sucesso")
 
def excluir(data = ()):
  with conn.connect(dbpath) as cx:
    query = "delete from contatos where id = ?;"
    cursor = cx.cursor()
    cursor.execute(query, data)
    print("dados excluídos com sucesso")
 
def listar():
  with conn.connect(dbpath) as cx:
    query = "select id, nome, telefone from contatos order by nome;"
    cursor = cx.cursor()
    cursor.execute(query)
    return cursor.fetchall()
 
def tabela(data):
  print("ID       Nome          Telefone")
  for item in data:
    print(f"{item[0]}       {item[1]}         {item[2]}")
 
def tela_inicial():
  janela = tk.Tk()
  janela.geometry("300x200")
  janela.title("Agenda Telefônica")
  janela.resizable(False, False)
 
 
 
  label_nome = tk.Label(text="Nome:")
  label_nome.pack()
 
  entry_nome = tk.Entry()
  entry_nome.pack()
 
  label_telefone = tk.Label(text="Telefone:")
  label_telefone.pack()
 
  entry_telefone = tk.Entry()
  entry_telefone.pack()
 
  def inserir_contato():
    nome = entry_nome.get()
    telefone = entry_telefone.get()
    inserir((nome, telefone))
    entry_nome.delete(0, tk.END)
    entry_telefone.delete(0, tk.END)
 
  def exportar_contatos():
    data = listar()
    with open('contatos.txt', 'w') as f:
      for item in data:
        f.write(','.join(map(str, item)) + '\n')
    print("Contatos exportados com sucesso para o arquivo contatos.txt")
 
  botao_inserir = tk.Button(text="Inserir", command=inserir_contato)
  botao_inserir.pack()
 
  botao_exportar = tk.Button(text="Exportar", command=exportar_contatos)
  botao_exportar.pack()
 
  janela.mainloop()
 
if __name__ == "__main__":
  tela_inicial()
 