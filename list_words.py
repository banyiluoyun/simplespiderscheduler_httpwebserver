# -*-coding:utf-8-*-
from fenci import Fenci

fenci = Fenci()
# fenci.tokenization()
import pymongo

localhost = '192.168.1.127'
localport = 27017
dbname = 'pengpai_test'
client_stopword = pymongo.MongoClient(localhost, localport)
db_stopwors = client_stopword[dbname]
zik = 0
for i in db_stopwors.suncn_news_pickfromunofficial.find():
    # # print(i)
    # if i['list_word']:
    if i['strContent'] == None:
        t_list = []
    else:
        t_list = fenci.tokenization(i['strContent'])

    db_stopwors.suncn_news_pickfromunofficial.update({'_id': i['_id']}, {'$set': {'list_words': t_list}})
    zik += 1
    # print(i)
    print(i['_id'])
    print(zik)
    #     continue



