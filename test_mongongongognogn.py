import pymongo

localhost = '192.168.1.127'
port = 27017

dbname = 'Sina'

db = pymongo.MongoClient(localhost,port)
db_colloction = db[dbname]



c = {"strId":"",
     "strNewsId":'',
     "strNewsTitle":"",
     "strPubDate":'',
"news_list":'',
"intAllSpot":'',
     "intComentNum":'',
     "beiyong1":'',
"beiyong2":'',
"beiyong3":'',
"intPositive":'',
     'intNagetive':'',
     'intNeutral':'',


     }
db_colloction.sucn_cycle_analysis.insert(c)