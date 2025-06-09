from dataclasses import dataclass
import sqlite3 as sql
from Project.Models.models import Livro, Cliente, Emprestimo

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

  
  def update_qtde_livro(self, id, operacao):
    try:
      conn = sql.connect('biblioteca.db')
      cursor = conn.cursor()

      new_quantidade = self.get_new_qtde_livro(id, operacao)

      cursor.execute('''UPDATE livros 
                              SET quantidade = ?
                              WHERE id = ?  ''', (new_quantidade, id))
      conn.commit()

      return True

    finally:
      conn.close()

  @staticmethod
  def get_new_qtde_livro(id, operacao):
    try:
      conn = sql.connect('biblioteca.db')
      cursor = conn.cursor()

      query = cursor.execute('''SELECT quantidade 
                                FROM livros 
                                WHERE id = ?  ''', (id, )).fetchone()

      quantidade_atual = query[0]

      if operacao == 'mais':
          return quantidade_atual + 1
      elif operacao == 'menos':
          return quantidade_atual - 1 if quantidade_atual > 0 else 0
      else:
          return None  # Operação inválida

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
  def update_status_emprestimo(id, new_status):
    try:
      conn = sql.connect('biblioteca.db')
      cursor = conn.cursor()

      cursor.execute('''UPDATE emprestimos 
                              SET status = ?
                              WHERE id = ?  ''', (new_status, id))
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

