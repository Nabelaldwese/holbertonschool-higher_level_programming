#!/usr/bin/python3
"""Task 1: Creating a Basic HTML Template in Flask (Jinja includes)."""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def home():
    """Home page."""
    return render_template('index.html')


@app.route('/about', strict_slashes=False)
def about():
    """About page."""
    return render_template('about.html')


@app.route('/contact', strict_slashes=False)
def contact():
    """Contact page."""
    return render_template('contact.html')


if __name__ == '__main__':
    app.run(port=5000)
