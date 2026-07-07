# NOTES

## pip Workflow

1. Created a virtual environment using:
   python -m venv .venv
2. Activated the environment.
3. Installed the requests package using:
   pip install requests
4. Generated requirements.txt using:
   pip freeze > requirements.txt

## uv Workflow

1. Deleted the previous virtual environment.
2. Created a new virtual environment using:
   uv venv
3. Activated the environment.
4. Installed the requests package using:
   uv pip install requests
5. Generated requirements.txt using:
   uv pip freeze > requirements.txt

## Comparison

- pip is the standard Python package manager and is included with Python.
- uv is a modern package manager that performs the same tasks much faster.
- Both can create virtual environments and install packages.
- Both can generate a requirements.txt file.