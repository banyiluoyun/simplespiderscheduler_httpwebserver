import re
str1 = '//@张怡筠：两周前我才在北京台的节目中，认识一群可爱认真的打工子弟学校的孩子们，知识给人自信，改变命运，请帮助他们继续上学！！！'
str2 = '武汉加油！中国加油！！🇨🇳🇨🇳🇨🇳🇨🇳'
str3 = '闲着没事，一定要带个话题。#武汉红十字会保安拦央视记者# //@Shannah_du:我也没啥好干的，就带个话题吧。怕热搜降下来#武汉红十字会保安拦央视记者#//@新星说:我就想问。武汉独立了吗？是不是要办签证了？'
str4 = '让智叟找路去吧 回复@ssmhp:假的!买啊 //@ssmhp:奥胶75了 //@侯宁:一定要蛋定：走愚公的道，让智叟找路去吧。'
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
            str_doing = re.findall(r"//@(.+?):", str_no)[0]
            str_doing = '//@' + str_doing + ':'
            return str_doing
        except Exception as e:
            str_doing = re.findall(r"//@(.+?)：", str_no)[0]
            str_doing = '//@' + str_doing + '：'
            return str_doing
    elif '回复@' in str_no:
        try:
            str_doing = re.findall(r"回复@(.+?):", str_no)[0]
            str_doing = '回复@' + str_doing + ':'
            return str_doing
        except Exception as e:
            str_doing = re.findall(r"回复@(.+?)：", str_no)[0]
            str_doing = '回复@' + str_doing + '：'
            return str_doing

def comment_filte(str_no):
    while True:

        str_doing = re_rule1(str_no)

        result_str = str_no.replace(str_doing, "")

        if '//@' not in result_str and '回复@' not in result_str:


            return result_str
        else:
            str_no = result_str
            continue

c= comment_filte(str4)
# print(c)