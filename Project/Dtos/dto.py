from dataclasses import dataclass
from datetime import date, datetime

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
  data_emprestimo: date
  data_devolucao: date
  status: str = "ativo"

  @classmethod
  def from_dict(cls, payload: dict):
    return cls(
              id_livro = payload['id_livro'],
              id_cliente = payload['id_cliente'],
              data_emprestimo = cls._parse_date(payload['data_emprestimo']),
              data_devolucao = cls._parse_date(payload['data_devolucao']),
              status = payload.get('status', 'ativo')
    )
  
  @staticmethod
  def _parse_date(date_str: str) -> date:
      """Converte string (YYYY-MM-DD) em date."""
      try:
          return datetime.strptime(date_str, "%Y-%m-%d").date()
      except ValueError:
          raise ValueError(f'Data inválida: {date_str}. Use o formato YYYY-MM-DD.')