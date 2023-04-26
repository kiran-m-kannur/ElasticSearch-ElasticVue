from flask import Flask, request, Response
import requests
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)

ELASTICSEARCH_URL = "http://127.0.0.1:9200"

@app.route('/', methods=['GET', 'POST', 'PUT', 'DELETE'])
# @cross_origin()
@app.route('/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
@cross_origin()
def forward_request(path):
    url = f"http://127.0.0.1:9200/{path}"
    app.logger.info("XYZ")
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
        # app.logger.info(response,"Abc")
        return Response(response.content, response.status_code, headers=dict(response.headers))

    except requests.exceptions.RequestException as e:
        return Response(str(e)+"PQR", 500, headers={'Content-Type': 'text/plain'})
        


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
