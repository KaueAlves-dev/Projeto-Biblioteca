from Project.Models.models import Livro, Emprestimo, Cliente 
from Project.Daos.dao import BibliotecaDao

#teste de esteira
# Aqui vai ficar toda a regra de negócio
class Biblioteca:
  def __init__(self):
    pass

  @staticmethod
  def cadastrar_livro( titulo, autor, descricao, quantidade):
    try:
      
      livro = Livro(id = None, titulo = titulo, autor = autor, descricao = descricao, quantidade = quantidade)
      validacao = BibliotecaDao.search_livro_by_model(livro)
      if validacao:
        response = {
                  "status_code": 200, 
                  "message": "Livro já cadastrado anteriormente"
                }
        return response
        
      BibliotecaDao.insert_livro(livro)
      response = {
                  "status_code": 200, 
                  "message": "Livro cadastrado com sucesso!"
                }
      return response
    
    except Exception as e:
      response = {
                  "status_code": 500, 
                  "message": f"Erro ao cadastrar livro {e}"
                }
      return response
    
  @staticmethod
  def cadastrar_cliente( nome, telefone, email):
    try:
      cliente = Cliente(id = None, nome = nome, telefone = telefone, email = email)

      validacao = BibliotecaDao.search_cliente_by_model(cliente)
      if validacao:
        response = {
                  "status_code": 200, 
                  "message": "Cliente já cadastrado anteriormente"
                }
        return response
      
      BibliotecaDao.insert_cliente(cliente)
      response = {
                  "status_code": 200, 
                  "message": "Cliente cadastrado com sucesso!"
                }
      return response
    
    except Exception as e:
      response = {
                  "status_code": 500, 
                  "message": f"Erro ao cadastrar cliente {e}"
                }
      return response
    
  @staticmethod
  def atualizar_quantidade(id_livro: int, operacao: str):
    try:
      BibliotecaDao.update_qtde_livro(id_livro, operacao)
      response = {
                    "status_code": 200, 
                    "message": "Quantidade do livro atualizada com sucesso"
                  }
      return response
    
    except Exception as e:
      response = {
                  "status_code": 500, 
                  "message": f"Atualizar quantidade do livro {e}"
                }
      return response

  @staticmethod
  def mostrar_livros():
    lista_livros = BibliotecaDao.list_all_livros()
    response = {
                  "status_code": 500, 
                  "message": f"Atualizar quantidade do livro",
                  "livros": lista_livros
                }
    return response
    
  @staticmethod
  def validar_livro_disponivel(id_livro):
    return BibliotecaDao.search_livro_disponivel(id_livro)
    
  @staticmethod  
  def validar_cliente_cadastrado(id_cliente):
    return BibliotecaDao.search_cliente_by_id(id_cliente)
  
  def adicionar_emprestimo(self, id_livro, id_cliente, data_empr, data_dev):
    try:
      valid_livro = self.validar_livro_disponivel(id_livro)
      valid_cliente = self.validar_cliente_cadastrado(id_cliente)

      if not valid_livro:
        return {
            "status_code": 404,
            "message": "Livro não disponível para empréstimo."
        }

      if not valid_cliente:
          return {
              "status_code": 404,
              "message": "Cliente não cadastrado."
          }

      emprestimo = Emprestimo(id= None, id_livro = id_livro, id_cliente= id_cliente, data_emprestimo = data_empr,
    data_devolucao= data_dev)
      BibliotecaDao.insert_emprestimo(emprestimo)
      self.atualizar_quantidade(id_livro, 'menos')
      response = {
                "status_code": 200, 
                "message": "Emprestimo realizado com sucesso!"
              }
      return response
      
      

    except Exception as e:
      response = {
                  "status_code": 500, 
                  "message": f"Erro ao realizar emprestimo do livro {e}"
                }
      return response

  def devolver_livro(id_emprestimo):
    pass


    