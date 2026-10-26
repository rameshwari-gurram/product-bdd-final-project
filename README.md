# Product Service — Final Project Evidence

This repository organizes the seven files requested for the final project rubric.

## Required evidence files

1. `tests/factories.py` — fake product factory.
2. `tests/test_models.py` — model tests: Read, Update, Delete, List All, Find by Name, Category, and Availability.
3. `tests/test_routes.py` — API route tests: Read, Update, Delete, List All, and filtered lists.
4. `service/routes.py` — API route implementations.
5. `features/steps/load_steps.py` — BDD background data loader.
6. `features/products.feature` — BDD scenarios.
7. `features/steps/web_steps.py` — browser step definitions.

## Important

This is an evidence-folder starter based on the Python/Behave version of the rubric. Merge these snippets into the course's original Product service project before claiming that the application or tests run. The original project may have different model methods, enum names, route prefixes, HTML element IDs, and flash-message wording.

In particular:
- Confirm `Category.UNKNOWN` and `Category.CLOTHS` exist in `service.models`; if not, use the exact names defined by the original project.
- Confirm whether `Product.all()` returns a list or a query object before using `len(...)` or `.count()`.
- Confirm the actual route prefix and response formats.
- The BDD steps in `products.feature` must match implemented step definitions and the real web UI.
- The example product records and expected values must match the project's test data.

## GitHub submission

After reviewing and testing the files, create a GitHub repository and push the folder. The seven URLs can then be copied from the repository's file pages.
