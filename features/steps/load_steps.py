"""BDD step that loads rows from a feature-file table through the API."""

import requests
from behave import given


@given("the following products")
def step_impl(context):
    """Create the products listed in the Gherkin table."""
    base_url = getattr(context, "base_url", "http://localhost:5000")

    for row in context.table:
        data = row.as_dict()
        payload = {
            "name": data["name"],
            "description": data["description"],
            "price": float(data["price"]),
            "available": data["available"].strip().lower() == "true",
            "category": data["category"],
        }

        response = requests.post(
            f"{base_url}/products",
            json=payload,
            headers={"Content-Type": "application/json"},
            timeout=10,
        )
        assert response.status_code == 201, (
            f"Could not create {payload['name']}: "
            f"{response.status_code} {response.text}"
        )
