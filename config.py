import os

SECRET_KEY = 'qgdostark'

# Configurações para acesso ao bd
MYSQL_HOST = "192.168.0.101"
MYSQL_USER = "stark"
MYSQL_PASSWORD = "pass"
MYSQL_DB = "jogoteca"
MYSQL_PORT =  3306

UPLOAD_PATH = os.path.dirname(os.path.abspath(__file__)) \
              + '/uploads'# Pegando nome do arquivo e caminho absoluto
