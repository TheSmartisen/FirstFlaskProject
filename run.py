import os
from app import create_app
# test
app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
