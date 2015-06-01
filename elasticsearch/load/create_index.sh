curl -XPOST localhost:9200/wiki -d '{
    "settings" : {
        "number_of_shards" : 8,
        "analysis": {
            "analyzer": {
                "fixedlength": {
                    "type": "custom",
                    "tokenizer": "fixedlength"
                }
            },
            "tokenizer": {
                "fixedlength": {
                    "type": "pattern",
                    "pattern" : "(.{1,16384})",
                    "group" : "0"
                }
            }
        }
    },
    "mappings" : {
        "articles" : {
            "_source" : { "enabled" : false },
            "properties" : {
                "text" : { "type" : "string", "index" : "analyzed", "analyzer" : "fixedlength" },
                "url" : { "type" : "string", "index" : "not_analyzed" },
                "title" : { "type" : "string", "index" : "not_analyzed" }
            }
        }
    }
}'
