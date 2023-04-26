from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

ES_URL = "http://elasticsearch:9200"
KB_URL = "http://kibana:5601"

@app.route('/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def forward_request(path):
    if path.startswith('elasticsearch'):
        url = ES_URL + '/' + path.split('/', 1)[1]
    else:
        url = KB_URL + '/' + path
    headers = request.headers
    method = request.method
    data = request.get_data()
    response = requests.request(method, url, headers=headers, data=data)
    excluded_headers = ['content-encoding', 'content-length', 'transfer-encoding', 'connection']
    response_headers = [(name, value) for (name, value) in response.raw.headers.items() if name.lower() not in excluded_headers]
    return (response.content, response.status_code, response_headers)
