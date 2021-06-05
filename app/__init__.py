from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options

bootstrap = Bootstrap()

def create_app(config_name):

  app = Flask(__name__)

  #Create the app configuration
  app.config.from_object(config_options[config_name])

  #INitializing flask extensions
  bootstrap.init_app(app)

  #Rejistering the blueprint
  from .main import main as main_blueprint
  app.register_blueprint(main_blueprint)

  #Setting config
  
