vagrant ssh

sudo id

sudo systemctl stop logstash

sudo systemctl status logstash

sudo systemctl start logstash #start logstash automatically

sudo systemctl status logstash

ls

cd /vagrant

ls

touch yat4tango.conf

ls

which logstash         #where is logstash binary

sudo /usr/share/logstash/bin/logstash -f yat4tango.conf --config.reload.automatic   #start logstash manually


sudo /usr/share/logstash/bin/logstash -f /vagrant/yat4tango.conf --config.reload.automatic #il faut écrire le bon chemin de yat4tango.conf





sudo /usr/share/logstash/bin/logstash /vagrant/assembly/pipelineassembly.yml --config.reload.automatic #logstash assembly launch

#take out -e or -f for not ignoring pipelines.yml





ps -ef                  #gestionnaire des taches

sudo kill 29022         #le numero signfie le pid process ID

history









#When we finish 

exit

vagrant halt












# Allume avec pipelines

sudo systemctl start logstash

tail -f logstash-plain.log

tail -f test.log