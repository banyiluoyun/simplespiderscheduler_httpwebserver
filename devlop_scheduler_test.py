import pymongo
localhost = '127.0.0.1'
localport = 27017
dbname = 'test_scheduler'
client_scheduler = pymongo.MongoClient(host=localhost,port=localport)
db111 = client_scheduler[dbname]
tttt = {"spider_id":"","spider_status":'',"spider_type":'','cron_rule':'','last_crawl_time':'',}
db111.scheduler.insert(tttt)