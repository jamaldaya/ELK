vagrant up

vagrant ssh

ps -ef    #gestionnare des taches

ls

/vagrant

/elk

cd /vagrant

ls

clear

curl https://artifacts.elastic.co/downloads/beats/filebeat/filebeat-7.14.0-linux-x86_64.tar.gz --output filebeat-7.14.0-linux-x86_64.tar.gz    #download filebeat

ls

tar -tvpzf filebeat-7.14.0-linux-x86_64.tar.gz  
    #content of the zip file
tar -xvpzf filebeat-7.14.0-linux-x86_64.tar.gz 
     #extract zip file
ls
cd filebeat-7.14.0-linux-x86_64
 ls
mkdir -p /tmp/test/cpp_devices/ds_Test/test.1/      #create a folder for our logs

mkdir -p /vagrant/assembly/test/yat4tango/ds_Test/test.1 

ls

cd ..  
                                                #change directory 2 points means go back a directory
filebeat-7.14.0-linux-x86_64/filebeat -e -c /vagrant/yat4tango.yml --strict.perms=false     #launch filebeat

filebeat-7.14.0-linux-x86_64/filebeat -e -c /vagrant/assembly/filebeatassembly.yml --strict.perms=false

history



echo "$(date +'%Y-%m-%dT%H:%M:%S.%N%z') | DEBUG | A10FFB70 | test/core/server.1 | Hello world" >> /vagrant/assembly/test/yat4tango/ds_Test/test.1/test_core_server.1.log.$(date -u "+%Y%m%d")


echo '<log4j:event logger="flyscan/core/data-merger.1" timestamp="1616322327325" level="INFO" thread="2557475696">
<log4j:message><![CDATA[Processing buffer file /nfs/srv5/spool1/flyscan_in/falcon1x_001251.nxs...]]></log4j:message>
<log4j:NDC><![CDATA[]]></log4j:NDC>
</log4j:event>' >> /vagrant/assembly/test/cppdevices/ds_Test/test.1/test_core_server.1.log.$(date -u "+%Y%m%d")
