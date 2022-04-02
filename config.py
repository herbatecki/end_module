# config.py
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))      #  1 # wielkimi literami zapis modułów

class Config:
    ADMIN_USERNAME = os.environ.get("ADMIN_USERNAME", "admin")
    ADMIN_PASSWORD = os.environ.get("ADMIN_PASSWORD", "change-me")
    SECRET_KEY = os.environ.get("SECRET_KEY") or "remember-to-add-secret-key"                       # 2
    SQLALCHEMY_DATABASE_URI = (                        # 3
        os.environ.get('DATABASE_URL') or
        'sqlite:///' + os.path.join(BASE_DIR, 'mikroblog.db')
    ) 
    # sqlite:///db.sqlite for a db in the same dir of .env file and
    # sqlite://../db.sqlite for relative one and
    # sqlite:////home/user/db.sqlite for absolute one.
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False             # 4 # flaga, która Wyłączy to funkcjonalność SQLAlchemy, polegającą na śledzeniu zmian w obiektach i emitowaniu sygnałów, gdy takie zmiany występują. To obciążające, więc powinno być wyłączane, jeśli nie jest potrzebne.