from flask import Flask, request, jsonify, make_response
from flask_cors import CORS
import json
import os

app = Flask(__name__)
CORS(app)

def load_data():
    json_file_path = os.path.join(os.path.dirname(__file__), '../public/q-vercel-python.json')
    with open(json_file_path, "r") as f:
        return json.load(f)

@app.route('/api', methods=['GET'])
def get_marks():
    data = load_data()
    names = request.args.getlist('name')
    marks = [item['marks'] for item in data if item['name'] in names]

    response = make_response(jsonify({"marks": marks}))
    response.headers["Access-Control-Allow-Origin"] = "https://exam.sanand.workers.dev"
    response.headers["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type, Authorization"
    return response

if __name__ == '__main__':
    app.run(debug=True)
