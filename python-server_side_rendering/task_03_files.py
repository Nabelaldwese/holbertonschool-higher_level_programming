#!/usr/bin/python3
"""Task 3: Display data from JSON or CSV in Flask using query parameters."""

import csv
import json
from flask import Flask, render_template, request

app = Flask(__name__)


def read_products_json(filename='products.json'):
    """Read products from a JSON file and return a list of dicts."""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)

        if not isinstance(data, list):
            return []

        products = []
        for item in data:
            if isinstance(item, dict):
                products.append({
                    "id": int(item.get("id")) if item.get("id") is not None else None,
                    "name": item.get("name"),
                    "category": item.get("category"),
                    "price": float(item.get("price")) if item.get("price") is not None else None
                })
        return products
    except (FileNotFoundError, json.JSONDecodeError, ValueError, TypeError):
        return []


def read_products_csv(filename='products.csv'):
    """Read products from a CSV file and return a list of dicts."""
    try:
        products = []
        with open(filename, 'r', encoding='utf-8', newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                products.append({
                    "id": int(row.get("id")) if row.get("id") else None,
                    "name": row.get("name"),
                    "category": row.get("category"),
                    "price": float(row.get("price")) if row.get("price") else None
                })
        return products
    except (FileNotFoundError, ValueError, TypeError):
        return []


@app.route('/products', strict_slashes=False)
def products():
    """
    /products?source=json|csv[&id=NUMBER]
    - Wrong source -> show "Wrong source"
    - id not found -> show "Product not found"
    """
    source = request.args.get('source', type=str)
    pid = request.args.get('id', default=None, type=int)

    if source not in ('json', 'csv'):
        return render_template('product_display.html', products=[], error="Wrong source")

    if source == 'json':
        data = read_products_json()
    else:
        data = read_products_csv()

    # Filter by id if provided
    if pid is not None:
        filtered = [p for p in data if p.get("id") == pid]
        if len(filtered) == 0:
            return render_template('product_display.html', products=[], error="Product not found")
        data = filtered

    return render_template('product_display.html', products=data, error=None)


if __name__ == '__main__':
    app.run(port=5000)
