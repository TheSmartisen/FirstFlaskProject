import sqlite3
from flask import current_app, g
from werkzeug.security import generate_password_hash

# Connexion à la base de données
def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row
    return g.db

# Fermer la connexion à la base de données
def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()
