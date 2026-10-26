"""Product API route examples.

Merge these handlers into the original service/routes.py. Keep the original
application setup, imports, route prefix, error handling, and content checks.
"""

from flask import jsonify, request

from service.models import Product


# Assumes `app` is the Flask application from the original project and
# `check_content_type` is already defined/imported there.


@app.route("/products/<int:product_id>", methods=["GET"])
def read_product(product_id):
    """Read one product by ID."""
    product = Product.find(product_id)
    if product:
        return jsonify(product.serialize()), 200
    return jsonify({"error": "Product not found"}), 404


@app.route("/products/<int:product_id>", methods=["PUT"])
def update_product(product_id):
    """Update one product by ID."""
    check_content_type("application/json")
    product = Product.find(product_id)
    if not product:
        return jsonify({"error": "Product not found"}), 404

    data = request.get_json()
    product.deserialize(data)
    product.update()
    return jsonify(product.serialize()), 200


@app.route("/products/<int:product_id>", methods=["DELETE"])
def delete_product(product_id):
    """Delete one product by ID."""
    product = Product.find(product_id)
    if not product:
        return jsonify({"error": "Product not found"}), 404

    product.delete()
    return "", 204


@app.route("/products", methods=["GET"])
def list_products():
    """List all products or filter by name, category, or availability."""
    name = request.args.get("name")
    category = request.args.get("category")
    available = request.args.get("available")

    # This implementation applies one filter at a time.
    if name:
        products = Product.find_by_name(name)
    elif category:
        products = Product.find_by_category(category)
    elif available is not None:
        products = Product.find_by_availability(
            available.strip().lower() == "true"
        )
    else:
        products = Product.all()

    return jsonify([product.serialize() for product in products]), 200
