from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes

POSTS = [
    {"id": 1, "title": "First post", "content": "This is the first post."},
    {"id": 2, "title": "Second post", "content": "This is the second post."},
]


@app.route('/api/posts', methods=['GET'])
def get_posts():
    return jsonify(POSTS)

# POST: Add a new post
@app.route('/api/posts', methods=['POST'])
def add_post():
    data = request.get_json()

    # Check if data is valid
    if not data:
        return jsonify({"error": "Request body must be JSON"}), 400

    # Check if title and content exist
    if "title" not in data or "content" not in data:
        return jsonify({"error": "Both 'title' and 'content' are required"}), 400

    # Find next ID (loop through posts)
    new_id = 1
    for p in POSTS:
        if p["id"] >= new_id:
            new_id = p["id"] + 1

    # Create new post
    new_post = {
        "id": new_id,
        "title": data["title"],
        "content": data["content"]
    }

    POSTS.append(new_post)
    return jsonify(new_post), 201  # 201 = Created

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5002, debug=True)
