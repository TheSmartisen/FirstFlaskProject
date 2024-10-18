import sqlite3
from flask import current_app, g

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

# Initialiser la base de données
def init_db():
    db = get_db()
    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read())

# Commande pour initier la base de données
def init_db_command():
    init_db()
    print('Base de données initialisée.')
