"""WSGI entry for production (e.g. gunicorn on Railway)."""
from app import create_app

app = create_app()
