# kafkaspeedup

## create topic
```bin/kafka-topics.sh --bootstrap-server localhost:9092 --create --topic <topic> --partitions <number-of-partitions>```

## delete topic
```bin/kafka-topics.sh --zookeeper localhost:2181 --delete --topic <topic>```

## list of topics
```bin/kafka-topics.sh --list --zookeeper localhost:2181```

## get details about the topic
```bin/kafka-topics.sh --describe --zookeeper localhost:2181 --topic <topic-name>```

## change the number of partitions for a topic
```bin/kafka-topics.sh --zookeeper localhost:2181 --alter --topic my_topic_name --partitions <number-of-partitions>```
