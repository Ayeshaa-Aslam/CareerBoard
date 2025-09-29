# backend/db.py
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def init_db(app):    
    from config import Config
    app.config.from_object(Config)
    db.init_app(app)

    with app.app_context():
        db.create_all()
