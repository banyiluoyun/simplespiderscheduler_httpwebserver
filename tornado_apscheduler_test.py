from datetime import datetime
from tornado.ioloop import IOLoop, PeriodicCallback
from tornado.web import RequestHandler, Application
from apscheduler.schedulers.tornado import TornadoScheduler
import pymongo
import os
import time
localhost = '127.0.0.1'
port = 27017
dbname = 'test_scheduler'
client_scheduler = pymongo.MongoClient(localhost,port)
db = client_scheduler[dbname]


scheduler = None
job_ids = []

# 初始化
def init_scheduler():
    global scheduler
    scheduler = TornadoScheduler()
    scheduler.start()
    print('[Scheduler Init]APScheduler has been started')

# 要执行的定时任务在这里
def task2(options):
    print('{} [APScheduler][Task]-{}'.format(datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'), options))
def task1(options):
    spider_id = options
    print(time.time())
    spider_name = db.scheduler.find_one({'spider_id': spider_id})['spider_name']
    spider_path = db.scheduler.find_one({'spider_id': spider_id})['spider_path']
    _id = db.scheduler.find_one({'spider_id': spider_id})['_id']
    os.chdir(spider_path)
    commend_spider = "scrapy runspider " + spider_name
    spider_status = '1'
    db.scheduler.update({'_id': _id}, {'$set': {'spider_status': spider_status}})
    os.system(commend_spider)
    spider_status = '0'
    db.scheduler.update({'_id': _id}, {'$set': {'spider_status': spider_status}})
    print('{} [APScheduler][Task]-{}'.format(datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'), options))
def task3(options):
    spider_id = options
    print(time.time())
    spider_name = db.scheduler.find_one({'spider_id': spider_id})['spider_name']
    spider_path = db.scheduler.find_one({'spider_id': spider_id})['spider_path']
    _id = db.scheduler.find_one({'spider_id': spider_id})['_id']
    os.chdir(spider_path)
    commend_spider = "scrapy runspider " + spider_name
    spider_status = '1'
    db.scheduler.update({'_id': _id}, {'$set': {'spider_status': spider_status}})
    os.system(commend_spider)
    spider_status = '0'
    db.scheduler.update({'_id': _id}, {'$set': {'spider_status': spider_status}})
    print('{} [APScheduler][Task]-{}'.format(datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'), options))

def find_cron_rule(spider_id):
    cron_rule = db.scheduler.find_one({'spider_id':spider_id})['cron_rule']
    return cron_rule
class MainHandler(RequestHandler):
    def get(self):
        self.write('<a href="/scheduler?job_id=1&action=add">add job</a><br><a href="/scheduler?job_id=1&action=remove">remove job</a>')
class SchedulerHandler(RequestHandler):
    def post(self):
        global job_ids
        spider_id = self.get_argument('spider_id', None)
        action = self.get_argument('action', None)
        cron_rule = find_cron_rule(spider_id)
        cron_rule = cron_rule.split(' ')
        cron_year = cron_rule[4]
        cron_month = cron_rule[3]
        cron_day = cron_rule[2]
        cron_hour = cron_rule[1]
        cron_minute = cron_rule[0]

        if spider_id:
            # add
            if 'add' == action:
                if spider_id not in job_ids:
                    job_ids.append(spider_id)
                    scheduler.add_job(task1, 'cron', year=cron_year, month=cron_month, day=cron_day, hour=cron_hour, minute=cron_minute, id=spider_id, args=(spider_id,), misfire_grace_time=30, replace_existing=True)
                    scheduler.add_job(task2, trigger='cron', minute='*/1', args=(spider_id,), misfire_grace_time=30, replace_existing=True)
                    self.write('[TASK ADDED] - {}'.format(spider_id))
                else:
                    self.write('[TASK EXISTS] - {}'.format(spider_id))
            # remove
            elif 'remove' == action:
                if spider_id in job_ids:
                    scheduler.remove_job(spider_id)
                    job_ids.remove(spider_id)
                    self.write('[TASK REMOVED] - {}'.format(spider_id))
                else:
                    self.write('[TASK NOT FOUND] - {}'.format(spider_id))
        else:
            self.write('[INVALID PARAMS] INVALID job_id or action')

class admin_scheduler(RequestHandler):
    # 查询当前任务接口
    def check_job(self, check_parse):
        if check_parse == '1':
            print(job_ids)
            job_ids2 = scheduler.get_jobs()
            print(job_ids2)
            self.write('job_ids - {}'.format(job_ids, job_ids2))
    # 一键添加全部爬虫到任务列表
    def add_all(self,add_all_parse):
        if add_all_parse == '1':
            list = ['111','112']
            for i in db.scheduler.find():
                spider_id = i['spider_id']
            # for i in list:
            #
            #     spider_id = i
                cron_rule = find_cron_rule(spider_id)
                cron_rule = cron_rule.split(' ')
                cron_year = cron_rule[4]
                cron_month = cron_rule[3]
                cron_day = cron_rule[2]
                cron_hour = cron_rule[1]
                cron_minute = cron_rule[0]
                job_ids.append(spider_id)
                scheduler.add_job(task3, trigger='cron', year=cron_year, month=cron_month, day=cron_day, hour=cron_hour, minute=cron_minute, id=spider_id, args=(spider_id,), misfire_grace_time=30, replace_existing=True)

        self.write('[TASK ADDED] all')
    # 一键删除任务列表中全部任务
    def remove_all(self,remove_all_parse):
        if remove_all_parse == '1':
            for i in job_ids:
                scheduler.remove_job(i)
                job_ids.remove(i)
            self.write('[TASK REMOVE] all')
    def post(self):
        # 开发一个查询当前任务列表中存在的爬虫任务接口，
        # 管理接口，包含，重启，添加
        check_parse = self.get_argument('check_parse')
        add_all_parse = self.get_argument('add_all_parse')
        remove_all_parse = self.get_argument('remove_all_parse')
        if add_all_parse:
            c = self.add_all(add_all_parse=add_all_parse)
        else:
            self.write('[INVALID PARAMS] INVALID add_all_parse')
        if remove_all_parse:
            d = self.remove_all(remove_all_parse=remove_all_parse)
        else:
            self.write('[INVALID PARAMS] INVALID remove_all_parse')
        if check_parse:
            e = self.check_job(check_parse)
        else:
            self.write('[INVALID PARAMS] INVALID check_parse')
if __name__ == "__main__":
    routes = [
        (r"/", MainHandler),
        (r"/scheduler/?", SchedulerHandler),
        (r"/admin", admin_scheduler),
    ]
    init_scheduler()
    app       = Application(routes, debug=True)
    app.listen(8888)
    IOLoop.current().start()