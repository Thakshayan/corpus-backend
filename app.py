import json
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from searchquery import search
from elasticsearch_dsl import Index

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/', methods=['GET'])
def index():
    return "Welcome to python server"


@app.route('/search', methods=['POST'])
@cross_origin()
def hello_world():
    data = json.loads(request.data)
    query = data['query']
    print(data)
    if ('filter' in data and 'fields' in data):
        filter = data['filter']
        fields = data['fields']
    elif ('filter' in data ):
        filter = data['filter']
        fields = []
    else:
        filter = False
        fields = []
    res = search(query, filter=filter, fields=fields)
    hits = res['hits']['hits']
    time = res['took']
    # aggs = res['aggregations']
    num_results = res['hits']['total']['value']

    return jsonify({'query': query, 'hits': hits, 'num_results': num_results, 'time': time})


if __name__ == '__main__':
    app.run()
