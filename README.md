# Elastic
Elasticsearch exercises and systems

Install...

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


