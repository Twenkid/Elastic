import pandas as pd
from elasticsearch import Elasticsearch

# 29.11.2023 - OK
# "Student": Twenkid
# From various sources
# es1.py

es = Elasticsearch("http://localhost:9200")
print(es) #lasticsearch)
es.info().body

"""
"size": 1000

"query_string": {
              "query": "(new york) OR (big apple)",
               "default_field": "plot"
            }            
            
"""

def search(): #OK!
    resp = es.search(
        index="movies",  
        size=1111,        
        body={   
         "query": {
           "query_string": {
               #"query": "(new york) OR (big apple) OR (washington) OR (los angeles)",
               #"query": "(washington) OR (la)",
               "query": "(alaska)", #(california)", # OR (alaska)",
               "default_field": "plot"
            }                       
           }
          }        
    )
#    "query": {
#"wildcard": {
#"field_name": {
#"value": "*search*pattern*"}


    print(resp.body)
    print(dir(resp))
    
    response_hits = resp['hits']['hits']
    print ('\n', 'number of hits:', len(response_hits))

    # use enumerate() to iterate list of documents:
    for num, doc in enumerate(response_hits):
        print ('\n', 'num:', num, doc)
        # get the document ID
        doc_id = doc['_id']
        print ('_id:', doc_id)

        # get the document's '_source'
        print ('_source:', doc['_source'])

        # get the car's VIN number
        print ('Title:', doc['_source']['title'])
    print("|||||||||||||||||||||||")
    for num, doc in enumerate(response_hits):
       print ('Title # ', num, ':', doc['_source']['title'])
       print ('Director:', doc['_source']['director'])
       print ('Cast:', doc['_source']['cast'])
       print("=================")
       
       
#"default_field": "content"
def search9(): #OK!
    resp = es.search(
        index="movies",  
        size=111,        
        body={   
         "query": {
           "wildcard": {
            #"cast": "schwarz*"
             "director": "*camer*" #James Cameron
            },           
           }
          }         
    )
#    "query": {
#"wildcard": {
#"field_name": {
#"value": "*search*pattern*"}


    print(resp.body)
    print(dir(resp))
    
    response_hits = resp['hits']['hits']
    print ('\n', 'number of hits:', len(response_hits))

    # use enumerate() to iterate list of documents:
    for num, doc in enumerate(response_hits):
        print ('\n', 'num:', num, doc)
        # get the document ID
        doc_id = doc['_id']
        print ('_id:', doc_id)

        # get the document's '_source'
        print ('_source:', doc['_source'])

        # get the car's VIN number
        print ('Title:', doc['_source']['title'])
    print("|||||||||||||||||||||||")
    for num, doc in enumerate(response_hits):
       print ('Title:', doc['_source']['title'])
       print ('Director:', doc['_source']['director'])
       print ('Cast:', doc['_source']['cast'])
       print("=================")
       

def search8(): #OK!
      
    resp = es.search(
        index="movies",  
        size=111,        
        body={   
         "query": {
           "wildcard": {
            "cast": "*dicaprio"
            }
           }
          }         
    )
    
    
#    "query": {
#"wildcard": {
#"field_name": {
#"value": "*search*pattern*"}


    print(resp.body)
    print(dir(resp))
    
    response_hits = resp['hits']['hits']
    print ('\n', 'number of hits:', len(response_hits))

    # use enumerate() to iterate list of documents:
    for num, doc in enumerate(response_hits):
        print ('\n', 'num:', num, doc)
        # get the document ID
        doc_id = doc['_id']
        print ('_id:', doc_id)

        # get the document's '_source'
        print ('_source:', doc['_source'])

        # get the car's VIN number
        print ('Title:', doc['_source']['title'])
    print("|||||||||||||||||||||||")
    for num, doc in enumerate(response_hits):
       print ('Title:', doc['_source']['title'])
       print ('Director:', doc['_source']['director'])
       print("=================")
    
    
def search7(): #OK but nothing found?
      
    resp = es.search(
        index="movies",  
        size=111,        
        body={   
         "query": {
           "query_string": {
           "fields": [
        "cast*"
         ],
         "query": "*dicapr"        
        }
       }        #body
       }
    )

    print(resp.body)
    
