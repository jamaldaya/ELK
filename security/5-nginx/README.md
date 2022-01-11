
# Add nginx

Add nginx in frontend of kibana

## Generate a CA and certificates for the cluster

```
docker-compose -f create-certs.yml run --rm create_certs
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
docker run --rm -v es_certs:/certs --network=es_elastic docker.elastic.co/elasticsearch/elasticsearch:7.15.2 curl --cacert /certs/ca/ca.crt -u elastic:PleaseChangeMe -s "https://es01:9200/_cat/nodes?v=true&pretty"
ip         heap.percent ram.percent cpu load_1m load_5m load_15m node.role   master name
172.26.0.3           68          32   0    0.06    0.44     0.47 cdfhilmrstw -      es03
172.26.0.4           29          32   0    0.06    0.44     0.47 cdfhilmrstw *      es02
172.26.0.2           61          32   0    0.06    0.44     0.47 cdfhilmrstw -      es01
```

## Setup passwords

```
docker exec -ti es01 /usr/share/elasticsearch/bin/elasticsearch-setup-passwords auto -b -u "https://localhost:9200"
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
docker run -ti --rm -v es_certs:/certs --network=es_elastic docker.elastic.co/elasticsearch/elasticsearch:7.15.2 
curl --cacert /certs/ca/ca.crt -u elastic -s "https://es01:9200/_cat/nodes?v=true&pretty"
Enter host password for user 'elastic':
ip         heap.percent ram.percent cpu load_1m load_5m load_15m node.role   master name
172.26.0.3           68          32   0    0.17    0.26     0.37 cdfhilmrstw -      es03
172.26.0.4           47          32   0    0.17    0.26     0.37 cdfhilmrstw *      es02
172.26.0.2           27          32   0    0.17    0.26     0.37 cdfhilmrstw -      es01
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

```
docker logs -f kib02
```

Expected:
```
{"type":"log","@timestamp":"2021-12-03T09:58:24+00:00","tags":["info","status"],"pid":7,"message":"Kibana is now available (was degraded)"}
```

## Test Kibana

http://localhost:5601
http://localhost:5602

## Start Nginx

```
docker-compose -f compose-nginx.yml up -d
```

## Logs Nginx

```
docker logs -f nginx
```

## Test Kibana via Nginx

http://localhost

Open a Kibana session, check the server used with "docker logs" and stop the container to "docker stop", after a while, the other instance is used.

## Tear down

```
docker-compose -f compose-nginx.yml down
docker-compose -f compose-kibana.yml down
docker-compose -f compose-elasticsearch.yml down --volumes --remove-orphans
```
