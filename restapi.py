from flask import Flask
from flask_restful import Api
from flask_restful import Resource
import redis
import json
import operator

r = redis.Redis()
app = Flask(__name__)
api = Api(app)

class showTransactions(Resource):
    def get(self):
        dic = {}
        li = [x for x in r.lrange("transactions", 0, -1)]
        inx = 0
        for i in li:
            dic[inx] = json.loads(i.decode("utf-8"))
            inx += 1
        return dic

class transactionsCount(Resource):
    def get(self, min_value=None):
        
            keys = r.keys('r*')
            keys.sort()
            dic = {}
            for key in keys:
                dic[key.decode("utf-8")[1:]] = r.get(key).decode("utf-8")

            if min_value is None:
                return dic

            if min_value in dic:
                return dic[min_value]

      
class highValueAddr(Resource):
    def get(self):
        
            keys = r.keys('v*')
            dic = {}
            for ikey in keys:
                dic[ikey.decode("utf-8")[1:]] = int(r.get(ikey).decode("utf-8"))
            sorted_x = sorted(dic.items(), key=operator.itemgetter(1), reverse=True)
            return sorted_x[:100]

api.add_resource(showTransactions, '/transactions')
api.add_resource(transactionsCount, '/transactions_count_per_minute/<min_value>', '/count_per_minute/')
api.add_resource(highValueAddr, '/high')
app.run(debug=True)
