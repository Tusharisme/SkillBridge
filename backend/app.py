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

    # Create Database Tables (for dev/testing)
    with app.app_context():
        db.create_all()

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
