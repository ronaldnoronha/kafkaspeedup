# kafkaspeedup

## create topic
```bin/kafka-topics.sh --bootstrap-server localhost:9092 --create --topic <topic> --partitions <number-of-partitions>```

## delete topic
```bin/kafka-topics.sh --zookeeper localhost:2181 --delete --topic <topic>```

