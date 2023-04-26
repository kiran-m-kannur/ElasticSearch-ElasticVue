from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

ELASTICSEARCH_URL = 'http://elasticsearch:9200'
ELASTICVUE_URL = 'http://elasticvue:8080'

@app.route('/search', methods=['POST'])
def search():
    query = request.json.get('query')
    index = request.json.get('index')
    url = f'{ELASTICSEARCH_URL}/{index}/_search'
    headers = {'Content-Type': 'application/json'}
    data = {'query': {'match': {'content': query}}}
    response = requests.post(url, headers=headers, json=data)
    return response.content, response.status_code, response.headers.items()

@app.route('/elasticvue')
def elasticvue():
    return requests.get(ELASTICVUE_URL).content

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)