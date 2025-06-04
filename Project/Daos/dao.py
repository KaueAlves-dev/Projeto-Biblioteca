from dataclasses import dataclass
import sqlite3 as sql
from Project.Models.models import Livro, Cliente

@dataclass
class Dao:
  conn = None
  cursor = None

  def insert_livro(livro: Livro):
    try:

      conn = sql.connect('biblioteca.db')
      cursor = conn.cursor()

      cursor.execute('''INSERT INTO livros 
                     (titulo, autor, descricao, quantidade) 
                     VALUES(?,?,?,?)''', 
                     (livro.titulo, livro.autor, livro.descricao, livro.quantidade))
      conn.commit()

    finally:
      conn.close()  

  def insert_cliente():
    pass

  def insert_emprestimo():
    pass   
