import time
import datetime
starttime = time.time()
time.sleep(10)
endtime = time.time()
costtime = endtime - starttime

if costtime >= 3600:
    print(costtime)
else:
    print('keyiyunxing ')