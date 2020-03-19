# coding:utf-8
from apscheduler.executors.pool import ThreadPoolExecutor
from apscheduler.jobstores.mongodb import MongoDBJobStore
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from scrapy import cmdline
import os
# import subprocess

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.schedulers.tornado import TornadoScheduler
from apscheduler.jobstores import mongodb
from multiprocessing import Process
from apscheduler.triggers.cron import CronTrigger
import pymongo
text = 111
import datetime
localhost = '127.0.0.1'
port = 27017
dbname = 'test_scheduler'
client_scheduler = pymongo.MongoClient(localhost,port)
db = client_scheduler[dbname]
from scrapy import cmdline
# executors = {
#       'default': ThreadPoolExecutor(20)
#   }
# jobstores = {
#     'mongo': MongoDBJobStore(),
#     # 'default': SQLAlchemyJobStore(url='sqlite:///jobs.sqlite')
# }

# sched = BackgroundScheduler
spider = [{'spider_id':'111',"spider_name":'sasa'},]
spider_id = spider[0]["spider_id"]
def find_cron_rule(spider_id):
    cron_rule = db.scheduler.find_one({'spider_id':spider_id})['cron_rule']
    return cron_rule
def find_trigger_id(spider_id):
    trigger_id = db.scheduler.find_one({"spider_id":spider_id})['trigger_id']
    return trigger_id
#
def spider_job(spider_id):
    print(spider_id)
    spider_name = db.scheduler.find_one({'spider_id':spider_id})['spider_name']
    # spider_name = 'news_pengpai.py'
    spider_path = db.scheduler.find_one({'spider_id':spider_id})['spider_path']
    os.chdir(spider_path)
    commend_spider = "scrapy runspider " + spider_name
    print(commend_spider)
    # print(os.getcwd())

    c_path = os.getcwd()
    print(c_path)
    # subprocess.Popen(commend_spider)
    os.system(commend_spider)
    # cmdline.execute(commend_spider.split())
    print(1)
# def process_111(spider_id):
#     p = Process(target=spider_job,args=(spider_id,))
#     p.start()
#     p.join()
#
# def main(spider_id):
#      cron_rule = find_cron_rule(spider_id=spider_id)
#      trigger_id = find_trigger_id(spider_id=spider_id)
#      cscs = sched.add_job(my_job, 'cron',minute='10',args=(spider_id) )
#      print(cscs)



        # self.sched.add_job(self.my_job, 'cron',second='*',args=['text'])
# def scheduler_start():
#
#     try:
#         sched.start(paused=False)
#         # sched.start()
#     except (KeyboardInterrupt, SystemExit):
#         pass
#
# def scheduler_stop(self):
#     # sched.shutdown()
#     sched.shutdown(wait=True)
def aps_test(spider):
    print(spider)
    c = spider['spider_id']
    print(spider['spider_id'])
    if c == '111':
        print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), '你好')
global sched
sched = TornadoScheduler()
# sched = BackgroundScheduler()
# sched = BlockingScheduler()
cron_rule = find_cron_rule(spider_id=spider_id)

# sched.add_job(func=aps_test, trigger='cron', second='*/5', args=(spider))
cron_rule = cron_rule.split(' ')

cron_year = cron_rule[4]

cron_mongth = cron_rule[3]
cron_day = cron_rule[2]
cron_hour = cron_rule[1]
cron_minute = cron_rule[0]
# cron_second = '*/3'
sched.add_job(func=spider_job,trigger='cron' , year=cron_year,month=cron_mongth,day=cron_day,hour=cron_hour,minute=cron_minute, args=(spider))
d = sched.get_jobs()
print(d)
sched.start()
# sched = BackgroundScheduler
# sched = TornadoScheduler(executors=executors, jobstores=jobstores)

# sched.add_job(func=my_job,trigger='cron',hour='*',minute='10',args=['spider_id'])
# sched.add_job(func=spider_job,trigger='cron',minute='*/2',args=(spider_id))
# print(1)
# sched.start()
# c = sched.get_jobs()
# print(c)
# # scheduler_start()
# print(2)