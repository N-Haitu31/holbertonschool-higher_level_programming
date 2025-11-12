from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/items')
def items():
    with open('items.json') as f:
        data = json.load(f)
    items_list = data.get('items', [])

    return render_template('items.html', items=items_list)

@app.route('/products')
def products():
    source = request.args.get("source")
    prod_id = request.args.get("id")

    error = None
    products = []

    if source == "json":
        products = load_json_products()
    elif source == "csv":
        products = load_csv_products()
    else:
        error = "Wrong source"

    # Filtrage par id si demandé et pas d’erreur source
    if not error and prod_id:
        try:
            prod_id = int(prod_id)
            filtered = [p for p in products if p["id"] == prod_id]
            if not filtered:
                error = "Product not found"
            products = filtered
        except ValueError:
            error = "Invalid id parameter"
            products = []

    return render_template("product_display.html", products=products, error=error)

def load_json_products(filename="products.json"):
    try:
        with open(filename) as f:
            return json.load(f)
    except Exception:
        return []

def load_csv_products(filename="products.csv"):
    products = []
    try:
        with open(filename) as f:
            reader = csv.DictReader(f)
            for row in reader:
                # Conversion id et price en bon type
                product = {
                    "id": int(row.get("id", 0)),
                    "name": row.get("name", ""),
                    "category": row.get("category", ""),
                    "price": float(row.get("price", 0))
                }
                products.append(product)
    except Exception:
        pass
    return products

if __name__ == '__main__':
    app.run(debug=True, port=5000)
