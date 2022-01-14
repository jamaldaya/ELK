vagrant ssh  

#Example Log Yat4tango
echo "$(date +'%Y-%m-%dT%H:%M:%S.%N%z') | DEBUG | A10FFB70 | test/core/server.1 | Hello world" >> /tmp/test/cpp_devices/ds_Test/test.1/test_core_server.1.log.$(date -u "+%Y%m%d")

#Example assembly
echo "$(date +'%Y-%m-%dT%H:%M:%S.%N%z') | DEBUG | A10FFB70 | test/core/server.1 | Hello world" >> /vagrant//assembly/test/yat4tango/ds_Test/test.1/test_core_server.1.log.$(date -u "+%Y%m%d")


cat test_core_server.1.log.20210809

echo "$(date +'%Y-%m-%dT%H:%M:%S.%N%z') | DEBUG | A10FFB70 | test/core/server.1 | Hello world" >> /tmp/test/cpp_devices/ds_Test/test.1/test_core_server.1.log.$(date -u "+%Y%m%d")

#Example Single line passerelle
echo 10 Nov 2019 14:01:36:024 [Eiger_ptycho3D_Nov2019_v2:GenerateValueFrom_CurrentListePosZ] - Generating value :-3.1991891874488 >> d:\elk\test\test.log

#Example Log multiline passerelle
(
echo 10 Nov 2019 14:01:57:827 [Eiger_ptycho3D_Nov2019_v2:MoveMotorTZ] - exception message is: IDL:Tango/DevFailed:1.0
echo Error Level 0:
echo - desc: Axis position is not writable in this state!
echo - origin: PowerPMACAxis::write_position
echo - reason: OPERATION_NOT_ALLOWED
echo - severity: ERROR
)>>/vagrant/test/test.log


sudo systemctl start elasticsearch      #launch elasticsearch

curl -X GET "localhost:9200/_template/yat4tango_template?pretty"
              #Verify that template is installed#

curl -X GET "localhost:9200/_cat/indices/*?v&s=index&pretty"
              #Health status#

curl -X GET "localhost:9200/_cluster/health?pretty"
			#Cluster health

curl localhost:9200/_cat/shards
			#list shards

curl -X GET "localhost:9200/_cat/shards/*?v&s=index&pretty"
 			#Shards Health

curl -X GET "localhost:9200/_cluster/health?pretty" 
            #Yellow means no replica#contains number of nodes and shards
curl -X GET "localhost:9200/yat4tango-2021.08.10/_search?pretty" -H 'Content-Type: application/json' -d' { "query": { "match_all": {}}}'
                                ####CORRECT THE DATE#####
            #THIS WILL SHOW US THE RECEPTION OF LOG IN ELASTIC SEARCH# 
curl -X GET "localhost:9200/yat4tango-2021.08.10?pretty"
            #Verify mapping of data in the index#

curl localhost:9200/_nodes/process?pretty
			#show date of every node


history


FOR TRUE LOGS:


#FIRST DELETE ALL OLD LOGS AND INDICES

curl -X DELETE "localhost:9200/yat4tango-*?pretty"


curl -X GET "localhost:9200/soleil?pretty"

#FOR DELETING DIRECTORIES AND EVERYTHING INSIDE

rm -rf ds_Flyscan

#DELETE FILEBEAT CACHE

rm -r data/registry/filebeat

#MOVE NEZ DATA INSIDE CPP_DEVICES

mv ds_Flyscan/ cpp_devices

#LIST ALL INDICES

curl -X GET "localhost:9200/_cat/indices/yat*?v&s=index&pretty"



#Delete the zip file in the directory of logs


curl -X PUT localhost:9200/_cluster/settings -H "Content-Type: application/json" -d '{ "persistent": { "cluster.max_shards_per_node": "3000" } }'

#create nodes
cluster.name: CLUSTER_NAME
node.name: ${HOSTNAME}
node.master: true
node.data: true
discovery.zen.ping.unicast.hosts: ["INTERNAL_IP_SERVER_1", "INTERNAL_IP_SERVER_2"]
discovery.zen.minimum_master_nodes: 2


#Create index


curl -X PUT "localhost:9200/soleil?pretty"

#index settings
curl -XGET 'localhost:9200/soleil/_settings?pretty'


#Edit index settings

