#!/usr/bin/python3
"""Task 2: Dynamic template with loops and conditions (Jinja + JSON)."""

import json
from flask import Flask, render_template

app = Flask(__name__)


def load_items():
    """Read items from items.json and return a list (or empty list on error)."""
    try:
        with open('items.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
        items = data.get('items', [])
        return items if isinstance(items, list) else []
    except (FileNotFoundError, json.JSONDecodeError):
        return []


@app.route('/', strict_slashes=False)
def home():
    return render_template('index.html')


@app.route('/about', strict_slashes=False)
def about():
    return render_template('about.html')


@app.route('/contact', strict_slashes=False)
def contact():
    return render_template('contact.html')


@app.route('/items', strict_slashes=False)
def items():
    return render_template('items.html', items=load_items())


if __name__ == '__main__':
    app.run(port=5000)
