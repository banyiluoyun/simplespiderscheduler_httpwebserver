import time
import tornado.ioloop
import tornado.web
import json
print(2)
from scheduler_test import scheduler_spider
print(1)
from apscheduler.schedulers.tornado import TornadoScheduler
import pymysql
import pymongo

localhost = '127.0.0.1'
localport = 27017
client  = pymongo.MongoClient(localhost,localport)
db = client['test_scheduler']
cc = db.scheduler.find_one({"spider_id":'111'})['last_crawl_time']
print(cc)

class mysql_tool(object):
    def spider_state_mysql(self):
        pass

class mongo_tool(object):
    def get_spider_status(self,spider_id):
        self.files = db['spider_list'].find({}, {"spider_id":spider_id})
        self.spider_status = self.files['spider_status']

class spider_switch(tornado.web.RequestHandler):
    # 这里可以用get的form信息,也可以直接用curl来post json数据

    # def get_canshu(self):
    #     self.spider_id = self.get_argument('spider_id')
    #     self.crawl_time = time.time()
    #     self.spider_start = self.get_argument('spider_start')
    #     self.spider_stop = self.get_argument('spider_stop')
    def doscheduler(self) -> object:
        asd = scheduler_spider()
        cron_rule = '*/1 * * * *'
        asd.cron_details(cron_rule)
        # pass

    # @tornado.web.asynchronous
    @tornado.gen.coroutine
    def post(self):

        num1 = self.get_argument('spider_start')
        print(num1)
        # num2 = self.get_argument('spider_stop')
        self.doscheduler()
        d = 1
        print(num1)
        # print(num1,num2)
        # res = json.loads(raw_data.decode())
        s = num1



        self.write(json.dumps({"sum":s,'result':d}))
        print(223232)

application = tornado.web.Application([

    (r"/spider_switch", spider_switch),
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()