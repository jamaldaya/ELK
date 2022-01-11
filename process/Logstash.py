#Yat4tango
input {
    beats {
        port => "5044"
    }
}
filter {
    if ! ("yat4tango" in [tags]) {
        drop { }
    }
    dissect {
        mapping => {
            "message" => "%{timestamp_nanos->} | %{level} | %{thread_id} | %{[device][name]} | %{message}"   #"message" => "2020-10-12T12:58:36.075157226+0200 | DEBUG | A10FFB70 | test/core/server.1 | Hello world",
        }
    }
   if "_dissectfailure" in [tags] {
   drop { }
    }
    grok {
        match => { "[device][name]" => "(?<[device][domain]>[^_/]+)/(?<[device][family]>[^_/]+)/(?<[device][member]>%{GREEDYDATA})" }
    }
    grok {
        match => { "[log][file][path]" => "%{GREEDYDATA}/(?<[device][process]>ds_[^/]+)/(?<[device][instance]>[^/]+)/%{GREEDYDATA}" }
    }
    date {
        match => [ "timestamp_nanos", "yyyy-MM-dd'T'HH:mm:ss.SSSSSSSSSZ" ]
    }
    mutate {
        rename => { "[fields][beamline]" => "beamline" }
        remove_field => [ "input", "tags", "fields" ]
    }
}
# Vers Elastic
output {   
    elasticsearch {
        hosts => ["localhost:9200"]
        index => "yat4tango-%{+YYYY.MM.dd}"
        manage_template => true
        template => "/vagrant/yat4tango_template.json"
        template_name => "yat4tango_template"
    }
}
#Vers Console

output {
    stdout { codec => rubydebug }
}


#CppDevices
input {
    beats {
        port => "5044"
    }
}
filter {
    if ! ("cppdevices" in [tags]) {
        drop { }
    }
    fingerprint {
        source => "message"
        target => "[@metadata][fingerprint]"
        method => "MURMUR3"
    }
    mutate {
        gsub => ["message", "log4j:", ""]
    }
    xml {
        source => "message"
        target => "event"
        force_array => false
    }
    if "_xmlparsefailure" in [tags] {
        drop { }
    }
    date {
        match => [ "[event][timestamp]", "UNIX_MS" ]
        remove_field => [ "[event][timestamp]" ]
        timezone => "Europe/Paris"
    }
    mutate {
        rename => {
            "[event][logger]" => "[device][name]"
            "[event][thread]" => "[thread]"
            "[event][level]" => "[level]"
            "[event][NDC]" => "[ndc]"
            "[event][message]" => "[message]"
        }
    }
    grok {
        match => { "[device][name]" => "(?<[device][domain]>[^_/]+)/(?<[device][family]>[^_/]+)/(?<[device][member]>%{GREEDYDATA})" }
    }
}
output {
    elasticsearch {
        hosts => ["localhost:9200"]
        index => "cppdevices-%{+YYYY.MM.dd}"
        document_id => "%{[@metadata][fingerprint]}"
    }
}

#SPYC
input {
    beats {
        port => "5044"
    }
}
filter {
    if ! ("spyc" in [tags]) {
        drop { }
    }
    grok {
        match => { "message" => ['%{SPYC_TIME:[spyc][timestamp]}\n%{NOTLINEBREAK:[spyc][command]}\n%{GREEDYDATA:[spyc][message]}'] }
         pattern_definitions => {
          "SPYC_TIME" => "%{DAY}, %{MONTHDAY} %{MONTH} %{YEAR} %{TIME}"
          "NOTLINEBREAK" => "[^\n]+"
        }
    }
    mutate {
        remove_field => ["message"]
    }
    if "([Ee]rr?(?:or)?|ERR?(?:OR)?)" in [spyc][message] {
        mutate {add_field => {"[spyc][level]" => "ERROR"}
                add_tag => ["ALOG"]
                } 
        }
    else {
        mutate {add_field => {"[spyc][level]" => "INFO"}
                add_tag => ["ALOG"]
                }
    }
    if ! ("ALOG" in [tags]){
        drop { }
    }
    date {
        match => [ "[spyc][timestamp]", "EEE, dd MMM yyyy HH:mm:ss" ]
        remove_field => [ "[spyc][timestamp]" ]
        timezone => "Europe/Paris"
           
    }
}

output {
    elasticsearch {
       hosts => ["localhost:9200"]
       index => "spyc-%{+YYYY.MM.dd}"
    }
}

output {
    stdout { codec => rubydebug }
}

#LOGDUMPS
input {
    beats {
        port => "5044"
    }
}

