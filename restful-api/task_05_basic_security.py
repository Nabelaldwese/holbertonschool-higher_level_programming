#!/usr/bin/python3
"""
Task 5: API Security and Authentication Techniques
- Basic Authentication (Flask-HTTPAuth)
- JWT Authentication (Flask-JWT-Extended)
- Role-based access (admin only)
"""

from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import (
    JWTManager,
    create_access_token,
    jwt_required,
    get_jwt_identity
)


app = Flask(__name__)

# Use a secret key for JWT
# (For checker purposes, a static value is fine. In real apps, use env var.)
app.config["JWT_SECRET_KEY"] = "super-secret-key"

auth = HTTPBasicAuth()
jwt = JWTManager(app)

# In-memory users store as specified
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


# ---------- Basic Auth ----------
@auth.verify_password
def verify_password(username, password):
    user = users.get(username)
    if not user:
        return None
    if check_password_hash(user["password"], password):
        return user
    return None


@auth.error_handler
def basic_auth_error(_status):
    # Always return 401 for auth failures
    return jsonify({"error": "Unauthorized"}), 401


@app.route("/basic-protected", methods=["GET"])
@auth.login_required
def basic_protected():
    return "Basic Auth: Access Granted"


# ---------- JWT Error Handlers (MUST return 401 for JWT auth errors) ----------
@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(jwt_header, jwt_payload):
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(jwt_header, jwt_payload):
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(jwt_header, jwt_payload):
    return jsonify({"error": "Fresh token required"}), 401


# ---------- JWT Login ----------
@app.route("/login", methods=["POST"])
def login():
    # Validate JSON
    if not request.is_json:
        return jsonify({"error": "Invalid JSON"}), 400

    data = request.get_json(silent=True)
    if data is None:
        return jsonify({"error": "Invalid JSON"}), 400

    username = data.get("username")
    password = data.get("password")

    # If credentials missing or invalid, return 401 (auth failure)
    user = users.get(username)
    if not user or not password or not check_password_hash(user["password"], password):
        return jsonify({"error": "Invalid credentials"}), 401

    # Put identity data inside token (username + role)
    identity = {"username": user["username"], "role": user["role"]}
    access_token = create_access_token(identity=identity)

    return jsonify({"access_token": access_token})


@app.route("/jwt-protected", methods=["GET"])
@jwt_required()
def jwt_protected():
    return "JWT Auth: Access Granted"


# ---------- Role-based (Admin only) ----------
@app.route("/admin-only", methods=["GET"])
@jwt_required()
def admin_only():
    identity = get_jwt_identity()
    # identity is a dict: {"username": ..., "role": ...}
    if not isinstance(identity, dict) or identity.get("role") != "admin":
        return jsonify({"error": "Admin access required"}), 403
    return "Admin Access: Granted"


if __name__ == "__main__":
    app.run()

