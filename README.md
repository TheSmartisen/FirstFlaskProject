# Gestion d'utilisateurs - Web Application

Cette application web permet de gérer des utilisateurs avec des fonctionnalités de création d'utilisateur et de liste des utilisateurs. L'application est construite avec Flask et SQLite, et inclut des API pour gérer les utilisateurs via des requêtes GET et POST.

## Fonctionnalités

- Ajouter un utilisateur avec les informations suivantes : email, prénom, nom de famille et mot de passe.
- Afficher la liste des utilisateurs dans une interface utilisateur.
- Hachage des mots de passe avant de les stocker.
- Connexion utilisateur avec session pour protéger les pages `/add-user` et `/users`.

## Prérequis

Assurez-vous d'avoir Python installé sur votre machine ainsi que `pip` pour installer les dépendances.

## Installation

1. Clonez ce dépôt ou téléchargez les fichiers.
2. Installez les dépendances requises en exécutant la commande suivante :

    ```bash
    pip install -r requirements.txt
    ```

## Configuration

Les informations de configuration sont définies dans le fichier `config.py`.

## Utilisation

1. Pour lancer l'application, exécutez le fichier `run.py` :

    ```bash
    python run.py
    ```

2. Une fois l'application lancée, vous pouvez accéder aux pages suivantes :

    - `/add-user` : Page pour ajouter un utilisateur via un formulaire.
    - `/users` : Page pour afficher la liste des utilisateurs.
    - `/login` : Page pour la connexion (protection des routes).
      - Pour tester toutes les pages :
        - **login** : patochehem@gmail.com
        - **mot de passe** : 1234  (Oui je sais c'est pas sécu mais **TOUTES** les données sont fictives)

## API

L'application expose deux routes API :

- `POST /api/users` : Ajouter un nouvel utilisateur.
    - Body de la requête : `{ "username": "email", "first_name": "prénom", "last_name": "nom", "password": "mot de passe" }`
    
- `GET /api/users` : Récupérer la liste des utilisateurs au format JSON.

## Base de données

- L'application utilise SQLite pour stocker les utilisateurs dans une base de données locale `app.db`.
- Le fichier `db.py` gère les opérations sur la base de données.

## Fichiers Inclus

- `requirements.txt` : Liste des dépendances à installer pour l'application.
- `add_user.html` : Page pour ajouter un utilisateur avec un formulaire.
- `users.html` : Page pour afficher la liste des utilisateurs.
- `routes.py` : Gère les routes de l'application.
- `db.py` : Gère les opérations de base de données.
- `run.py` : Fichier pour démarrer le serveur Flask.

## Technologies Utilisées

- Flask (Python)
- SQLite
- HTML, CSS (Bootstrap)
- JavaScript (Fetch API)


