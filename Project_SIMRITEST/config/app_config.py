# Flask secret key
import secrets

SECRET_KEY = secrets.token_hex(16)

# Database URI
DATABASE = 'mysql+pymysql'
USERNAME = 'root'
PASSWORD = '123123'
ADDRESS = '127.0.0.1'
PORT = 3306
DATABASE_NAME = 'simritest'
