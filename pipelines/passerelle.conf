input {
    pipeline {
        address => passerelle
    }
}
filter {
    grok {
        match => { 
            "message" => ['%{PASSERELLE_TIME:[passerelle][timestamp]} \[%{GREEDYDATA:[passerelle][actor]}:%{GREEDYDATA:[passerelle][source]}\] - %{GREEDYDATA:[passerelle][message]}'] 
        }
        pattern_definitions => {
            "PASSERELLE_TIME" => "%{MONTHDAY} %{MONTH} %{YEAR} %{TIME}"
        }
    }
    date {
        match => [ "[passerelle][timestamp]", "dd MMM yyyy HH:mm:ss:SSS" ]
        remove_field => [ "[passerelle][timestamp]" ]
        timezone => "Europe/Paris"
    }
    mutate {
        rename => {
            "[passerelle][message]" => "message"
        }
    }
    mutate {
        rename => { 
            "[fields][beamline]" => "beamline" 
        }
        remove_field => [ "tags", "fields" ]
    }
}
output {   
    pipeline {
        send_to => tangocs
    }
}
