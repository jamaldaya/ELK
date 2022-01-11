# ELK
Internship at SOLEIL project ELK 

# Launch

## Prerequisite for Docker on Windows

```
C:\> wsl -d docker-desktop sysctl -w vm.max_map_count=262144
```

## Start Elasticsearch

```
docker-compose -f elasticsearch-compose.yml up -d
```

## Logs Elasticsearch

```
docker logs -f elasticsearch
```

Expected :
```
{"type": "server", ... , "cluster.name": "es-cluster", "node.name": "elasticsearch", "message": "Active license is now [BASIC]; Security is enabled", ... }
```

## Start Kibana

```
docker-compose -f kibana-compose.yml up -d
```

## Logs Kibana

```
docker logs -f kibana
```

Expected:
```
{"type":"log",...,"message":"Kibana is now available (was degraded)"}
```

## Start Logstash

```
docker-compose -f logstash-compose.yml up -d
```

## Logs Logstash

```
docker logs -f logstash
```

Expected:
```
[...][INFO ][logstash.agent           ] Pipelines running {:count=>14, :running_pipelines=>[:cooxdaemon, :metricbeat, :test, :passerelle, :logdumps, :yat4tango, :javagui, :javadevices, :cppdevices, :tangocs, :trash, :spyc, :cooxviewer, :beats], :non_running_pipelines=>[]}
[...][INFO ][org.logstash.beats.Server][beats][0c8c3ce1f26d9488eca9c5e0fa4277dac76cb990f0190a9230fa11a824399729] Starting server on port: 5044
```
