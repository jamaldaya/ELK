# Set up minimal security for Elasticsearch

Adding password protection in the minimal security configuration

## Start Elasticsearch

```
docker-compose -f compose-elasticsearch.yml up -d
```

## Logs Elasticsearch

```
docker logs -f es01
```

## Check Elasticsearch

```
curl -XGET "localhost:9200/_cat/nodes?v=true&pretty" 
{
  "error" : {
    "root_cause" : [
      {
        "type" : "security_exception",
        "reason" : "missing authentication credentials for REST request [/_cat/nodes?v=true&pretty]",
        "header" : {
          "WWW-Authenticate" : "Basic realm=\"security\" charset=\"UTF-8\""
        }
      }
    ],
    "type" : "security_exception",
    "reason" : "missing authentication credentials for REST request [/_cat/nodes?v=true&pretty]",
    "header" : {
      "WWW-Authenticate" : "Basic realm=\"security\" charset=\"UTF-8\""
    }
  },
  "status" : 401
}
```

## Setup passwords

```
docker exec -ti es01 /usr/share/elasticsearch/bin/elasticsearch-setup-passwords interactive -u "http://localhost:9200"
```

Password for all accounts: DontUse

## Check password

```
curl -XGET "localhost:9200/_cat/nodes?v=true&pretty" -u elastic:DontUse  
ip           heap.percent ram.percent cpu load_1m load_5m load_15m node.role   master name
192.168.96.3           38          28   1    0.00    0.05     0.14 cdfhilmrstw -      es01
192.168.96.2           43          28   1    0.00    0.05     0.14 cdfhilmrstw -      es02
192.168.96.4           75          28   1    0.00    0.05     0.14 cdfhilmrstw *      es03
```

## Start Kibana

```
docker-compose -f compose-kibana.yml up -d
```

## Logs Kibana

```
docker logs -f kib01
```
Expected:
```
{"type":"log","@timestamp":"2021-12-03T09:58:24+00:00","tags":["info","status"],"pid":7,"message":"Kibana is now available (was degraded)"}
```

## Test Kibana

http://localhost:5601

Username: elastic
Password: DontUse

# Tear down

```
docker-compose -f compose-kibana.yml down
docker-compose -f compose-elasticsearch.yml down --volumes --remove-orphans
```

