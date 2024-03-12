"""
The flask application package. First deploy to azure
"""

from flask import Flask
app = Flask(__name__)

import FlaskWebProject1.views
