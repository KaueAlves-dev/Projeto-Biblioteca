from dataclasses import dataclass
from typing import Optional
from datetime import date

@dataclass
class Livro:
  id: Optional[int]
  titulo: str
  autor:str
  descricao: str
  quantidade: int

@dataclass
class Cliente:
  id: Optional[int]
  nome: str
  telefone: str
  email: str

@dataclass
class Emprestimo:
  id: Optional[int]
  id_livro: int
  id_cliente: int
  data_emprestimo: date
  data_devolucao: date
  status: str = "ativo"

