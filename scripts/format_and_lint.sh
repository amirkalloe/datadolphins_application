npm --prefix ./frontend/ run lint
cd backend
poetry run python -m flake8 app
poetry run python -m flake8 common
poetry run python -m black app
poetry run python -m black common