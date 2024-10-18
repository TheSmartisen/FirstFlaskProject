from flask import request, jsonify, render_template
from .db import get_db

def init_routes(app):
    # Route pour afficher le formulaire d'ajout d'utilisateur
    @app.route('/add-user', methods=['GET'])
    def add_user_form():
        return render_template('add_user.html')

    # Route pour afficher la liste des utilisateurs dans une page HTML
    @app.route('/')
    def home():
        return render_template('users.html')

    # Route GET pour récupérer les utilisateurs
    @app.route('/api/users', methods=['GET'])
    def get_users():
        db = get_db()
        users = db.execute('SELECT * FROM users').fetchall()
        return jsonify([dict(user) for user in users])

    # Route POST pour ajouter un utilisateur
    @app.route('/api/users', methods=['POST'])
    def add_user():
        data = request.json
        username = data['username']
        first_name = data['first_name']
        last_name = data['last_name']
        password = data['password']
        db = get_db()
        db.execute('INSERT INTO users (username, first_name, last_name, password) VALUES (?, ?, ?, ?)', (username, first_name, last_name, password))
        db.commit()
        return jsonify({'message': 'Utilisateur ajouté avec succès'}), 201
