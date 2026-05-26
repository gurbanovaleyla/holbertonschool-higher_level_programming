from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)


# JSON
def read_json():
    with open("products.json", "r") as file:
        return json.load(file)


# CSV
def read_csv():
    products = []
    with open("products.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            row["id"] = int(row["id"])
            row["price"] = float(row["price"])
            products.append(row)
    return products


# SQLITE
def read_sql():
    try:
        conn = sqlite3.connect("products.db")
        cursor = conn.cursor()

        cursor.execute("SELECT id, name, category, price FROM Products")
        rows = cursor.fetchall()

        conn.close()

        return [
            {
                "id": row[0],
                "name": row[1],
                "category": row[2],
                "price": row[3]
            }
            for row in rows
        ]

    except Exception:
        return None


@app.route('/products')
def products():

    source = request.args.get("source")
    product_id = request.args.get("id")

    data = []
    error = None

    # SOURCE HANDLING
    if source == "json":
        data = read_json()

    elif source == "csv":
        data = read_csv()

    elif source == "sql":
        data = read_sql()

        if data is None:
            return render_template("product_display.html", error="Database error")

    else:
        return render_template("product_display.html", error="Wrong source")

    # FILTER BY ID
    if product_id:
        try:
            product_id = int(product_id)
            data = [p for p in data if p["id"] == product_id]

            if not data:
                return render_template("product_display.html", error="Product not found")

        except ValueError:
            return render_template("product_display.html", error="Invalid ID")

    return render_template("product_display.html", products=data, error=error)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
