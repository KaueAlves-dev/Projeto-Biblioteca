from Project.Models.models import Livro, Emprestimo, Cliente 
from Project.Daos.dao import Dao


# Aqui vai ficar toda a regra de negócio
class Biblioteca:
  def __init__(self):
    pass


  def cadastrar_livro(self, titulo, autor, descricao, quantidade):
    livro = Livro(None, titulo, autor, descricao, quantidade)
    Dao.insert_livro(livro)