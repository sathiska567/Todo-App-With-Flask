from flask import Flask

app = Flask(__name__)

# Import and register the routes
from app import routes
