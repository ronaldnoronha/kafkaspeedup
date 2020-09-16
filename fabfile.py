# Import Fabric's API module
from fabric.api import sudo
from fabric.operations import reboot
from fabric2 import Connection, Config
from invoke import Responder
from fabric2.transfer import Transfer
import os
from time import sleep

with open('./conf/master', 'r') as f:
    array = f.readline().split()
    masterHost = array[0]
    masterPort = array[1]
    user = array[2]
    host = array[3]

config = Config(overrides={'user': user})
conn = Connection(host=host, config=config)
configMaster = Config(overrides={'user': user, 'connect_kwargs': {'password': '1'}, 'sudo': {'password': '1'}})
master = Connection(host=masterHost, config=configMaster, gateway=conn)

slaveConnections = []
configSlaves = Config(overrides={'user': user, 'connect_kwargs': {'password': '1'}, 'sudo': {'password': '1'}})
with open('./conf/slaves', 'r') as f:
    array = f.readline().split()
    while array:
        slaveConnections.append(Connection(host=array[0], config=configSlaves, gateway=conn))
        array = f.readline().split()
with open('./conf/kafka', 'r') as f:
    array = f.readline().split()
    kafka = Connection(host=array[0], config=Config(overrides={'user': user,
                                                                         'connect_kwargs': {'password': '1'},
                                                                         'sudo': {'password': '1'}}), gateway=conn)
sudopass = Responder(pattern=r'\[sudo\] password:',
                     response='1\n',
                     )




def startKafka(dataSize='1000'):
    kafka.run('tmux new -d -s kafka')
    kafka.run('tmux new-window')
    kafka.run('tmux new-window')
    kafka.run('tmux new-window')
    kafka.run('tmux send -t kafka:0 /home/ronald/kafka_2.12-2.5.0/bin/zookeeper-server-start.sh\ '
               '/home/ronald/kafka_2.12-2.5.0/config/zookeeper.properties ENTER')
    sleep(5)
    kafka.run('tmux send -t kafka:1 /home/ronald/kafka_2.12-2.5.0/bin/kafka-server-start.sh\ '
               '/home/ronald/kafka_2.12-2.5.0/config/server.properties ENTER')
    sleep(5)
    kafka.run('tmux send -t kafka:3 python3\ /home/ronald/kafkaConsumer.py ENTER')
    kafka.run('tmux send -t kafka:2 python3\ /home/ronald/kafkaProducer.py\ '+dataSize+' ENTER')




def stopKafka():
    kafka.run('tmux kill-session -t kafka')


def transferToKafka(filename):
    transfer = Transfer(kafka)
    transfer.put(filename)


def testKafka(n='100'):
    transfer = Transfer(kafka)
    transfer.put('./kafkaProducer.py')
    transfer.put('./kafkaConsumer.py')
    startKafka(n)
