from flask import Flask
from config import Config

app = Flask(__name__, template_folder='C://Users/a7089/Desktop/Programming/BostonHacks/realWage/frontend/templates')
app.config.from_object(Config)

from app import routes