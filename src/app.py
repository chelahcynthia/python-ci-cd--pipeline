import os, time
from datetime import datetime
from typing import Dict, Any, List

from flask import Flask, jsonify, request
from werkzeug.exceptions import HTTPException

from src.models import User
from src.utils import validate_email

def create_app() -> Flask:
    app = Flask(__name__)

    app.config['ENV'] = os.getenv('FLASK_ENV', 'development')
    app.config['DEBUG'] = app.config['ENV'] == 'development'
    app.config['START_TIME'] = time.time()

    register_routes(app)
    register_error_handlers(app)

    return app
