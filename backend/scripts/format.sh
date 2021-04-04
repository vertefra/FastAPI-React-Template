
# Isort

isort app/**.py

# Black

black -t py38 app/

# MyPy

mypy --exclude '__init__.py' -v app/**.py