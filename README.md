# Elastic

# Refresh 29.11.2023

* Install 8.
  
## Elasticsearch exercises ...

* Install and configure new version 8.11.1 ...  https://www.elastic.co/downloads/elasticsearch

* /config/yaml....
* JVM start heapsize, maxsize

c:\Elastic\bin>set ES_JAVA_OPTS=-Xms1g -Xmx1g

(No "" quotes ... 500M ... etc.)

c:\Elastic\bin>elasticsearch.bat

* Create a database/index, fill with data: movie databases, pandas (issues with the Anaconda installation, pandas 1.5.1, ... clip (for CLIP-retrieval ... ) messed up --> running on the python3.9 installation

* Do many exercises, explore queries, tasks; add your data and use cases etc. Practise also pandas ...

Valuable tutorials etc.:

* https://dylancastillo.co/elasticsearch-python/
* https://github.com/dylanjcastillo/random/blob/main/elasticsearch.ipynb?ref=dylancastillo.co
* https://www.kaggle.com/datasets/jrobischon/wikipedia-movie-plots/  -- 31 MB, 35000 movies
* https://github.com/kiq005/movie-recommendation/blob/master/src/dataset/wiki_movie_plots_deduped.csv



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


