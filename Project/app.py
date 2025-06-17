from flask import Flask
from Routes.index import bluep  # importa o blueprint
from DataBase.database import create_database

app = Flask(__name__)
app.register_blueprint(bluep, url_prefix='/livros')  # registra as rotas

if __name__ == '__main__':
    create_database()
    app.run(debug=True)