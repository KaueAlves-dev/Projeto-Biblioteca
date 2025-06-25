from flask import Flask, request
from routes.index import bluep  # importa o blueprint
from database.database import create_database

app = Flask(__name__)
app.register_blueprint(bluep, url_prefix='/livros')  # registra as rotas

if __name__ == '__main__':
    create_database()
    app.run(debug=True)
