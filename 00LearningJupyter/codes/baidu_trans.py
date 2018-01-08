#/usr/bin/env python
#coding=utf8
 
#import httplib  #python2
import http.client #python3
#import md5 #python2
import hashlib
import urllib.request as ur
import random
import requests
import json


# use baidu tranlslate api 
def baidu_translate(texts):
    ''' use baidu tranlate api to translate English texts into Chinese, return list[src, dst], you can use return[0] or return[1] to choose'''
    appid = '20180104000112180'
    secretKey = 'aJNKIfe1rn6Cf4vSKUJl'
    q = texts
    if q =="":
        q = "<br>"
    httpClient = None
    myurl = '/api/trans/vip/translate'
    fromLang = 'en'
    toLang = 'zh'
    salt = random.randint(32768, 65536)
    
    sign = appid+q+str(salt)+secretKey
    m1 = hashlib.md5()
    m1.update(sign.encode(encoding="utf-8", errors='strict'))
    sign = m1.hexdigest()
    myurl = myurl+'?appid='+appid+'&q='+ur.quote(q)+'&from='+fromLang+'&to='+toLang+'&salt='+str(salt)+'&sign='+sign
    
    try:
        httpClient = http.client.HTTPConnection('api.fanyi.baidu.com')
        httpClient.request('GET', myurl)
 
        #response是HTTPResponse对象
        response = httpClient.getresponse()
        trans_result = response.read().decode('unicode-escape') # 注意转化unicode为UTF-8，结果为json
        #print(trans_result)
        src = json.loads(trans_result)['trans_result'][0]['src']
        dst = json.loads(trans_result)['trans_result'][0]['dst']
        #print(src,dst)
        return src,dst
    except Exception as e: # 如果为空，报错，返回空字符给函数返回值
        print(e)
        src = ""
        dst = ""
        return src,dst 
    finally:
        if httpClient:
            httpClient.close()

src=baidu_translate("apple egg computer")[0]
dst=baidu_translate("apple egg computer")[1]

print(src)

