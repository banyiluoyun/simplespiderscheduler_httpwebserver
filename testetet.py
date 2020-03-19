import pymongo

localhost = '127.0.0.1'
port = 27017
suncnhost = '192.168.1.127'

dbname = 'Sina'
client_host = pymongo.MongoClient(localhost,port)
client_suncn = pymongo.MongoClient(suncnhost,port)
db_host = client_host[dbname]
db_suncn = client_suncn[dbname]

numq=0
for i in db_host.suncn_news_pickfromunofficial.find(no_cursor_timeout = True):
    # print(i)
    db_suncn.suncn_news_pickfromunofficial.insert(i)
    numq +=1
    if numq % 10000 == 0:
        print(numq)