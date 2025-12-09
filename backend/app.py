import os
from flask import Flask, jsonify
from flask_cors import CORS
from config import config
from models import db

def create_app(config_name='default'):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    
    # Initialize Extensions
    db.init_app(app)
    CORS(app) # Enable CORS for frontend

    # Setup Flask-Security
    from flask_security import Security, SQLAlchemyUserDatastore, hash_password
    from models import User, Role
    user_datastore = SQLAlchemyUserDatastore(db, User, Role)
    security = Security(app, user_datastore)

    # Create Database Tables (for dev/testing)
    with app.app_context():
        db.create_all()
        
        # Create a test user if not exists
        if not user_datastore.find_user(email="test@example.com"):
            user_datastore.create_user(email="test@example.com", password=hash_password("password"), full_name="Test User")
            db.session.commit()

    @app.route('/')
    def index():
        return jsonify({"message": "Welcome to SkillBridge API"})

    @app.route('/api/health')
    def health_check():
        return jsonify({"status": "healthy"})

    return app

if __name__ == '__main__':
    app = create_app(os.getenv('FLASK_CONFIG') or 'default')
    app.run(port=5000)
