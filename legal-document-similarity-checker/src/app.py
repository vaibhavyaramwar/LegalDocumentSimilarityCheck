from flask import Flask, request, jsonify
from upload.uploader import Uploader
from query.query_handler import QueryHandler
from pipeline.data_pipeline import DataPipeline

app = Flask(__name__)

# Initialize components
uploader = Uploader()
query_handler = QueryHandler()
data_pipeline = DataPipeline()

@app.route('/upload', methods=['POST'])
def upload_document():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    result = uploader.upload(file)
    return jsonify(result), 200

@app.route('/query', methods=['GET'])
def query_clause():
    clause = request.args.get('clause')
    if not clause:
        return jsonify({'error': 'No clause provided'}), 400
    results = query_handler.query(clause)
    return jsonify(results), 200

@app.route('/process', methods=['POST'])
def process_data():
    result = data_pipeline.process()
    return jsonify(result), 200

if __name__ == '__main__':
    app.run(debug=True)