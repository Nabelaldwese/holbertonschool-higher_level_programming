#!/usr/bin/python3
"""Task 4: Extend products display to support JSON, CSV, and SQLite sources."""

import csv
import json
import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)


def read_products_json(filename='products.json'):
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


def read_products_sql(db_name='products.db'):
    """Read products from SQLite db and return list of dicts."""
    try:
        conn = sqlite3.connect(db_name)
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("SELECT id, name, category, price FROM Products ORDER BY id;")
        rows = cur.fetchall()
        conn.close()

        return [{
            "id": row["id"],
            "name": row["name"],
            "category": row["category"],
            "price": row["price"]
        } for row in rows]
    except sqlite3.Error:
        return None  # distinguish DB error from empty list


@app.route('/products', strict_slashes=False)
def products():
    """
    /products?source=json|csv|sql[&id=NUMBER]
    - Wrong source -> "Wrong source"
    - id not found -> "Product not found"
    - DB error -> "Database error"
    """
    source = request.args.get('source', type=str)
    pid = request.args.get('id', default=None, type=int)

    if source not in ('json', 'csv', 'sql'):
        return render_template('product_display.html', products=[], error="Wrong source")

    if source == 'json':
        data = read_products_json()
    elif source == 'csv':
        data = read_products_csv()
    else:
        data = read_products_sql()
        if data is None:
            return render_template('product_display.html', products=[], error="Database error")

    if pid is not None:
        filtered = [p for p in data if p.get("id") == pid]
        if len(filtered) == 0:
            return render_template('product_display.html', products=[], error="Product not found")
        data = filtered

    return render_template('product_display.html', products=data, error=None)


if __name__ == '__main__':
    app.run(port=5000)
