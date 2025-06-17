from dataclasses import dataclass
from datetime import datetime, timedelta

@dataclass
class LivroDTO:
  titulo: str
  autor:str
  descricao: str
  quantidade: int

  @classmethod
  def from_dict(cls, payload: dict):
    return cls(
              titulo = payload['titulo'],
              autor = payload['autor'],
              descricao = payload['descricao'],
              quantidade = payload['quantidade']
              )
  

@dataclass
class ClienteDTO:
  nome: str
  telefone: str
  email: str

  @classmethod
  def from_dict(cls, payload: dict):
    return cls(
              nome = payload['nome'],
              telefone = payload['telefone'],
              email = payload['email'],
              )

@dataclass
class EmprestimoDTO:
  id_livro: int
  id_cliente: int
  data_emprestimo: str
  data_devolucao: str
  status: str = "ativo"

  @classmethod
  def from_dict(cls, payload: dict):
    return cls(
              id_livro = payload['id_livro'],
              id_cliente = payload['id_cliente'],
              data_emprestimo = datetime.now().strftime('%Y-%m-%d'),         # string: '2025-06-09'
              data_devolucao = (datetime.now() + timedelta(days=30)).strftime('%Y-%m-%d'),  # string: '2025-07-09',
              status = payload.get('status', 'ativo')
    )
  
 