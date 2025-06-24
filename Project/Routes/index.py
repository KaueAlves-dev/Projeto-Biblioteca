from flask import Blueprint, request, jsonify, Response
import json
from Dtos.dto import ClienteDTO, LivroDTO, EmprestimoDTO
from BibliotecaControl.biblioteca_control import Biblioteca

bluep = Blueprint('bluep', __name__)

# Rotas para Cadastros
@bluep.route('/cadastrar-cliente', methods = ['POST'])
def cadastrar_cliente():
  print('Iniciando cadastro de cliente')
  payload = request.json
  cliente = ClienteDTO.from_dict(payload)
  response = Biblioteca.cadastrar_cliente(cliente)
  print('cliente cadastrado com sucesso')
  return Response(json.dumps(response), mimetype='application/json')

@bluep.route('/cadastrar-livro', methods = ['POST'])
def cadastrar_livro():
  print('Iniciando cadastro de livro')
  payload = request.json
  livro = LivroDTO.from_dict(payload)
  response = Biblioteca.cadastrar_livro(livro)
  print('livro cadastrado com sucesso')
  return Response(json.dumps(response), mimetype='application/json')

# Cadastrar emprestimo
@bluep.route('/cadastrar-emprestimo', methods = ['POST'])
def cadastrar_emprestimo():
  print('Iniciando cadastro de emprestimo')
  payload = request.json
  emprestimo = EmprestimoDTO.from_dict(payload)
  biblioteca = Biblioteca()
  response = biblioteca.adicionar_emprestimo(emprestimo)
  print('emprestimo cadastrado com sucesso')
  return Response(json.dumps(response), mimetype='application/json')

# Rotas para listagens
@bluep.route('/listar-clientes', methods = ['GET'])
def listar_clientes():
  print('Iniciando listagem de clientes')
  response = Biblioteca.mostrar_clientes()
  return Response(json.dumps(response), mimetype='application/json')

@bluep.route('/listar-livros', methods = ['GET'])
def listar_livros():
  print('Iniciando listagem de livros')
  response = Biblioteca.mostrar_livros()
  return Response(json.dumps(response), mimetype='application/json')
  

# Listar emprestimo  
@bluep.route('/listar-emprestimos', methods = ['GET'])
def listar_emprestimos():
  print('Iniciando listagem de emprestimos')
  response = Biblioteca.mostrar_emprestimos()
  return Response(json.dumps(response), mimetype='application/json')

# Atualizar quantidade de livros
@bluep.route('/atualizar-quantidade', methods = ['POST'])
def atualizar_quantidade():
  print('Atualizando quantidade de livro')
  payload = request.json
  response = Biblioteca.atualizar_quantidade(payload['id_livro'], payload['quantidade'])
  return Response(json.dumps(response), mimetype='application/json')

#Devolver livro
@bluep.route('/devolver-livro', methods = ['POST'])
def devolver_emprestimo():
  print('Iniciando devolução de livro')
  payload = request.json
  biblioteca = Biblioteca()
  response = biblioteca.devolver_livro(payload['id_emprestimo'])
  return Response(json.dumps(response), mimetype='application/json')
