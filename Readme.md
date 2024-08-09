# Flask Application for Data Retrieval and Processing

## Setup and Run Locally

1. Create a virtual environment: `python -m venv venv`
2. Activate the virtual environment: `source venv/bin/activate` (on Linux/Mac) or `venv\Scripts\activate` (on Windows)
3. Install dependencies: `pip install -r requirements.txt`
4. Run the Flask application: `python app/app.py`
5. Open a web browser and navigate to `http://localhost:5000` to access the API endpoints

## API Endpoints

### 1. Fetch Data: `GET /fetch_data`

Simulates fetching data from an external service (e.g. Shopify).

### 2. Process Data: `POST /process_data`

Processes the fetched data and stores it in memory.

### 3. Get Processed Data: `GET /get_processed_data`

Returns the processed data stored in memory.

Note: This is a simplified example and you should consider using a more robust data storage solution in a real-world application.