import sqlite3 as sql

def create_database():
  try:
    conn = sql.connect('biblioteca.db')
    cursor = conn.cursor()

    cursor.execute(''' CREATE TABLE IF NOT EXISTS livros(
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        titulo TEXT NOT NULL,
                        autor TEXT NOT NULL,
                        descricao TEXT NOT NULL,
                        quantidade INTEGER NOT NULL
                    )
                    ''')


    cursor.execute(''' CREATE TABLE IF NOT EXISTS clientes(
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nome TEXT NOT NULL,
                        telefone TEXT NOT NULL,
                        email TEXT NOT NULL
                        
                    )
                    ''')

    cursor.execute(''' CREATE TABLE IF NOT EXISTS emprestimos(
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        id_livro INTEGER NOT NULL,
                        id_cliente INTEGER NOT NULL,
                        data_emprestimo DATE NOT NULL,
                        data_devolucao DATE NOT NULL,
                        status TEXT DEFAULT 'ativo',
                        FOREIGN KEY (id_livro) REFERENCES livros(id),
                        FOREIGN KEY (id_cliente) REFERENCES clientes(id)

                        
                    )
                    ''')


    conn.commit()
    
  finally:  
    conn.close()


