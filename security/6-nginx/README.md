# Add nginx

Add nginx reverse proxy in frontend of kibana to access default HTTP and add load balancing

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
docker run --rm -v es_certs:/certs --network=es_elastic docker.elastic.co/elasticsearch/elasticsearch:7.16.0 curl --cacert /certs/ca/ca.crt -u elastic:PleaseChangeMe -s "https://es01:9200/_cat/nodes?v=true&pretty"
ip         heap.percent ram.percent cpu load_1m load_5m load_15m node.role   master name
172.26.0.3           68          32   0    0.06    0.44     0.47 cdfhilmrstw -      es03
172.26.0.4           29          32   0    0.06    0.44     0.47 cdfhilmrstw *      es02
172.26.0.2           61          32   0    0.06    0.44     0.47 cdfhilmrstw -      es01
```

## Setup passwords

```
docker exec -ti es01 /usr/share/elasticsearch/bin/elasticsearch-setup-passwords interactive -u "https://localhost:9200"
```

Password for all accounts: DontUse

## Check password

```
docker run -ti --rm -v es_certs:/certs --network=es_elastic docker.elastic.co/elasticsearch/elasticsearch:7.16.0 curl --cacert /certs/ca/ca.crt -u elastic:DontUse -s "https://es01:9200/_cat/nodes?v=true&pretty"
ip         heap.percent ram.percent cpu load_1m load_5m load_15m node.role   master name
172.26.0.3           68          32   0    0.17    0.26     0.37 cdfhilmrstw -      es03
172.26.0.4           47          32   0    0.17    0.26     0.37 cdfhilmrstw *      es02
172.26.0.2           27          32   0    0.17    0.26     0.37 cdfhilmrstw -      es01
```

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

# Create roles for Logstash

```
docker run -ti --rm -v es_certs:/certs -v %cd%/config/roles:/roles --network=es_elastic docker.elastic.co/elasticsearch/elasticsearch:7.16.0 curl --cacert /certs/ca/ca.crt -u elastic:DontUse -s -X POST "https://es01:9200/_security/role/logstash_reader" -H "accept: application/json" -H "Content-Type: application/json" -d @/roles/logstash_reader.json
```

```
docker run -ti --rm -v es_certs:/certs -v %cd%/config/roles:/roles --network=es_elastic docker.elastic.co/elasticsearch/elasticsearch:7.16.0 curl --cacert /certs/ca/ca.crt -u elastic:DontUse -s -X POST "https://es01:9200/_security/role/logstash_writer" -H "accept: application/json" -H "Content-Type: application/json" -d @/roles/logstash_writer.json
```

# Create users for Logstash

```
docker run -ti --rm -v es_certs:/certs -v %cd%/config/users:/users --network=es_elastic docker.elastic.co/elasticsearch/elasticsearch:7.16.0 curl --cacert /certs/ca/ca.crt -u elastic:DontUse -s -X POST "https://es01:9200/_security/user/logstash_user" -H "accept: application/json" -H "Content-Type: application/json" -d @/users/logstash_user.json
```

```
docker run -ti --rm -v es_certs:/certs -v %cd%/config/users:/users --network=es_elastic docker.elastic.co/elasticsearch/elasticsearch:7.16.0 curl --cacert /certs/ca/ca.crt -u elastic:DontUse -s -X POST "https://es01:9200/_security/user/logstash_internal" -H "accept: application/json" -H "Content-Type: application/json" -d @/users/logstash_internal.json
```

## Start Logstash

```
docker-compose -f compose-logstash.yml up -d
```

## Logs Logstash

```
docker logs -f logstash
```

Expected:
```
[2021-12-08T13:16:15,811][INFO ][logstash.agent           ] Pipelines running {:count=>2, :running_pipelines=>[:beats, :default], :non_running_pipelines=>[]}
```

# Check Logstash API

```
docker run -ti --rm --network=es_elastic docker.elastic.co/elasticsearch/elasticsearch:7.16.0 curl -XGET "logstash:9600/?pretty"
```

## Start Filebeat

```
docker-compose -f compose-filebeat.yml up -d
```

## Logs Filebeat

```
docker logs -f filebeat
```

```
2021-12-09T07:17:11.655Z        INFO    [publisher_pipeline_output]     pipeline/output.go:151  Connection to backoff(async(tcp://logstash:5044)) established
```

## Check Logstash and filebeat

Go in Kibana to create "default-*" index pattern and discover one log message "Hello"

Add new log entry:

```
echo Hello ... >> logs/test.log
```

Discover the new message in Kibana

## Tear down

```
docker-compose -f compose-nginx.yml down
docker-compose -f compose-filebeat.yml down
docker-compose -f compose-logstash.yml down
docker-compose -f compose-kibana.yml down
docker-compose -f compose-elasticsearch.yml down --volumes --remove-orphans
```
