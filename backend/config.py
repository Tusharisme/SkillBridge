import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard-to-guess-string'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///skillbridge.db'
    
    # Flask-Security Config
    SECURITY_PASSWORD_SALT = os.environ.get('SECURITY_PASSWORD_SALT') or 'super-secret-salt'
    SECURITY_REGISTERABLE = True
    SECURITY_SEND_REGISTER_EMAIL = False # For dev
    SECURITY_TOKEN_AUTHENTICATION_HEADER = 'Authentication-Token'
    WTF_CSRF_ENABLED = False # Disable CSRF for API (use tokens)


class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False
    # SQLALCHEMY_DATABASE_URI will be pulled from env in prod

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
