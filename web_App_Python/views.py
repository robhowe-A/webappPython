"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from web_App_Python import app




@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    """
    Guessing what customer's logic is doing
    import requests
    api_url = "https://norwayeast.api.cognitive.microsoft.com/history/generate"
    //api_url = "https://norwayeast.api.cognitive.microsoft.com/history/delete"
    response = requests.get(api_url)
    response.json()
    {'userId': 1, 'id': 1, 'title': 'delectus aut autem', 'completed': False}
    
    source: https://realpython.com/api-integration-in-python/
    """
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    raise Exception("This is a test exception.")
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )
