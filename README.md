# Madstreetden Task
A streaming application which reads data from realtime bitcoin transactions.

1. Receive streaming bitcoin transaction data from here: https://www.blockchain.com/api/api_websocket
2. Stream the transaction log to kafka
3. Analyze the transactions in realtime and count the rate of transactions on a given minute, save this in redis
4. Consume the transactions from a kafka consumer and persist only the transactions made in the last 3 hours
5. Build a rest api in any python framework to read from redis to show the latest transactions

#  Prerequisites

   Python 3 - https://www.python.org/downloads/
   
   Flask-RESTful - https://flask-restful.readthedocs.io/en/latest/
   
   Python3-pip - sudo apt-get install python3-pip
   
   Kafka - https://kafka.apache.org/quickstart
   
   Redis - https://redis.io/topics/quickstart
   
# Installing

   Install follwoing commands in the terminal:
    
    pip3 install redis
    pip3 install pykafka
    pip3 install flask-restful
    pip3 websocket-client 
    pip3 apscheduler
    
  # Deployment
 
   Start Zookeeper server using command:
   
    bin/zookeeper-server-start.sh config/zookeeper.properties
    :
   Start Kafka server using command:
    
    bin/kafka-server-start.sh config/server.properties
   
   Create a kafka topic named "test" using command:
    
    bin/kafka-topics.sh --create --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1 --topic test
    
   List the topics to verify "test" is created using command:
   
    bin/kafka-topics.sh --list --bootstrap-server localhost:9092
    
   Start Redis server using command:
   
    redis-server
    
   Run Python file:
     
     python3 first.py
     python3 second.py
     python3 restapi.py
     
   # API Execution
     
   Display latest 100 transactions
   
    http://127.0.0.1:5000/transactions
    
   Display number of transactions per minute for the last hour
   
    http://127.0.0.1:5000/count_per_minute
    
   Display the bitcoin addresses which has the most aggregate value in transactions in the last 3 hour
    
    http://127.0.0.1:5000/high_value_addr


    
    
