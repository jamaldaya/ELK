# Start Elasticsearch

```
docker-compose -f compose-elasticsearch.yml up -d
```

# Logs 

```
docker logs -f es01
```

# Check

```
curl -XGET "localhost:9200/_cat/nodes?v=true&pretty" 
ip           heap.percent ram.percent cpu load_1m load_5m load_15m node.role   master name
192.168.48.2           52          28   3    0.03    0.29     0.49 cdfhilmrstw -      es02
192.168.48.4           33          28   3    0.03    0.29     0.49 cdfhilmrstw *      es01
192.168.48.3           27          28   3    0.03    0.29     0.49 cdfhilmrstw -      es03
```

# Start Kibana

```
docker-compose -f compose-kibana.yml up -d
```

## Test

http://localhost:5601


# Tear down

```
docker-compose -f compose-kibana.yml down
docker-compose -f compose-elasticsearch.yml down --volumes --remove-orphans
```

