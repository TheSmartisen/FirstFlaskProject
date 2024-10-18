import os
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash
from app import create_app
from app.db import get_db

app = create_app()


def hash_existing_passwords():
    db = get_db()

    # Récupérer tous les utilisateurs de la base de données
    users = db.execute('SELECT id, password FROM users').fetchall()

    for user in users:
        user_id = user['id']
        password = user['password']

        # Supposons que les mots de passe non hachés sont en clair (par exemple, moins de 60 caractères)
        if len(password) < 60:  # Vérifie si le mot de passe est probablement en clair
            hashed_password = generate_password_hash(password)

            # Mettre à jour la base de données avec le mot de passe haché
            db.execute('UPDATE users SET password = ? WHERE id = ?', (hashed_password, user_id))
            db.commit()

            print(f"Mot de passe pour l'utilisateur avec l'ID {user_id} haché avec succès.")
        else:
            print(f"Le mot de passe pour l'utilisateur avec l'ID {user_id} est déjà haché.")


if __name__ == '__main__':
    # S'assurer que la base de données est initialisée
    with app.app_context():
        hash_existing_passwords()
