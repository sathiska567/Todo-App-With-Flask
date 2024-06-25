from app import app
from db import db

if __name__ == '__main__':
    app.run(port=8080,debug=True)
