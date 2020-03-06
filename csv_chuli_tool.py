import re
import csv
import pandas as pd
import emoji
# 过滤emoji表情
def filter_emoji(desstr, restr=''):
    '''
    过滤表情
     '''
    try:
        co = re.compile(u'[\U00010000-\U0010ffff]')
    except re.error:
        co = re.compile(u'[\uD800-\uDBFF][\uDC00-\uDFFF]')
    return co.sub(restr, desstr)
def re_rule1(str_no):
    if '//@' in str_no:
        try:
            if re.findall(r"//@(.+?):", str_no):
                str_doing = re.findall(r"//@(.+?):", str_no)[0]
                str_doing = '//@' + str_doing + ':'
                return str_doing
        except Exception as e:
            if re.findall(r"//@(.+?)：", str_no):
                str_doing = re.findall(r"//@(.+?)：", str_no)[0]
                str_doing = '//@' + str_doing + '：'
                return str_doing

    elif '回复@' in str_no :
        try:
            if re.findall(r"回复@(.+?):", str_no):
                str_doing = re.findall(r"回复@(.+?):", str_no)[0]
                str_doing = '回复@' + str_doing + ':'
                return str_doing

        except Exception as e:
            if re.findall(r"回复@(.+?)：", str_no):
                str_doing = re.findall(r"回复@(.+?)：", str_no)[0]
                str_doing = '回复@' + str_doing + '：'
                return str_doing
    elif '// @' in str_no:
        try:
            if re.findall(r"//(.+?):", str_no):
                str_doing = re.findall(r"//(.+?):", str_no)[0]
                str_doing = '回复@' + str_doing + ':'
                return str_doing

        except Exception as e:
            if re.findall(r"//(.+?)：", str_no):
                str_doing = re.findall(r"//(.+?)：", str_no)[0]
                str_doing = '// @' + str_doing + ' ：'
                return str_doing

def comment_filte(str_no):
    while True:

        str_doing = re_rule1(str_no)
        # print(str_doing)
        if str_doing == None:
            result_str = str_no
            return result_str
        else:
            result_str = str_no.replace(str_doing, "")
            # print(1)

        if '//@' not in result_str :
            if '回复@' not in result_str:

                # print(result_str)
                return result_str
            else:
                str_no=result_str
        else:
            str_no = result_str
            continue


def transpond(str_tran):
    if "转发此微博" in str_tran:
        result = str_tran.split('转发此微博')[1]
        return result
    elif "转发微博" in str_tran:
        result = str_tran.split('转发微博')[1]
        return result
    elif "转发" in str_tran:
        result = str_tran.replace('转发','')
    else:
        return str_tran


date= pd.read_csv('pon_comment_score.csv',index_col=0,header=0)
df = pd.DataFrame(columns=['id','comment'])
for row in range(date.shape[0]):
    comment = date.loc[row,'comment']
    id = date.loc[row,'id']
    sentiment = date.loc[row,'sentiment']
    M_score = date.loc[row,'M_score']
    comment = str(comment)
    comment_q = filter_emoji(comment)
    cccc = comment_filte(comment_q)
    dddd = transpond(cccc)
    df = df.append({'id':id, 'comment':dddd}, ignore_index=True)
df.to_csv('./df.csv')





