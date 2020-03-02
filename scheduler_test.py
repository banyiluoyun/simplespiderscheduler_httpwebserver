from datetime import datetime
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
import pymongo
# dict_canshu ={"year": "*", "month":'*', 'day':'*',}

cron_rule = '*/1 * * * *'
class scheduler_spider(object):
    sched = BlockingScheduler()
    text = '111111'
    def my_job(self,text):
        print('text')
    def cron_details(self,cron_rule):
        # 在2009年11月6日执行
        # self.sched.add_job(self.my_job, 'cron', run_date=datetime(2020, 3, 2, 10, 7, 1), args=['text'])
        self.sched.add_job(self.my_job, CronTrigger.from_crontab(cron_rule), args=['text'])

        # self.sched.add_job(self.my_job, 'cron',second='*',args=['text'])
        self.sched.start()

# asd = scheduler_spider()

# asd.cron_details(cron_rule)