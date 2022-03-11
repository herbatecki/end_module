# blog/__init__.py

from flask import Flask    #1
from config import Config
from flask_sqlalchemy import SQLAlchemy # trzeba wyjść ze środowiska wirtualnego, żeby poprawnie zainstalować paczki zawarte w requirements.txt 
from flask_migrate import Migrate

app = Flask(__name__)       # 2
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app,db)

from blog import routes, models      # 3