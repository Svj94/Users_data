import json
import base64


def test_create_user(client):
    user_data = {
        "username": "john_doe",
        "email": "john@example.com",
        "password": "securepassword"
    }
    auth_headers = {
        "Authorization": "Basic " + base64.b64encode(b"admin:password").decode("utf-8")
    }
    response = client.post('/users', data=json.dumps(user_data),
                           headers={**auth_headers, "Content-Type": "application/json"})
    assert response.status_code == 201
    assert 'id' in json.loads(response.data)


def test_get_user(client):
    user_data = {
        "username": "john_doe",
        "email": "john@example.com",
        "password": "securepassword"
    }
    auth_headers = {
        "Authorization": "Basic " + base64.b64encode(b"admin:password").decode("utf-8")
    }
    # Create user
    response = client.post('/users', data=json.dumps(user_data),
                           headers={**auth_headers, "Content-Type": "application/json"})
    user_id = json.loads(response.data)['id']

    # Get user
    response = client.get(f'/users/{user_id}', headers=auth_headers)
    assert response.status_code == 200
    assert json.loads(response.data)['username'] == 'john_doe'


def test_update_user(client):
    user_data = {
        "username": "john_doe",
        "email": "john@example.com",
        "password": "securepassword"
    }
    auth_headers = {
        "Authorization": "Basic " + base64.b64encode(b"admin:password").decode("utf-8")
    }
    # Create user
    response = client.post('/users', data=json.dumps(user_data),
                           headers={**auth_headers, "Content-Type": "application/json"})
    user_id = json.loads(response.data)['id']

    # Update user
    update_data = {
        "email": "john_new@example.com"
    }
    response = client.put(f'/users/{user_id}', data=json.dumps(update_data),
                          headers={**auth_headers, "Content-Type": "application/json"})
    assert response.status_code == 200
    assert json.loads(response.data)['message'] == 'User updated'


def test_delete_user(client):
    user_data = {
        "username": "john_doe",
        "email": "john@example.com",
        "password": "securepassword"
    }
    auth_headers = {
        "Authorization": "Basic " + base64.b64encode(b"admin:password").decode("utf-8")
    }
    # Create user
    response = client.post('/users', data=json.dumps(user_data),
                           headers={**auth_headers, "Content-Type": "application/json"})
    user_id = json.loads(response.data)['id']

    # Delete user
    response = client.delete(f'/users/{user_id}', headers=auth_headers)
    assert response.status_code == 200
    assert json.loads(response.data)['message'] == 'User deleted'
