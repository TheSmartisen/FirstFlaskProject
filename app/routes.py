from click import password_option
from flask import request, jsonify, render_template, session, redirect, flash, url_for
from .db import get_db
from werkzeug.security import generate_password_hash, check_password_hash

def init_routes(app):
    # Route pour afficher le formulaire de connexion
    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']

            db = get_db()
            user = db.execute('SELECT * FROM users WHERE username = ?', (username,)).fetchone()

            if user and check_password_hash(user['password'], password):
                session['user_id'] = user['id']  # Stocker l'ID de l'utilisateur dans la session
                flash('Connexion réussie', 'success')
                return redirect(url_for('home'))
            else:
                flash('Nom d\'utilisateur ou mot de passe incorrect', 'danger')

        return render_template('login.html')

    # Déconnexion
    @app.route('/logout')
    def logout():
        session.clear()  # Efface toutes les données de session
        flash('Déconnecté avec succès', 'success')
        return redirect(url_for('login'))

    # Route pour afficher le formulaire d'ajout d'utilisateur
    @app.route('/add-user', methods=['GET'])
    def add_user_form():
        if not session.get('user_id'):
            return redirect(url_for('login'))
        return render_template('add_user.html')

    # Route pour afficher la liste des utilisateurs dans une page HTML
    @app.route('/')
    def home():
        if not session.get('user_id'):
            return redirect(url_for('login'))
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
        password = generate_password_hash(data['password'])
        db = get_db()
        db.execute('INSERT INTO users (username, first_name, last_name, password) VALUES (?, ?, ?, ?)', (username, first_name, last_name, password))
        db.commit()
        return jsonify({'message': 'Utilisateur ajouté avec succès'}), 201
