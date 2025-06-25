from dataclasses import dataclass
import sqlite3 as sql
from models.models import Livro, Cliente, Emprestimo

@dataclass
class BibliotecaDao:

  @staticmethod
  def list_all_livros():
    
    try:

      conn = sql.connect('biblioteca.db')
      cursor = conn.cursor()

      query = cursor.execute('SELECT * FROM livros').fetchall()

      return query
    
    finally:
      conn.close() 

  @staticmethod
  def list_all_clientes():
    
    try:

      conn = sql.connect('biblioteca.db')
      cursor = conn.cursor()

      query = cursor.execute('SELECT * FROM clientes').fetchall()

      return query
    
    finally:
      conn.close()  
  @staticmethod
  def list_all_emprestimos():
    
    try:

      conn = sql.connect('biblioteca.db')
      cursor = conn.cursor()

      query = cursor.execute('SELECT * FROM emprestimos').fetchall()

      return query
    
    finally:
      conn.close()        

  @staticmethod
  def insert_livro(livro: Livro):
    try:

      conn = sql.connect('biblioteca.db')
      cursor = conn.cursor()

      cursor.execute('''INSERT INTO livros 
                     (titulo, autor, descricao, quantidade) 
                     VALUES(?,?,?,?)''', 
                     (livro.titulo, livro.autor, livro.descricao, livro.quantidade))
      conn.commit()

      return True

    finally:
      conn.close()  

  @staticmethod
  def insert_cliente(cliente: Cliente):
    try:

      conn = sql.connect('biblioteca.db')
      cursor = conn.cursor()

      cursor.execute('''INSERT INTO clientes 
                     (nome, telefone, email) 
                     VALUES(?,?,?)''', 
                     (cliente.nome, cliente.telefone, cliente.email))
      conn.commit()

      return True
    
    finally:
      conn.close() 

  @staticmethod
  def insert_emprestimo(emprestimo: Emprestimo):
    try:

      conn = sql.connect('biblioteca.db')
      cursor = conn.cursor()

      cursor.execute('''INSERT INTO emprestimos 
                     (id_livro, id_cliente, data_emprestimo, data_devolucao) 
                     VALUES(?,?,?,?)''', 
                     (emprestimo.id_livro, emprestimo.id_cliente, emprestimo.data_emprestimo, emprestimo.data_devolucao))
      conn.commit()

      return True

    finally:
      conn.close() 

  @staticmethod
  def get_qtde_livro(id_livro: int):
    try:  
      conn = sql.connect('biblioteca.db')
      cursor = conn.cursor()
      query = cursor.execute('''SELECT quantidade 
                                  FROM livros 
                                  WHERE id = ?  ''', (id_livro, )).fetchone()

      return query[0]
    
    finally:
      conn.close()  

  @staticmethod
  def update_qtde_livro(id_livro: int, quantidade):
    try:
      conn = sql.connect('biblioteca.db')
      cursor = conn.cursor()

      cursor.execute('''UPDATE livros 
                              SET quantidade = ?
                              WHERE id = ?  ''', (quantidade, id_livro))
      conn.commit()

      return True

    finally:
      conn.close()

  @staticmethod
  def search_livro_disponivel(id):
    try:
      conn = sql.connect('biblioteca.db')
      cursor = conn.cursor()

      query = cursor.execute('''SELECT quantidade 
                                FROM livros 
                                WHERE id = ?  ''', (id, )).fetchone()

      if query:
        return True if query[0] > 0 else False
      
      return False

    finally:
      conn.close()    

  @staticmethod
  def devolver_emprestimo(id_emprestimo: int):
    try:
      conn = sql.connect('biblioteca.db')
      cursor = conn.cursor()

      cursor.execute('''UPDATE emprestimos 
                              SET status = ?
                              WHERE id = ?  ''', ("devolvido", id_emprestimo))
      conn.commit()

      return True

    finally:
      conn.close()

  @staticmethod
  def search_livro_by_model(livro: Livro):
    try:
      conn = sql.connect('biblioteca.db')
      cursor = conn.cursor()

      query = cursor.execute('''SELECT id 
                        FROM livros
                        WHERE titulo = ? and autor = ? and descricao = ?''', (livro.titulo, livro.autor, livro.descricao)).fetchone()
      
      return query[0] if query else None
    
    finally:
      conn.close()

  @staticmethod
  def search_cliente_by_model(cliente: Cliente):
    try:
      conn = sql.connect('biblioteca.db')
      cursor = conn.cursor()

      query = cursor.execute('''SELECT id 
                        FROM clientes
                        WHERE nome = ? and telefone = ? and email = ?''', (cliente.nome, cliente.telefone, cliente.email)).fetchone()
      
      return query[0] if query else None
    
    finally:
      conn.close() 

    #=================================================
  @staticmethod  
  def search_livro_by_id(id: int):
    try:
      conn = sql.connect('biblioteca.db')
      cursor = conn.cursor()

      query = cursor.execute('''SELECT id 
                        FROM livros
                        WHERE id = ? ''', (id, )).fetchone()
      
      return True if query else False
    
    finally:
      conn.close()

  @staticmethod
  def search_cliente_by_id(id: int):
    try:
      conn = sql.connect('biblioteca.db')
      cursor = conn.cursor()

      query = cursor.execute('''SELECT id 
                        FROM clientes
                        WHERE id = ?''', (id, )).fetchone()
      
      return True if query else False
    
    finally:
      conn.close() 

  @staticmethod
  def search_emprestimo_by_id(id: int):
    try:
      conn = sql.connect('biblioteca.db')
      cursor = conn.cursor()

      query = cursor.execute('''SELECT id 
                        FROM emprestimos
                        WHERE id = ?''', (id, )).fetchone()
      
      return True if query else False
    
    finally:
      conn.close()     


  @staticmethod
  def search_livro_by_emprestimo(id_emprestimo: int):
    try:
      conn = sql.connect('biblioteca.db')
      cursor = conn.cursor()

      query = cursor.execute('''SELECT id_livro 
                        FROM emprestimos
                        WHERE id = ?''', (id_emprestimo, )).fetchone()
      
      return query[0]
    
    finally:
      conn.close()  