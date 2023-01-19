from elasticsearch import Elasticsearch


INDEX = 'lyrics-search-engine'
client = Elasticsearch(HOST="http://localhost", PORT=9200)

def basic_query_search(query):
    q = {
        "query": {
            "query_string": {
                "query": query
            }
        },
        "size":101
    }
    return q

def advanced_query_search(query, fields):
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

def full_text_search(query):
    q = {
        "query": {
            "match_phrase_prefix": {
                "text": query
            }
        }
    }
    return q

def fuzzy_search(query):
    q = {
        "query": {
            "fuzzy": {
                "text": {
                    "value": query,
                    "fuzziness": 2
                }
            }
        }
    }
    return q

def search(query,filter, fields):
    
    print(filter)
    if filter:
        query_body = advanced_query_search( query, fields)
    else:
        query_body = basic_query_search(query)
    res = client.search(index=INDEX, body=query_body)
    return res
