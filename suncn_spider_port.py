#!/bin/env python
import tornado.ioloop
import tornado.web
import tornado.web
import json
from tornado.concurrent import run_on_executor
from concurrent.futures import ThreadPoolExecutor
# from scheduler_test import main as scheduler_main
import pymongo

localhost = '127.0.0.1'
localport = 27017
client  = pymongo.MongoClient(localhost,localport)
db = client['test_scheduler']
cc = db.scheduler.find_one({"spider_id":'111'})['last_crawl_time']

class mysql_tool(object):
    def spider_state_mysql(self):
        pass
class Mongo_Tool(object):
    def find(self,spider_id,):
        self.result = db.sheduler.find({"spider_id":spider_id})

        return self.result
    def insert_spider(self,kwargs):
        try:
            self.result = db.scheduler.insert(kwargs)
            return {'resulterror':"ok"}
        except Exception as e:
            return {'resulterror':e}
mongo_tool = Mongo_Tool

class spider_switch(tornado.web.RequestHandler):
    executor = ThreadPoolExecutor(10)

    def add_spider(self,spider_id,):

        pass


    def post(self):
        num1 = self.get_argument('spider_start')
        cron_rule = self.get_argument('cron_rule')
        sig_start = int(self.get_argument('spider_start'))
        sig_stop = int(self.get_argument('spider_stop'))
        sig_spider_id = self.get_argument('spider_id')




        result_additems = self.items_add(sig_spider_id, cron_rule)
        result_start = self.items_start(sig_start)
        # self.items_stop(sig_stop)

        self.write(json.dumps({"sum": num1, 'result': 122, 'cron_rule': cron_rule,'result':result_start,'result_add':result_additems}))
application = tornado.web.Application([

    (r"/spider_switch", spider_switch),
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()