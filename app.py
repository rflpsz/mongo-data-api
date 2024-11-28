import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from flask import Flask, request
from flasgger import Swagger
from flask_cors import CORS
from api import (
    aggregate_bp,
    delete_many_bp,
    delete_one_bp,
    find_bp,
    find_one_bp,
    insert_many_bp,
    insert_one_bp,
    update_many_bp,
    update_one_bp,
)
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Set up CORS
CORS(app)

# Registering blueprints
app.register_blueprint(insert_one_bp, url_prefix="/api")
app.register_blueprint(insert_many_bp, url_prefix="/api")
app.register_blueprint(find_one_bp, url_prefix="/api")
app.register_blueprint(find_bp, url_prefix="/api")
app.register_blueprint(update_one_bp, url_prefix="/api")
app.register_blueprint(update_many_bp, url_prefix="/api")
app.register_blueprint(delete_one_bp, url_prefix="/api")
app.register_blueprint(delete_many_bp, url_prefix="/api")
app.register_blueprint(aggregate_bp, url_prefix="/api")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=False, host="0.0.0.0", port=port)