filter {
    if ! ("logdumps" in [tags]) {
        drop { }
    }
    grok { 
           match => { "message" => ['%{NOTLINEBREAK:[logdumps][server]}\n%{WORD:[logdumps][Started]}: %{TIMESTAMP_ISO8601:[logdumps][startdate]}\n%{WORD:[logdumps][Aborted]}: %{TIMESTAMP_ISO8601:[logdumps][abortdate]}\n%{NOTLINEBREAK:[logdumps][host]}\n%{NOTLINEBREAK:[logdumps][reason]}\n%{NOTLINEBREAK:[logdumps][why]}\n%{VERYGREEDYDATA:[logdumps][stacktrace]}'] }
         pattern_definitions => {
          "NOTLINEBREAK" => "[^\n]+"
          "VERYGREEDYDATA" => "(?<message>(.|\r|\n)*)"
        }
    }
    date { 
        match => [ "[logdumps][abortdate]", "ISO8601" ]
        timezone => "Europe/Paris"
    }

}

output {
    stdout { codec => rubydebug }
}

output {
    elasticsearch {
       hosts => ["localhost:9200"]
       index => "logdumps-%{+YYYY.MM.dd}"
    }
}

output {
    elasticsearch {
       hosts => ["localhost:9200"]
       index => "soleil"
    }
}


#JAVAGUI
input {
    beats {
        port => "5044"
    }
}

filter {
    grok {
        match => { "[log][file][path]" => ['%{LASTONE:[javagui][pathinfo]}'] }
        pattern_definitions => {"LASTONE" => "([^/]*-)"}
        }
    grok {
        match => { "[javagui][pathinfo]" => ['%{BEAMLINE:[javagui][beamline]}-']}
        pattern_definitions => {"BEAMLINE" => "[A-Za-z]+"}
        remove_field => [ "[javagui][pathinfo]" ]
        }
    grok {
           match => { "message" => ['%{JAVAGUIDATE:[javagui][date]} +%{TIME:[javagui][time]} +%{LOGLEVEL:[javagui][level]} +%{GREEDYDATA:[javagui][threadname]}:%{NUMBER:[javagui][tasknumber]} - %{GREEDYDATA:[javagui][message]}'] }
           pattern_definitions => {"JAVAGUIDATE" => "%{YEAR}\-%{MONTHNUM}\-%{MONTHDAY}"}
           remove_field => [ "message" ]
        }
    mutate {
        add_field => { "[@metadata][ts]" => "%{[javagui][date]} %{[javagui][time]}" }
        }
    date {
        match => [ "[@metadata][ts]", "yyyy-MM-dd HH:mm:ss.SSS" ]
        remove_field => ["[javagui][date]"]
        remove_field => ["[javagui][time]"]
        timezone => "Europe/Paris"
        }
    }

output {
    elasticsearch {
       hosts => ["localhost:9200"]
       index => "javagui-%{+YYYY.MM.dd}"
    }
}

#JAVADEVICES
input {
    beats {
        port => "5044"
    }
}
filter {
    if ! ("javadevices" in [tags]) {
        drop { }
    }
    grok { 
       match => { "message" => ['%{LOGLEVEL:[javadevices][level]} +%{TIMESTAMP_ISO8601:[javadevices][timestamp]} +%{NOSPACE:[javadevices][devicename]} \- %{GREEDYDATA:[javadevices][threadname]} \| %{GREEDYDATA:[javadevices][method]}:%{INT:[javadevices][tasknumber]} - %{GREEDYDATA:[javadevices][message]}'] 
        }                   #What we do here is that we create a grok filter that matches with every log that had a log parse failure
        pattern_definitions => {
          "NOSPACE" => "\S*"
            }
        remove_field => [ "message" ]
    }  
    
    if "_grokparsefailure" in [tags] {
    	grok { 
       		match => { "message" => ['%{LOGLEVEL:[javadevices][level]} +%{TIMESTAMP_ISO8601:[javadevices][timestamp]} +\- %{GREEDYDATA:[javadevices][threadname]} \| %{GREEDYDATA:[javadevices][method]}:%{INT:[javadevices][tasknumber]} - %{GREEDYDATA:[javadevices][message]}'] 
        	}                   #What we do here is that we create a grok filter that matches with every log that had a log parse failure
        	pattern_definitions => {
         	 "NOSPACE" => "\S*"
            }
       		 remove_field => [ "message" ]
    	}
#ERROR 2020-10-14 17:01:13,239  - Thread-11 | o.t.s.admin.AdminDevice.run:253 - kill server
	}

    date {
       match => [ "[javadevices][timestamp]", "ISO8601" ]
       remove_field => [ "[javadevices][timestamp]" ]
       timezone => "Europe/Paris"
       }
    }

