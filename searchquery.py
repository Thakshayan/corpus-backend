from elasticsearch import Elasticsearch


def basic_search(query):
    q = {
        "query": {
            "query_string": {
                "query": query
            }
        },
        "size":101
    }
    return q

def advanced_search(query, fields):
    q = {
        "query": {
            "multi_match": {
                "query":    query,
                "fields": fields
            }
        },
        "size":101
    }
    return q


INDEX = 'lyrics-search-engine'
client = Elasticsearch(HOST="http://localhost", PORT=9200,
                       http_auth=('elastic', 'EMyoDwDL4UH=4GHQW5X='))


def search(query,filter, fields):
    # result = client. (index=INDEX,body=standard_analyzer(query))
    # keywords = result ['tokens']['token']
    # print(keywords)

    print(filter)
    # query_body= process(query)
    query_body = advanced_search(
        query, fields) if filter else basic_search(query)
    print('Making Basic Search ')
    res = client.search(index=INDEX, body=query_body)
    return res
