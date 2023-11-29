# Elastic

# Refresh 29.11.2023

* Install 8.
  
## Elasticsearch exercises ...

* Install and configure new version 8. ...
* /config/yaml....
* JVM start heapsize, maxsize
* Create a database/index, fill with data: movie databases, pandas (issues with the Anaconda installation, pandas 1.5.1, ... clip (for CLIP-retrieval ... ) messed up --> running on the python3.9 installation
* Many exercises and continue


### 29.12.2021 ...
...

http://localhost:9200

https://www.elastic.co/downloads/elasticsearch

python -m pip install elasticsearch-async

Python ...

es = Elasticsearch('http://localhost:9200')

c:\Elastic\bin>elasticsearch.bat

Z:\elasticsearch-7.16.2-windows-x86_64\elasticsearch-7.16.2
```
elasticsearch.index(index=index, id=model.id, body=payload)

elasticsearch.delete(index=index, id=model.id)

search = elasticsearch.search(
        index=index,
        body={'query': {'multi_match': {'query': query, 'fields': ['*']}},
              'from': (page - 1) * per_page, 'size': per_page})
              
ids = [int(hit['_id']) for hit in search['hits']['hits']]
    return ids, search['hits']['total']['value']
    
```


