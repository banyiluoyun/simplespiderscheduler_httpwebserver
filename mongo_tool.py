import pymongo

localhost = '127.0.0.1'
port = 27017
suncnhost = '192.168.1.127'

dbname = 'Sina'
# dbname = "pengpai_test"
client_host = pymongo.MongoClient(localhost,port)
client_suncn = pymongo.MongoClient(suncnhost,port)
db_host = client_host[dbname]
db_suncn = client_suncn[dbname]

numq=0
# collection.update({"_id":1},{"$unset":{"new_field":1}})
db_suncn.suncn_news_pickfromunofficial.update({}, {'$rename': {'intcontent': "intCount"}},multi=True)

for i in db_suncn.suncn_news_pickfromunofficial.find(no_cursor_timeout=True):

    if i['intCount']:

        i['intCount'] = i['intCommentNum'] + i['intUpNum'] + i['intTranspondNum']
        db_suncn.suncn_news_pickfromunofficial.update({"_id": i['_id']}, {'$set': {'intCount': i['intCount']}})
    else:
        i['intCount'] =i['intUpNum'] + i['intTranspondNum']
        db_suncn.suncn_news_pickfromunofficial.update({"_id":i['_id']},{'$set':{'intCommentNum':0}})
        db_suncn.suncn_news_pickfromunofficial.update({"_id":i['_id']},{'$set':{'intCount':i['intCount']}})

    numq +=1
    if numq % 100000 == 0:
        print(numq)