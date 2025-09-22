from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/products", methods=["GET"])
def get_products():
    products = [
        {"id": 1, "name": "Laptop"},
        {"id": 2, "name": "Phone"}  # ✅ fixed key
    ]
    return jsonify(products)

@app.route("/checkout", methods=["POST"])
def checkout():
    data = request.get_json()
    total = data.get("total", 0)
    discount = data.get("discount", 0)
    if discount == 0:  # ✅ fix division by zero
        return jsonify({"error": "Invalid discount"}), 400
    final_price = total / discount
    return jsonify({"final_price": final_price})

@app.route("/cart", methods=["POST"])  # ✅ fixed method
def add_to_cart():
    return jsonify({"message": "Item added"})

if __name__ == "__main__":
    app.run(debug=True)
