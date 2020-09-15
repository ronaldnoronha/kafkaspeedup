from kafka import KafkaConsumer
from json import loads
import sys
from time import time

consumer = KafkaConsumer(
    'test',
     bootstrap_servers=['localhost:9092'],
     auto_offset_reset='earliest',
     enable_auto_commit=True,
     group_id='consumer-group',
     value_deserializer=lambda x: loads(x.decode('utf-8')))

counter = 0
totalReceived = 0
t1 = time()
for message in consumer:
    # print('{} received'.format(message.value))
    counter +=1
    print(counter)
    totalReceived += sys.getsizeof(str(message.value).encode())
print('Total time to receive {}'.format(t1-time()))
print('Total messages received {}'.format(counter))
print('Total data received {} bytes'.format(totalReceived))

