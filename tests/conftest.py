import pytest
from app import app as flask_app
from app.db import db
from app.models import User
from werkzeug.security import generate_password_hash

@pytest.fixture
def app():
    flask_app.config.update({
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": "sqlite:///test.db",
    })

    with flask_app.app_context():
        db.create_all()
        admin_user = User(username="admin", email="admin@example.com", password_hash=generate_password_hash("password"))
        db.session.add(admin_user)
        db.session.commit()

    yield flask_app

    with flask_app.app_context():
        db.session.remove()
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def runner(app):
    return app.test_cli_runner()
