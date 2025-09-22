from flask import Flask, jsonify, request

app = Flask(__name__)

# Bug 1: Product list has wrong key
@app.route("/products", methods=["GET"])
def get_products():
    products = [
        {"id": 1, "name": "Laptop"},
        {"id": 2, "title": "Phone"},  # BUG: inconsistent key
    ]
    return jsonify(products)

# Bug 2: Division by zero
@app.route("/checkout", methods=["POST"])
def checkout():
    data = request.get_json()
    total = data.get("total", 0)
    discount = data.get("discount", 0)
    final_price = total / discount  # BUG: crash if discount=0
    return jsonify({"final_price": final_price})

# Bug 3: Wrong method
@app.route("/cart", methods=["GET"])  # Should be POST
def add_to_cart():
    return jsonify({"message": "Item added"})


if __name__ == "__main__":
    app.run(debug=True)
