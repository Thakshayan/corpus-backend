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
            "match_phrase" : {
                "lyrics": query
            }
        },
        "size":101
    }
    return q

def multi_language_search(query):
    q = {
        "query": {
            "bool": {
                "should": [
                    { "match_phrase": { "lyrics": query } },
                    { "match_phrase": { "lyrics.tamil_analyzer": query } }
                ]
            }
        },
        "size": 101
    }
    return q

def fuzzy_search(query):
    q = {
        "query": {
            "fuzzy": {
                "song_name": {
                    "value": query,
                    "fuzziness": 1
                }
            }
        },
        "size":101
    }
    return q

def match_phrase_search():
    q = {
        
     "query": {
        "match_phrase": {
            "song_name": {
                "query":"Nee Illai Endraal"
            } 
        }
    },

        "size":101
    }
    return q


# def fuzzy_search(query):
#     q = {
#         "query": {
#             "fuzzy": {
#                 "text": {
#                     "value": query,
#                     "fuzziness": "AUTO",
#                     "prefix_length": 0,
#                     "max_expansions": 100
#                 }
#             }
#         },
#         "size":101
#     }
#     return q

def search(query,filter, fields):
    
    print(filter)
    if filter == "full":
        query_body = match_phrase_search()
        print(query_body)
    elif filter == "fuzzy":
        query_body = fuzzy_search(query)
        
    elif filter:
        query_body = advanced_query_search(query, fields)
    else:
        query_body = basic_query_search(query)
    print(query_body)
    res = client.search(index=INDEX, body=query_body)
    print(res)
    return res
