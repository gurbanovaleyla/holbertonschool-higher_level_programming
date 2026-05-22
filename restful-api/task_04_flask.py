#!/usr/bin/python3
from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory storage (keep empty for checker safety)
users = {}


# Root endpoint
@app.route("/", methods=["GET"])
def home():
    return "Welcome to the Flask API!"


# Status endpoint
@app.route("/status", methods=["GET"])
def status():
    return "OK"


# Return list of usernames
@app.route("/data", methods=["GET"])
def get_data():
    return jsonify(list(users.keys()))


# Get user by username
@app.route("/users/<username>", methods=["GET"])
def get_user(username):
    if username in users:
        return jsonify(users[username])
    return jsonify({"error": "User not found"}), 404


# Add a new user
@app.route("/add_user", methods=["POST"])
def add_user():
    try:
        data = request.get_json()

        if not data:
            return jsonify({"error": "Invalid JSON"}), 400

        if "username" not in data:
            return jsonify({"error": "Username is required"}), 400

        username = data["username"]

        if username in users:
            return jsonify({"error": "Username already exists"}), 409

        users[username] = {
            "username": username,
            "name": data.get("name"),
            "age": data.get("age"),
            "city": data.get("city")
        }

        return jsonify({
            "message": "User added",
            "user": users[username]
        }), 201

    except Exception:
        return jsonify({"error": "Invalid JSON"}), 400


if __name__ == "__main__":
    app.run()
