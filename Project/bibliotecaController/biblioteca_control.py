from models.models import Livro, Emprestimo, Cliente 
from daos.dao import BibliotecaDao

#teste de esteira
# Aqui vai ficar toda a regra de negócio
class Biblioteca:
  def __init__(self):
    pass

  @staticmethod
  def cadastrar_livro( livro: Livro):
    try:
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
  def cadastrar_cliente(cliente: Cliente):
    try:

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
  def atualizar_quantidade(id_livro: int, quantidade: int):
    try:
      BibliotecaDao.update_qtde_livro(id_livro, quantidade)
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
    try:
        lista_livros = BibliotecaDao.list_all_livros()
        livros = [{"id":livro[0],
                   "titulo": livro[1],
                   "autor": livro[2], 
                   "descricao": livro[3],
                   "quantidade": livro[4]
                   } for livro in lista_livros]
        
        response = {
            "status_code": 200,
            "message": "Consulta realizada com sucesso.",
            "livros": livros
        }
        return response
    except Exception as e:
        response = {
            "status_code": 500,
            "message": f"Erro ao consultar livros: {e}"
        }
        return response

  @staticmethod
  def mostrar_clientes():
    try:
        lista_clientes = BibliotecaDao.list_all_clientes()
        clientes = [{"id":cliente[0],
                   "nome": cliente[1],
                   "telefone": cliente[2], "email": cliente[3]} for cliente in lista_clientes]
      
        response = {
            "status_code": 200,
            "message": "Consulta realizada com sucesso.",
            "clientes": clientes
        }
        return response
    except Exception as e:
        response = {
            "status_code": 500,
            "message": f"Erro ao consultar clientes: {e}"
        }
        return response  
    
  @staticmethod
  def mostrar_emprestimos():
    try:
        lista_emprestimos = BibliotecaDao.list_all_emprestimos()
        clientes = [{"id":emprestimo[0],
                   "id_livro": emprestimo[1],
                   "id_cliente": emprestimo[2], 
                   "data_emprestimo": emprestimo[3], 
                   "data_devolucao": emprestimo[4], 
                   "status": emprestimo[5]} for emprestimo in lista_emprestimos]
      
        response = {
            "status_code": 200,
            "message": "Consulta realizada com sucesso.",
            "clientes": clientes
        }
        return response
    except Exception as e:
        response = {
            "status_code": 500,
            "message": f"Erro ao consultar clientes: {e}"
        }
        return response
      
  @staticmethod
  def validar_livro_disponivel(id_livro):
    return BibliotecaDao.search_livro_disponivel(id_livro)
  
  @staticmethod
  def validar_emprestimo(id_emprestimo):
    return BibliotecaDao.search_emprestimo_by_id(id_emprestimo)
    
  @staticmethod  
  def validar_cliente_cadastrado(id_cliente):
    return BibliotecaDao.search_cliente_by_id(id_cliente)
  
  def adicionar_emprestimo(self, emprestimo: Emprestimo):
    try:
      
      valid_livro = self.validar_livro_disponivel(emprestimo.id_livro)
      valid_cliente = self.validar_cliente_cadastrado(emprestimo.id_cliente)

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

      BibliotecaDao.insert_emprestimo(emprestimo)
      quantidade_atual = BibliotecaDao.get_qtde_livro(emprestimo.id_livro)
      quantidade_nova = quantidade_atual - 1 if quantidade_atual > 0 else 0
      BibliotecaDao.update_qtde_livro(emprestimo.id_livro, quantidade_nova)

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

  def devolver_livro(self, id_emprestimo):
    try:
      valid = self.validar_emprestimo(id_emprestimo)

      if not valid:
        response = {
                "status_code": 404,
                "message": "Emprestimo não encontrado."
            }
        return response
      
      BibliotecaDao.devolver_emprestimo(id_emprestimo)
      id_livro = BibliotecaDao.search_livro_by_emprestimo(id_emprestimo)
      quantidade_atual = BibliotecaDao.get_qtde_livro(id_livro)
      quantidade_nova = quantidade_atual + 1
      BibliotecaDao.update_qtde_livro(id_livro, quantidade_nova)

      response = {
                "status_code": 200, 
                "message": "Livro devolvido com sucesso!"
              }
      return response

    except Exception as e:
      response = {
                  "status_code": 500, 
                  "message": f"Erro ao realizar emprestimo do livro {e}"
                }
      return response


    




    