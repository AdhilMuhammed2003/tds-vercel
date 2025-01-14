from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import os

app = Flask(__name__)
CORS(app)
# Load data from JSON file in the `public/` directory
def load_data():
    json_file_path = os.path.join(os.path.dirname(__file__), '../public/q-vercel-python.json')
    with open(json_file_path, "r") as f:
        return json.load(f)

@app.route('/api', methods=['GET'])
def get_marks():
    # Load data from the JSON file
    data = load_data()

    # Extract 'name' parameters from the request
    names = request.args.getlist('name')

    # Find marks for the requested names
    marks = [item['marks'] for item in data if item['name'] in names]

    return jsonify({"marks": marks})

if __name__ == '__main__':
    app.run(debug=True)

