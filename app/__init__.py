from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    
    # Set up database URI
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Optional, just to remove a warning

    # Attach db to app
    db.init_app(app)
    
    from .models import CaseInfo
    from .routes import main
    app.register_blueprint(main)
    
    
    return app




