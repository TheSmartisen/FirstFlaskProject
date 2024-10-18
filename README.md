
# Application Web de Gestion des Utilisateurs

Il s'agit d'une application web simple permettant de gérer des utilisateurs via une API. L'application prend en charge l'ajout d'utilisateurs, l'affichage d'une liste d'utilisateurs et utilise une base de données SQLite pour le stockage.

## Prérequis

Avant de commencer, assurez-vous d'avoir les éléments suivants installés :

- Python 3.x
- Flask
- SQLite

## Installation

1. Clonez le dépôt ou téléchargez les fichiers du projet.

2. Installez les paquets Python requis en exécutant la commande suivante :

   ```bash
   pip install -r requirements.txt
   ```

   Les paquets requis sont listés dans le fichier `requirements.txt` :
   
   ```txt
   click==8.0.1
   Flask==2.0.1
   Flask-Session==0.3.2
   itsdangerous==2.0.1
   Jinja2==3.0.1
   MarkupSafe==2.0.1
   Werkzeug==2.0.1
   ```

3. Configurez la base de données SQLite en exécutant le script SQL `schema.sql` pour initialiser le schéma de la base de données. Vous pouvez le faire en exécutant la commande suivante :

   ```bash
   sqlite3 database.db < schema.sql
   ```

   Cela créera les tables nécessaires dans le fichier `database.db`.

## Exécution de l'Application

1. Pour démarrer l'application Flask, exécutez le fichier `run.py` :

   ```bash
   python run.py
   ```

   L'application sera accessible à l'adresse `http://127.0.0.1:5000`.

## Structure du Projet

- `run.py`: Point d'entrée principal de l'application qui démarre le serveur Flask.
- `config.py`: Contient les paramètres de configuration pour l'application Flask, y compris la gestion des sessions.
- `routes.py`: Définit les routes de l'API pour la gestion des utilisateurs.
- `db.py`: Gère les connexions et les requêtes à la base de données.
- `schema.sql`: Script SQL pour créer les tables nécessaires dans la base de données SQLite.
- `templates/`: Contient les modèles HTML pour les pages web.

## Points de terminaison de l'API

L'application fournit les points de terminaison API suivants :

### GET `/api/users`
Récupère la liste des utilisateurs au format JSON.

### POST `/api/users`
Ajoute un nouvel utilisateur à la base de données. Le corps de la requête doit contenir les champs suivants :

```json
{
    "username": "email@example.com",
    "first_name": "First",
    "last_name": "Last",
    "password": "password"
}
```

## Pages HTML

### 1. Page d'ajout d'utilisateur (`add_user.html`)

- Accessible via `/add-user`.
- Cette page permet l'ajout de nouveaux utilisateurs via un formulaire.
- Lors de la soumission du formulaire, l'utilisateur est ajouté via l'API POST `/api/users`.
- [Voir le code source HTML](add_user.html).

### 2. Page de liste des utilisateurs (`users.html`)

- Accessible via `/users`.
- Affiche un tableau listant tous les utilisateurs de la base de données.
- Les données des utilisateurs sont récupérées via l'API GET `/api/users`.
- [Voir le code source HTML](users.html).

## Comment ça fonctionne

1. **Ajout d'un utilisateur** :  
   La page `add_user.html` contient un formulaire permettant d'ajouter de nouveaux utilisateurs. Lorsque le formulaire est soumis, les données sont envoyées au point de terminaison `/api/users` via une requête POST, et l'utilisateur est ajouté à la base de données.

2. **Affichage des utilisateurs** :  
   La page `users.html` récupère la liste des utilisateurs en utilisant le point de terminaison `/api/users` (GET) et affiche les résultats dans un tableau.

## Licence

Ce projet est open-source et disponible sous la licence [MIT License](LICENSE).
