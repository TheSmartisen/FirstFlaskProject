import os

class Config:
    SECRET_KEY = 'dev_key'
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    DATABASE = os.path.join(BASE_DIR, 'instance', 'app.db')
