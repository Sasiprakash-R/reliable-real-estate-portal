from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient

app = Flask(__name__)
CORS(app)

# MongoDB Setup
client = MongoClient("mongodb://localhost:27017/")
db = client["user_db"]
collection = db["users"]

@app.route("/add_user", methods=["POST"])
def add_user():
    data = request.json
    # Insert data into MongoDB
    result = collection.insert_one(data)
    return jsonify({"message": "User added", "id": str(result.inserted_id)})

@app.route("/get_users", methods=["GET"])
def get_users():
    users = list(collection.find({}, {"_id": 0}))  # Exclude MongoDB ObjectID from response
    return jsonify(users)

if __name__ == "__main__":
    app.run(debug=True)
