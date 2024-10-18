import os
from app import create_app
from app.db import init_db_command

app = create_app()

if __name__ == '__main__':
    if not os.path.exists('instance/app.db'):
        init_db_command()  # Initialiser la base de données si elle n'existe pas
    app.run(debug=True)
