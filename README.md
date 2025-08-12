# Booky — Flask CRUD Example

Simple Flask app demonstrating a clean structure, CRUD operations, Flask-SQLAlchemy, Flask-Migrate, Flask-WTF and Bootstrap.

## Features

- Create / Read / Update / Delete (CRUD) for `Book` model
- Form validation with Flask-WTF (CSRF protection)
- Database migrations with Flask-Migrate (Alembic)
- App factory + Blueprints pattern
- Bootstrap 5 frontend (CDN)

## Tech stack

- Python 3.11+ (tested on 3.12)
- Flask 3.1.1
- Flask-SQLAlchemy 3.1.1
- Flask-Migrate 4.1.0
- Flask-WTF 1.2.2
- python-dotenv for environment variables

## Quick start

```bash
git clone <repo-url>
cd booky-flask
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

cp .env.example .env
# Edit .env (SECRET_KEY, DATABASE_URL if needed)

export FLASK_APP=run.py
flask db init
flask db migrate -m "init"
flask db upgrade

flask --app run
# open http://127.0.0.1:5000


Project structure
(see repo root for full files; main app is under app/)

Notes & tips
Don't use the development secret key in production; set SECRET_KEY to a secure random value.

To switch DB, change DATABASE_URL (e.g., PostgreSQL) and run migrations.

Consider adding tests, linting (flake8/black), CI, and Docker for production-ready repo


License
MIT
```
