"""
This script runs the web_App_Python application using a development server.
"""

from os import environ
from web_App_Python import app

if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '7000'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT, debug=False)
