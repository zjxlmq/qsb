#coding=utf-8
import requests,json
import threading
from threading import Thread
def qsb():
 while True:
    url='https://comm.ams.game.qq.com/ams/ame/amesvr?ameVersion=0.3&sServiceType=start&iActivityId=407796&sServiceDepartment=group_l&sSDID=febf9f32af4f2d90dedae9cf6d42138c&sMiloTag=AMS-MILO-407796-809290-o1666149353-1634723503687-Suu8i3&_=1634723503691'
    headers={
    'Host':'comm.ams.game.qq.com',
    'content-length':'364',
    'sec-fetch-mode':'cors',
    'origin':'https://start.qq.com',
    'user-agent':'Mozilla/5.0(Linux; Android 10;V1838A) AppleWebKit/537.36 (KHTML,like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36',
    'content-type':'application/x-www-form-urlencoded',
    'accept':'*/*',
    'sec-fetch-site':'same-site',
    'referer':'https://start.qq.com/act/a202110/index.html?viptoken=718c9adde901d1b29e08686c2a1e4737',
    'accept-encoding':'gzip,deflate,br',
    'accept-language':'zh-CN,en-US;q=0.9',
    'cookie':'填你的'
}
    data='填你的'
    k=requests.post(url=url,headers=headers,data=data).text
    print(k)
    

thread_list=[]
for i in range(2):#不要太大会被拉黑
    t=threading.Thread(target=qsb)
    t.start()
    thread_list.append(t)
for i in thread_list:
    i.join() 
    
    
    