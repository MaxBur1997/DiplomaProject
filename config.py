import os

class Config:
    """Базовая конфигурация приложения."""
    SECRET_KEY = os.environ.get('SECRET_KEY', 'your_secret_key')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///app.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