curl -X PUT "localhost:9200/soleil/_settings?pretty" -H 'Content-Type: application/json' -d'
{            
  "index" : {        
    "routing.allocation.total_shards_per_node" : 20    
  }           
}'

#close the index

curl -XPOST 'localhost:9200/lookupindex/_close'

#open the index

curl -XPOST 'localhost:9200/lookupindex/_open'

#shard sizing in an index
##################################################################################
curl -X PUT "localhost:9200/soleil?pretty" -H 'Content-Type: application/json' -d'
{
   "settings": {
      "number_of_replicas": 0,
      "number_of_shards": 5,
      "refresh_interval": "30s"
  }
}'

####################################################################################

curl -X PUT "localhost:9200/yat4tango?pretty" -H 'Content-Type: application/json' -d'
{
   "settings": {
      "number_of_replicas": 0,
      "number_of_shards": 5
  }
}'


#show empty indices         

curl -X GET "localhost:9200/_cat/count/soleil?v=true&pretty"




[WARN ][logstash.outputs.elasticsearch][cooxviewer][e34340242eee1ad1db0d00e090d3dad5b52a7655c163d1a4a7740c51ce68971e]
Could not index event to Elasticsearch. {:status=>400, :action=>["index", {:_id=>nil, :_index=>"soleil-2020.09.07", 
:routing=>nil}, {"ecs"=>{"version"=>"1.10.0"}, "tags"=>["cooxviewer", "beats_input_codec_plain_applied"], "@version"=>"1",
"host"=>{"name"=>"localhost.localdomain"}, "agent"=>{"name"=>"localhost.localdomain", "ephemeral_id"=>"6f4b59d1-fb78-4c28-ba6e-0d3ece428c45",
"version"=>"7.14.0", "type"=>"filebeat", "id"=>"5f61175d-e407-49d3-b9a3-3efa77d25554", "hostname"=>"localhost.localdomain"},
"cooxviewer"=>{"level"=>"INFO", "message"=>"Client - connection opened : /172.19.1.6:33001 [marssupervision.engine1.event]"},
"input"=>{"type"=>"log"}, "@timestamp"=>2020-09-07T08:02:05.495Z,
"log"=>{"file"=>{"path"=>"/vagrant/assembly/ds_RecordingManager/coox/mars/CooxViewer/tcp_io0.log.2"},
"offset"=>38859}}], :response=>{"index"=>{"_index"=>"soleil-2020.09.07", "_type"=>"_doc", "_id"=>nil,
"status"=>400, "error"=>{"type"=>"validation_exception","reason"=>"Validation Failed: 1: this action would add [2] shards,
but this cluster currently has [1000]/[1000] maximum normal shards open;"}}}}



[2021-09-15T13:09:39,436][WARN ][logstash.outputs.elasticsearch][cppdevices][62492695d933728f438151c7ae27d1c22f6d509536c592174d0b10ab262b3e15] 
Could not index event to Elasticsearch. {:status=>400, :action=>["index", {:_id=>"69399857", :_index=>"soleil", :routing=>nil}, {"ndc"=>{},
"device"=>{"domain"=>"i06-m-cx", "member"=>"falconx1.1", "family"=>"dt", "name"=>"i06-m-cx/dt/falconx1.1"}, "@timestamp"=>2021-03-26T07:36:50.336Z,
"@version"=>"1", "host"=>{"name"=>"localhost.localdomain"}, "thread"=>"5680", "input"=>{"type"=>"log"}, "log"=>{"flags"=>["multiline"], "offset"=>72678,
"file"=>{"path"=>"/vagrant/assembly/ds_RecordingManager/cppdevices/cpplogs-20210326-22h46/i06-m-cx_dt_falconx1.1.log.1"}},
"agent"=>{"ephemeral_id"=>"3c90d315-7268-46bc-9ee2-05c1c3a8b1ee", "id"=>"5f61175d-e407-49d3-b9a3-3efa77d25554", "hostname"=>"localhost.localdomain",
"type"=>"filebeat", "version"=>"7.14.0", "name"=>"localhost.localdomain"}, "ecs"=>{"version"=>"1.10.0"}, "event"=>{}, "tags"=>["cppdevices",
"beats_input_codec_plain_applied"], "message"=>{}, "level"=>"INFO"}], :response=>{"index"=>{"_index"=>"soleil", "_type"=>"_doc", "_id"=>"69399857",
"status"=>400, "error"=>{"type"=>"mapper_parsing_exception", 
"reason"=>"failed to parse field [message] of type [text] in document with id '69399857'. Preview of field's value: '{}'",
"caused_by"=>{"type"=>"illegal_state_exception", "reason"=>"Can't get text on 
a START_OBJECT at 1:723"}}}}}





[2021-09-16T13:13:21,130][ERROR][logstash.agent] 
Failed to execute action {:action=>LogStash::PipelineAction::Create/pipeline_id:yat4tango, :exception=>"LogStash::ConfigurationError",
:message=>"Expected one of [ \\t\\r\\n], \"#\", \"{\", \"-\", [0-9], [A-Za-z_], '\"', \"'\", \"}\" at line 33,
column 73 (byte 1055) after output {   \r\n    elasticsearch {\r\n        hosts => [\"localhost:9200\"]\r\n        
index => {name => \"yat4tango\"\r\n                  settings =>\"routing.allocation.total_shards_per_node\" ",
:backtrace=>["/usr/share/logstash/logstash-core/lib/logstash/compiler.rb:32:in `compile_imperative'",
"org/logstash/execution/AbstractPipelineExt.java:187:in `initialize'", "org/logstash/execution/JavaBasePipelineExt.java:72:in `initialize'",
"/usr/share/logstash/logstash-core/lib/logstash/java_pipeline.rb:47:in `initialize'",
"/usr/share/logstash/logstash-core/lib/logstash/pipeline_action/create.rb:52:in `execute'",
"/usr/share/logstash/logstash-core/lib/logstash/agent.rb:391:in `block in converge_state'"]}



curl -X PUT "localhost:9200/soleil?pretty" -H 'Content-Type: application/json' -d'
{
   "settings": {
      "number_of_replicas": 0,
      "number_of_shards": 5
  }
}'


curl -X PUT "localhost:9200/soleil/_settings?pretty" -H 'Content-Type: application/json' -d'
{            
  "index" : {        
    "number_of_replicas" : 0    
  }           
}'





DOCKER AND ELASTICSEARCH:



RUN CONTAINER:
docker run -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" docker.elastic.co/elasticsearch/elasticsearch:7.15.0

The vm.max_map_count setting must be set in the docker-desktop container:

wsl -d docker-desktop #connect to linux wsl

sysctl vm.max_map_count #it returns the maximum virtual memory size

sysctl -w vm.max_map_count=262144 #augment the memory size of wsl
sysctl -w vm.max_map_count=524288
sysctl -w vm.max_map_count=1048576

echo "vm.max_map_count = 262144" >>  /etc/sysctl.d/00-alpine.conf #persistently have this memory at 262144

docker-compose down --volumes #config down





docker-compose -f elastic-compose.yml up





Download filebeat from ELK website on windows
then 
filebeat -e -c filebeatassembly.yml


#Always maintain virtual memory agter shell exits
However, after adding ulimits, attempting a docker-compose up will result in a separate, but related, error:
ERROR: [1] bootstrap checks failed
[1]: max virtual memory areas vm.max_map_count [65530] is too low, increase to at least [262144]
ERROR: Elasticsearch did not exit normally — check the logs at /usr/share/elasticsearch/logs/docker-cluster.log
This is Elasticsearch letting us know that the default OS limits for mmapfs are too low. To resolve this:
sysctl -w vm.max_map_count=262144
In order to have this change persist after shell exit:
Edit /etc/sysctl.conf
Add vm.max_map_count=262144


#Configuration of Elasticsearch nodes
docker inspect es1


curl -X PUT -u elastic:PleaseChangeMe "http://localhost:9200/_ilm/policy/ilm-policy" -H "accept: application/json" -H "Content-Type: application/json" -d @config/logstash/ilm/ilm-policy.json

curl -X GET -u elastic:PleaseChangeMe "localhost:9200/_cat/indices/*?v&s=index&pretty"

curl -X DELETE -u elastic:PleaseChangeMe "localhost:9200/soleil-*?pretty"

curl -X PUT -u elastic:PleaseChangeMe "localhost:9200/soleil?pretty" -H "Content-Type: application/json" -d'
{
   "settings": {
      "number_of_replicas": 0,
      "number_of_shards": 5
  }
}''
