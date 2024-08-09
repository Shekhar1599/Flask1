from flask import Flask, jsonify, request
from models.data_processor import process_data

app = Flask(__name__)

# Mock data storage
data_storage = {}

@app.route('/fetch_data', methods=['GET'])
def fetch_data():
    # Simulate fetching data from an external service (e.g. Shopify)
    mock_data = [
        {'id': 1, 'name': 'Product 1', 'price': 10.99},
        {'id': 2, 'name': 'Product 2', 'price': 9.99},
        {'id': 3, 'name': 'Product 3', 'price': 12.99}
    ]
    return jsonify(mock_data)

@app.route('/process_data', methods=['POST'])
def process_data_endpoint():
    data = request.get_json()
    processed_data = process_data(data)
    data_storage['processed_data'] = processed_data
    return jsonify({'message': 'Data processed and stored'})

@app.route('/get_processed_data', methods=['GET'])
def get_processed_data():
    return jsonify(data_storage.get('processed_data', {}))

if __name__ == '__main__':
    app.run(debug=True)