def search6(): #OK nothing found
      
    resp = es.search(
        index="movies",  
        size=111,        
        body={   
              "query": {  
              "bool":{
              "must": [ 
              {
                "match_phrase": {
                          "cast": "dicaprio"
                          },
              }#,
              #{
              #"query_string":{
              #    "query": "dicaprio"  
              # }             
              # }                
              ]
              }        
           }
           }
    )

    print(resp.body)
    
    
def search5(): #OK nothing found
      
    resp = es.search(
        index="movies",  
        size=111,        
        body={   
              "query": {  
              "bool":{
              "must": [ 
              {
                "match": {
                          "field_name": "cast"
                          },
              },
              {
               "query_string":{
                  "query": "dicaprio"  
                }             
               }                
              ]
              }        
           }
           }
    )

    print(resp.body)
    
    
def search4(): #OK
      
    resp = es.search(
        index="movies",  
        size=111,        
        body={   
             "query": {                  
               "query_string":{
                  "query": "*dicapr"               
                }              

               }        
           }
    )

    print(resp.body)
    
def search3(): #OK
      
    resp = es.search(
        index="movies",  
        size=111,        
        body={   
             "query": {                  
               "query_string":{
                  "query": "*caprio"               
                }              
               }        
           }
    )

    print(resp.body)
    
def search2():
      
    resp = es.search(
        index="movies",                
        size=111,              
        query={                        
                "bool": {
                    "must": {
                        "match_phrase": {
                            "cast": "dicaprio", # "jack nicholson" arnold   #schwarzenegger dicaprio
                        }
                    },
                    "filter": {"bool": {"must_not": {"match_phrase": {"director": "roman polanski"}}}},
                },                
           }    
    )

    print(resp.body)
    

def search1():
      
    resp = es.search(
        index="movies",
        query={
                "bool": {
                    "must": {
                        "match_phrase": {
                            "cast": "schwarzenegger", # "jack nicholson" arnold 
                        }
                    },
                    "filter": {"bool": {"must_not": {"match_phrase": {"director": "roman polanski"}}}},
                },
            },            
    )

    print(resp.body)

def prepare():
    df = (
        pd.read_csv("j:/archive/wiki_movie_plots_deduped.csv")
        .dropna()
        .sample(5000, random_state=42)
        .reset_index()
    )

    mappings = {
            "properties": {
                "title": {"type": "text", "analyzer": "english"},
                "ethnicity": {"type": "text", "analyzer": "standard"},
                "director": {"type": "text", "analyzer": "standard"},
                "cast": {"type": "text", "analyzer": "standard"},
                "genre": {"type": "text", "analyzer": "standard"},
                "plot": {"type": "text", "analyzer": "english"},
                "year": {"type": "integer"},
                "wiki_page": {"type": "keyword"}
        }
    }

    es.indices.create(index="movies", mappings=mappings)

    for i, row in df.iterrows():
        doc = {
            "title": row["Title"],
            "ethnicity": row["Origin/Ethnicity"],
            "director": row["Director"],
            "cast": row["Cast"],
            "genre": row["Genre"],
            "plot": row["Plot"],
            "year": row["Release Year"],
            "wiki_page": row["Wiki Page"]
        }
                
        es.index(index="movies", id=i, document=doc)
	
def bulk():
    from elasticsearch.helpers import bulk

    bulk_data = []
    for i,row in df.iterrows():
        bulk_data.append(
            {
                "_index": "movies",
                "_id": i,
                "_source": {        
                    "title": row["Title"],
                    "ethnicity": row["Origin/Ethnicity"],
                    "director": row["Director"],
                    "cast": row["Cast"],
                    "genre": row["Genre"],
                    "plot": row["Plot"],
                    "year": row["Release Year"],
                    "wiki_page": row["Wiki Page"],
                }
            }
        )
    bulk(es, bulk_data)

def refresh():
    es.indices.refresh(index="movies")
    es.cat.count(index="movies", format="json")

'''
resp = es.search(
    index="movies",
    query={
            "bool": {
                "must": {
                    "match_phrase": {
                        "cast": "jack nicholson",
                    }
                },
                "filter": {"bool": {"must_not": {"match_phrase": {"director": "roman polanski"}}}},
            },
        },            
)

print(resp.body)
'''

search()

#control theory
#state-space model
