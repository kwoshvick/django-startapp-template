# Django Startapp Template

## Project Setup

### Prerequisites
Before using this template, ensure you have the following installed:

- [uv](https://github.com/astral-sh/uv) (for package management)

### Depenedencies
These are the depencies installed in the template installed:

- django
- djangorestframework
- markdown (Markdown support for the browsable API.)
- django-filter (Filtering support)
- django-silk (profiling and inspection)
- django-environ (env variables management)
- ruff (linting and formatting)
- pytest (testing)
- pytest-cov (coverage)
- django_extensions (To auto-import necessary packages and modules from Django when we start a shell)

### Installation

1. **Create a virtual environment** (if not using uv globally):
   ```sh
   uv venv .venv
   source .venv/bin/activate
   ```

2. **Install dependencies:**
   ```sh
   uv pip install django ruff
   ```

3. **Create a Django project and app:**
   ```sh
   django-admin startproject myproject
   cd myproject
   django-admin startapp myapp
   ```

## Code Formatting & Linting

### Ruff Configuration
To configure Ruff, create a `pyproject.toml` file in the root directory:

```toml
[tool.ruff]
line-length = 88
select = ["E", "F", "W", "I"]  # Example rules
```

### Running Ruff
To check for linting issues:
```sh
ruff check .
```
To apply automatic fixes:
```sh
ruff check --fix .
```


### Running test
To run test:
```sh
uv run pytest .
```
To run coverage:
```sh
coverage run -m pytest .
```


## Running the Django Server

1. **Apply migrations:**
   ```sh
   python manage.py migrate
   ```
2. **Run the development server:**
   ```sh
   python manage.py runserver
   ```


## Directory Structure
```
myproject/
│── manage.py
│── config/
│   │── __init__.py
│   │── settings.py
│   │── urls.py
│   │── wsgi.py
│── apps

│── myapp/
│   │── migrations/
│   │── __init__.py
│   │── admin.py
│   │── apps.py
│   │── models.py
│   │── tests.py
│   │── views.py
```

## Next Steps
- Configure `settings.py`
- Add models, views, and templates
- Set up `urls.py` for the app
- Implement authentication and permissions (if required)

---
This template provides a quick start for Django app development using `uv` for package management and `ruff` for linting.
