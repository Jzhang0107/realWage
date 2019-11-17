from flask import Flask
from flask_bootstrap import Bootstrap
from config import Config

app = Flask(__name__, static_folder='C://Users/a7089/Desktop/Programming/BostonHacks/realWage/frontend/templates/css', template_folder='C://Users/a7089/Desktop/Programming/BostonHacks/realWage/frontend/templates')
app.config.from_object(Config)
Bootstrap(app)

from app import routes