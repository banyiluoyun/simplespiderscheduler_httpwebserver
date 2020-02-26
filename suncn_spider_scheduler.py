#!/usr/bin/env python
# -*- coding:utf-8 -*-
import time
import tornado.ioloop
import tornado.web
import json
import pymysql
import pymongo
from apscheduler.schedulers.blocking import BlockingScheduler
localhost = '127.0.0.1'
localport = 27017
client  = pymongo.MongoClient(localhost,localport)
db = client['suncn_spider']
class mysql_tool(object):
    def spider_state_mysql(self):
        pass

class mongo_tool(object):
    def get_spider_status(self,spider_id):
        self.files = db['spider_list'].find({}, {"spider_id":spider_id})
        self.spider_status = self.files['spider_status']
mongotool = mongo_tool()
class spider_switch(tornado.web.RequestHandler):
    # 这里可以用get的form信息,也可以直接用curl来post json数据

    def __init__(self):
        self.spider_id = self.get_argument('spider_id')
        self.crawl_time = time
        self.spider_start = self.get_argument('spider_start')
        self.spider_stop = self.get_argument('spider_stop')
        self.spider_state = mongotool.get_spider_status(self.spider_id)



    def post(self):

        num1 = self.get_argument('spider_start')
        num2 = self.get_argument('spider_stop')
        print(num1)
        # print(num1,num2)
        # res = json.loads(raw_data.decode())
        s = num1 + num2



        self.write(json.dumps({"sum":s}))


application = tornado.web.Application([

    (r"/spider_switch", spider_switch),
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()