output {
    elasticsearch {
       hosts => ["localhost:9200"]
       index => "javadevices-%{+YYYY.MM.dd}"
    }
}

#output {
#    stdout { codec => rubydebug }
#}




#Passerelle
input {
    beats {
        port => "5044"
    }
}
filter {
    if ! ("passerelle" in [tags]) {
        drop { }
    }
    grok {
        match => { "message" => ['%{PASSERELLE_TIME:[passerelle][timestamp]} \[%{GREEDYDATA:[passerelle][actor]}:%{GREEDYDATA:[passerelle][source]}\] - %{GREEDYDATA:[passerelle][message]}'] }
        pattern_definitions => {
          "PASSERELLE_TIME" => "%{MONTHDAY} %{MONTH} %{YEAR} %{TIME}"
        }
    }
    if "_grokparsefailure" in [tags] {
   drop { }
    }
    date {
        match => [ "[passerelle][timestamp]", "dd MMM yyyy HH:mm:ss:SSS" ]
        remove_field => [ "[passerelle][timestamp]" ]
        timezone => "Europe/Paris"
    }
    mutate{
        rename => {"[passerelle][message]" => "message"}
    }
}
output {
    elasticsearch {
        hosts => ["localhost:9200"]
        index => "passerelle-%{+YYYY.MM.dd}"
    }
}

#COOXDAEMON
input {
    beats {
        port => "5044"
    }
}

filter {
    grok { 
           match => { "message" => ['%{COOXDAEMON_TIME:[cooxdaemon][timestamp]} +\- +\[%{LOGLEVEL:[cooxdaemon][level]}\] +: +%{GREEDYDATA:[cooxdaemon][message]}'] }
           pattern_definitions => { "COOXDAEMON_TIME" => "%{MONTHDAY}/%{MONTHDAY}/%{YEAR} +%{TIME}"
                                    "VERYGREEDYDATA" => "(?<message>(.|\r|\n)*)"   
           }
           remove_field => [ "message" ]
           #remove_field => [ "@timestamp" ]
    }
#    date { 
#        match => [ "[cooxdaemon][timestamp]", "dd/MM/yy HH:mm:ss.SSS" ]
#        remove_field => ["[cooxdaemon][timestamp]"]
#        timezone => "Europe/Paris"
#    }

}

output {
    elasticsearch {
       hosts => ["localhost:9200"]
       index => "cooxdaemon-%{+YYYY.MM.dd}"
    }
}

#COOXVIEWER
input {
    beats {
        port => "5044"
    }
}

filter {
    if ! ("cooxviewer" in [tags]) {
        drop { }
    }
    grok { 
           match => { "message" => ['%{COOXVIEWER_TIME:[cooxviewer][timestamp]} - \[%{LOGLEVEL:[cooxviewer][level]}\] : %{GREEDYDATA:[cooxviewer][message]}'] }
           pattern_definitions => { "COOXVIEWER_TIME" => "%{MONTHNUM}/%{MONTHDAY}/%{YEAR} %{TIME}"}
           remove_field => [ "message" ]
    }
    date { 
        match => [ "[cooxviewer][timestamp]", "MM/dd/yy HH:mm:ss.SSS" ]
        remove_field => ["[cooxviewer][timestamp]"]
        timezone => "Europe/Paris"
    }
    if ("_grokparsefailure" in [tags]) or ("_dateparsefailure" in [tags]) {
            grok { 
           match => { "message" => ['%{COOXVIEWER_TIME:[cooxviewer][timestampf]} +%{LOGLEVEL:[cooxviewer][level]} +%{GREEDYDATA:[cooxviewer][threadname]}:%{INT:[cooxviewer][threadnumber]} +- +%{GREEDYDATA:[cooxviewer][message]}'] }
           pattern_definitions => { "COOXVIEWER_TIME" => "%{MONTHDAY} %{MONTH} %{YEAR} %{TIME}"}
           remove_field => [ "message" ]
                }
           date { 
            match => [ "[cooxviewer][timestampf]", "dd MMM yyyy HH:mm:ss.SSS" ]
            remove_field => ["[cooxviewer][timestampf]"]
            timezone => "Europe/Paris"
                }
    }

}

output {
    elasticsearch {
       hosts => ["localhost:9200"]
       index => "cooxviewer-%{+YYYY.MM.dd}"
    }
}

