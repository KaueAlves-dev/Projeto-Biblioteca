EVENT_SCHEMA_cadastrar_cliente = {
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "properties": {
    "nome": {
      "type": "string",
      "minLength": 1
    },
    "telefone": {
      "type": "string",
      "pattern": "^[0-9]{10,11}$"
    },
    "email": {
      "type": "string",
      "format": "email"
    }
  },
  "required": ["nome", "telefone", "email"],
  "additionalProperties": False
}


EVENT_SCHEMA_cadastrar_livro = {
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "properties": {
    "titulo": {
      "type": "string",
      "minLength": 1
    },
    "autor": {
      "type": "string",
      "minLength": 1
    },
    "descricao": {
      "type": "string",
      "minLength": 1
    },
    "quantidade": {
      "type": "integer",
      "minimum": 0
    }
  },
  "required": ["titulo", "autor", "descricao", "quantidade"],
  "additionalProperties": False
}


EVENT_SCHEMA_cadastrar_emprestimo = {
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "properties": {
    "id_livro": {
      "type": "integer",
      "minimum": 1
    },
    "id_cliente": {
      "type": "integer",
      "minimum": 1
    }
  },
  "required": ["id_livro", "id_cliente"],
  "additionalProperties": False
}


EVENT_SCHEMA_atualizar_quantidade = {
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "properties": {
    "id_livro": {
      "type": "integer",
      "minimum": 1
    },
    "quantidade": {
      "type": "integer",
      "minimum": 0
    }
  },
  "required": ["id_livro", "quantidade"],
  "additionalProperties": False
}


EVENT_SCHEMA_devolver_livro = {
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "properties": {
    "id_emprestimo": {
      "type": "integer",
      "minimum": 1
    }
  },
  "required": ["id_emprestimo"],
  "additionalProperties": False
}

