from flask import Flask, request, Response
import requests

app = Flask(__name__)

ELASTICSEARCH_URL = "http://elasticsearch:9200"

@app.route('/', defaults={'path': ''}, methods=['GET', 'POST', 'PUT', 'DELETE'])
@app.route('/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def forward_request(path):
    url = f"http://elasticvue:8080/{path}"

    headers = dict(request.headers)
    data = request.get_data()

    try:
        response = requests.request(
            method=request.method,
            url=f"{ELASTICSEARCH_URL}/{path}",
            headers=headers,
            data=data,
            timeout=5,
        )
        return Response(response.content, response.status_code, headers=dict(response.headers))

    except requests.exceptions.RequestException as e:
        return Response(str(e), 500, headers={'Content-Type': 'text/plain'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
