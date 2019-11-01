import datetime
import redis
import json
from pykafka import KafkaClient
from pykafka.common import OffsetType
from pykafka.exceptions import SocketDisconnectedError
from apscheduler.schedulers.background import BackgroundScheduler

def count_txn_rate():
    global r, count
    temp = count
    count = 0
    pref = "r"
    r.set(pref + str(datetime.datetime.now().strftime("%H:%M")), str(temp), ex=3600)

r = redis.Redis()
client = KafkaClient(hosts="localhost:9092")
topic = client.topics['test']
consumer = topic.get_simple_consumer(
    auto_offset_reset=OffsetType.LATEST,
    reset_offset_on_start=True
)
scheduleRate = BackgroundScheduler()
count = 0
scheduleRate.add_job(count_txn_rate, 'cron', second='0')
scheduleRate.start()
pre = "v"
for message in consumer:
    if message is not None:
        count += 1
        x = message.value.decode("utf-8")
        jsonVar = json.loads(x)
        r.lpush("transactions", json.dumps(jsonVar).encode("utf-8"))
        r.ltrim("transactions", 0, 99)  
        print(message.offset)

        

