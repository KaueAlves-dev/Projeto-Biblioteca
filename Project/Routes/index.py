from flask import Blueprint, request, Response
import json
from jsonschema import validate, ValidationError
from dtos.dto import ClienteDTO, LivroDTO, EmprestimoDTO
from bibliotecaController.biblioteca_control import Biblioteca
from json_schemas.event import EVENT_SCHEMA_cadastrar_emprestimo, EVENT_SCHEMA_atualizar_quantidade, EVENT_SCHEMA_cadastrar_cliente, EVENT_SCHEMA_cadastrar_livro, EVENT_SCHEMA_devolver_livro


bluep = Blueprint('bluep', __name__)

# Rotas para Cadastros
@bluep.route('/cadastrar-cliente', methods = ['POST'])
def cadastrar_cliente():
  try:
    print('Iniciando cadastro de cliente')
    payload = request.json
    validate(instance=payload, schema=EVENT_SCHEMA_cadastrar_cliente)
    cliente = ClienteDTO.from_dict(payload)
    response = Biblioteca.cadastrar_cliente(cliente)
    print('cliente cadastrado com sucesso')
    return Response(json.dumps(response), mimetype='application/json')

  except ValidationError as e:
    return build_schema_error(e)
  
@bluep.route('/cadastrar-livro', methods = ['POST'])
def cadastrar_livro():
  try:

    print('Iniciando cadastro de livro')
    payload = request.json
    validate(instance=payload, schema=EVENT_SCHEMA_cadastrar_livro)
    livro = LivroDTO.from_dict(payload)
    response = Biblioteca.cadastrar_livro(livro)
    print('livro cadastrado com sucesso')
    return Response(json.dumps(response), mimetype='application/json')
  
  except ValidationError as e:
    return build_schema_error(e)
# Cadastrar emprestimo
@bluep.route('/cadastrar-emprestimo', methods = ['POST'])
def cadastrar_emprestimo():
  try:
    print('Iniciando cadastro de emprestimo')
    payload = request.json
    validate(instance=payload, schema=EVENT_SCHEMA_cadastrar_emprestimo)
    emprestimo = EmprestimoDTO.from_dict(payload)
    biblioteca = Biblioteca()
    response = biblioteca.adicionar_emprestimo(emprestimo)
    print('emprestimo cadastrado com sucesso')
    return Response(json.dumps(response), mimetype='application/json')
  
  except ValidationError as e:
    return build_schema_error(e)
  
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
@bluep.route('/atualizar-quantidade', methods = ['PATCH'])
def atualizar_quantidade():
  try:  
    print('Atualizando quantidade de livro')
    payload = request.json
    validate(instance=payload, schema=EVENT_SCHEMA_atualizar_quantidade)
    response = Biblioteca.atualizar_quantidade(payload['id_livro'], payload['quantidade'])
    return Response(json.dumps(response), mimetype='application/json')

  except ValidationError as e:
    return build_schema_error(e)

#Devolver livro
@bluep.route('/devolver-livro', methods = ['POST'])
def devolver_emprestimo():
  try:
    print('Iniciando devolução de livro')
    payload = request.json
    validate(instance=payload, schema=EVENT_SCHEMA_devolver_livro)
    biblioteca = Biblioteca()
    response = biblioteca.devolver_livro(payload['id_emprestimo'])
    return Response(json.dumps(response), mimetype='application/json')
  
  except ValidationError as e:
    return build_schema_error(e)

def build_schema_error(error):
  return Response(
            json.dumps({"erro": f"Dados inválidos: {error.message}"}),
            status=400,
            mimetype='application/json'
        )