# Set up basic security for the Elastic Stack

Enable Transport Layer Security (TLS) for internal communication between nodes in your cluster.

## Generate a CA and certificates for the cluster

```
docker-compose -f create-certs.yml run --rm create_certs
```

## Create keystore

```
docker-compose -f create-keystore.yml run --rm create_keystore
```

## Check created files

```
docker-compose -f check.yml run --rm check
```

## Start Elasticsearch

```
docker-compose -f compose-elasticsearch.yml up -d
```

## Logs Elasticsearch

```
docker logs -f es01
```

Expected :
```
{"type": "server", ... , "cluster.name": "es-cluster", "node.name": "es01", "message": "Active license is now [BASIC]; Security is enabled", ... }
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

## Setup password

```
docker exec -ti es01 /usr/share/elasticsearch/bin/elasticsearch-setup-passwords auto -b -u "http://localhost:9200"
Changed password for user apm_system
PASSWORD apm_system = pbwAM9C46ovufBpDQ8Bc

Changed password for user kibana_system
PASSWORD kibana_system = r3PUMAbCbp8fQ9RBvy0s

Changed password for user kibana
PASSWORD kibana = r3PUMAbCbp8fQ9RBvy0s

Changed password for user logstash_system
PASSWORD logstash_system = FOoFoaQEVqYFAmhklJUq

Changed password for user beats_system
PASSWORD beats_system = 8f13wFyveJmbArLxngow

Changed password for user remote_monitoring_user
PASSWORD remote_monitoring_user = oTawmGPagGNU6iAQh5Wn

Changed password for user elastic
PASSWORD elastic = F2ag4imwwKb53bRh4L9x
```

## Check password

```
curl -XGET "localhost:9200/_cat/nodes?v=true&pretty" -u elastic
Enter host password for user 'elastic':
ip           heap.percent ram.percent cpu load_1m load_5m load_15m node.role   master name
192.168.96.3           38          28   1    0.00    0.05     0.14 cdfhilmrstw -      es01
192.168.96.2           43          28   1    0.00    0.05     0.14 cdfhilmrstw -      es02
192.168.96.4           75          28   1    0.00    0.05     0.14 cdfhilmrstw *      es03
```

## Update password in kibana.yml

```
elasticsearch.username: "kibana"
elasticsearch.password: "r3PUMAbCbp8fQ9RBvy0s" 
```
(Warning: use your kibana password)

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

# Tear down

```
docker-compose -f compose-kibana.yml down
docker-compose -f compose-elasticsearch.yml down --volumes --remove-orphans
```

