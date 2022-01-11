input {
    pipeline {
        address => spyc
    }
}
filter {
    grok {
        match => { 
            "message" => ['%{SPYC_TIME:[spyc][timestamp]}\n%{NOTLINEBREAK:[log][origin][function]}\n%{GREEDYDATA:[spyc][message]}'] 
        }
        pattern_definitions => {
          "SPYC_TIME" => "%{DAY}, %{MONTHDAY} %{MONTH} %{YEAR} %{TIME}"
          "NOTLINEBREAK" => "[^\n]+"
        }
    }
    mutate{
        rename => {
            "[spyc][message]" => "message"
        }
    }
    if "([Ee]rr?(?:or)?|ERR?(?:OR)?)" in [spyc][message] {
        mutate {
            add_field => {
                "[log][level]" => "ERROR"
            }
        }
    } else {
        mutate {
            add_field => {
                "[log][level]" => "INFO"
            }
        }
    }
    date {
        match => [ "[spyc][timestamp]", "EEE, dd MMM yyyy HH:mm:ss" ]
        remove_field => [ "[spyc][timestamp]" ]
        timezone => "Europe/Paris"
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
