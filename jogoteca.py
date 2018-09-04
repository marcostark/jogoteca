from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config.from_pyfile('config.py')

db = MySQL(app)

from views import *

# Executar apenas quando for chamado
if __name__ == '__main__':
    # Definindo acesso externo e definido porta 8080
    # Debug=True, detecta as alterações automaticamente, para não precisar restartar a aplicação
    app.run(debug=True, host='0.0.0.0', port=8080)

