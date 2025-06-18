import pytest
from apps.user_app.app import app  # Make sure the import path is correct
from unittest.mock import patch


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_index_route(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"<html" in response.data  # crude HTML check, adjust as needed


@patch("apps.user_app.app.add_user")
def test_add_user_success(mock_add_user, client):
    mock_add_user.return_value = None
    response = client.post(
        "/add_user", data={"name": "John", "email": "john@example.com"}
    )
    assert response.status_code == 302  # Redirect to /users


@patch("apps.user_app.app.add_user", side_effect=Exception("DB error"))
def test_add_user_failure(mock_add_user, client):
    response = client.post(
        "/add_user", data={"name": "Jane", "email": "jane@example.com"}
    )
    assert response.status_code == 200
    assert b"Error: DB error" in response.data


@patch("apps.user_app.app.get_all_users")
def test_user_list(mock_get_all_users, client):
    mock_get_all_users.return_value = [
        ["Alice", "alice@example.com"],
        ["Bob", "bob@example.com"],
    ]
    response = client.get("/users")
    assert response.status_code == 200
    assert b"Alice" in response.data
    assert b"Bob" in response.data
