#!/usr/bin/python3
from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import (
    JWTManager, create_access_token,
    jwt_required, get_jwt_identity
)

app = Flask(__name__)
auth = HTTPBasicAuth()
app.config['JWT_SECRET_KEY'] = 'my_secret_key'
jwt = JWTManager(app)

users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}


@auth.verify_password
def verify_password(username, password):
    """
    Verify the provided username and password for Basic Authentication.

    Args:
        username (str): The username provided by the client.
        password (str): The password provided by the client.

    Returns:
        dict or None: The user dictionary if authentication is successful,
                      None otherwise.
    """
    user = users.get(username)
    if user and check_password_hash(user['password'], password):
        return user
    return None


@app.route('/basic-protected')
@auth.login_required
def basic_protected():
    """
    Endpoint protected by Basic Authentication.

    Returns:
        str: A success message confirming access via Basic Auth.
    """
    return "Basic Auth: Access Granted"


@app.route('/login', methods=['POST'])
def login():
    """
    Authenticate a user and issue a JWT token if credentials are valid.

    Expects a JSON payload with 'username' and 'password'.

    Returns:
        Response: JSON containing the access token if successful,
                  or an error message with HTTP 401 if authentication fails.
    """
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    user = users.get(username)

    if not user or not check_password_hash(user['password'], password):
        return jsonify({"error": "Invalid credentials"}), 401

    access_token = create_access_token(
        identity={"username": username, "role": user["role"]}
    )
    return jsonify(access_token=access_token)


@app.route('/jwt-protected')
@jwt_required()
def protected():
    """
    Endpoint protected by JWT authentication.

    Requires a valid JWT token in the Authorization header.

    Returns:
        str: A success message confirming access via JWT.
    """
    return "JWT Auth: Access Granted"


@app.route('/admin-only')
@jwt_required()
def admin_only():
    """
    Endpoint restricted to users with the 'admin' role.

    Requires a valid JWT token. If the authenticated user is not an admin,
    access is denied.

    Returns:
        Response: Success message if the user is admin,
                  or error message with HTTP 403 otherwise.
    """
    current_user = get_jwt_identity()
    if current_user["role"] != "admin":
        return jsonify({"error": "Admin access required"}), 403
    return "Admin Access: Granted"


@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    """
    Handle cases where a JWT token is missing or not provided.

    Args:
        err (str): The error message provided by Flask-JWT-Extended.

    Returns:
        Response: JSON error message with HTTP 401 status.
    """
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    """
    Handle cases where the provided JWT token is invalid.

    Args:
        err (str): The error message.

    Returns:
        Response: JSON error message with HTTP 401 status.
    """
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(err):
    """
    Handle cases where the JWT token has expired.

    Args:
        err (str): The error message.

    Returns:
        Response: JSON error message with HTTP 401 status.
    """
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    """
    Handle cases where the JWT token has been revoked.

    Args:
        err (str): The error message.

    Returns:
        Response: JSON error message with HTTP 401 status.
    """
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    """
    Handle cases where a fresh JWT token is required.

    Args:
        err (str): The error message.

    Returns:
        Response: JSON error message with HTTP 401 status.
    """
    return jsonify({"error": "Fresh token required"}), 401


if __name__ == "__main__":
    """
    Run the Flask application in debug mode.
    """
    app.run()
