from flask import Flask, request, jsonify, make_response
from flask_cors import CORS
import json
import os

app = Flask(__name__)

# Enable CORS for all routes
CORS(app, resources={r"/api/*": {"origins": "*"}})

# Load data from JSON file
def load_data():
    json_file_path = os.path.join(os.path.dirname(__file__), '../public/q-vercel-python.json')
    with open(json_file_path, "r") as f:
        return json.load(f)

@app.route('/api', methods=['GET', 'OPTIONS'])
def get_marks():
    # Load data from JSON
    data = load_data()

    # Extract 'name' parameters from the request
    names = request.args.getlist('name')

    # Find marks for the requested names
    marks = [item['marks'] for item in data if item['name'] in names]

    # Create a response
    response = make_response(jsonify({"marks": marks}))
    response.headers["Access-Control-Allow-Origin"] = "https://exam.sanand.workers.dev"  # Set to specific origin in production
    response.headers["Access-Control-Allow-Methods"] = "GET, OPTIONS"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type, Authorization"
    return response

if __name__ == '__main__':
    app.run(debug=True)
