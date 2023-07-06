from src.schemas.user_schema import UserCreate


def test_register_success(test_client):
    user_data = {
        "username": "testuser2",
        "password": "testpassword",
        "email": "test2@example.com"
    }
    user = UserCreate(**user_data)
    response = test_client.post("/register", json=user.dict())
    assert response.status_code == 200
    assert response.json() == {"detail": "User has been registered successfully"}


def test_register_existing_username(test_client):
    user_data = {
        "username": "testuser2",
        "password": "testpassword",
        "email": "test2@example.com"
    }
    user = UserCreate(**user_data)

    response = test_client.post("/register", json=user.dict())

    assert response.status_code == 400
    assert response.json() == {"detail": "Username has already been taken"}


def test_create_post_success(test_client, test_token):
    post_data = {
        "content": "This is a test post"
    }
    response = test_client.post("/posts", json=post_data, headers={"Authorization": f"Bearer {test_token}"})

    assert response.status_code == 200
    assert response.json() == {"message": "Post has been created successfully"}


def test_update_post_success(test_client, test_token, test_post):
    post_id = test_post.id
    post_data = {
        "content": "This is an updated post"
    }
    response = test_client.put(f"/posts/{post_id}", json=post_data, headers={"Authorization": f"Bearer {test_token}"})

    assert response.status_code == 200

    assert response.json() == {"message": "Post has been updated successfully"}
