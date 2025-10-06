"""
本程序仅作学习交流用途,禁止用于盈利或二次转载,若是侵犯了您的权益请联系我删除！！！
调用Api均为第三方Api,本站和第三方Api均不负责存储音频数据
CenguiguiAPI站声明:
 0请勿直接调用本站的接口，本站为演示站，仅供测试使用！！！
 1笒鬼鬼API是笒鬼鬼博客自用API接口调用服务，为降低服务器资源消耗，接口请求QPS为 10 秒 5 次
 2本站接口全部来源于网络公开数据,若是侵犯了您的权益请联系我关闭！
 3使用者务必遵循法律法规
云智Api公告:
 1为了确保公共资源得到合理利用，本站接口均已开启反爬策略(10QPS/每秒)和速率限制(85次/每分钟)，触发后系统将开启访问验证。如有更高的业务需求可以添加官方群聊购买请求资源包(十元/单个无限制)，感谢您的支持与信赖！
 2本次调用音乐解析由Cenguigui提供技术支持
"""
import requests
import webview
import requests as req
import json
from collections import defaultdict

from charset_normalizer.cli import query_yes_no

headers = {
    'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36"
}
auth = 2
error_data = {
    "code": -1,
    "data": []
}
error_json = json.dumps(error_data,indent=1,ensure_ascii=False)
q_pic_cache = defaultdict(dict)
class w:
    def __init__(self):
        #Uses Cenguigui API(api.cenguigui.cn)
        pass
    def search(self,s="11"):
        url = 防止滥用已删除,请自行通过自述了解内容
        resp = req.get(url, headers=headers)
        if resp.status_code != 200:
            print(f'[ERROR] 获取失败,{resp.status_code}')
            return error_json
        print(f'[INFO] 获取成功,{resp.status_code}')
        data = resp.json()
        if data.get('code') != 200:
            print(f'[ERROR] 获取失败,{resp.status_code}')
            return error_json
        try:
            for d in data['data']:
                d['name'] = f'{d['songname']}'
                d['artist'] = f'{d['singer']}'
                d['pic'] = 防止滥用已删除,请自行通过自述了解内容
                d['id'] = f'{d["song_rid"]}'
                for i in ["n","songname","song_rid","singer"]:
                    d.pop(i,None)
        except Exception as e:
            print(f'[ERROR] 处理返回内容时发生错误:{e}!')
            return error_json
        return json.dumps(data,ensure_ascii=False,indent=1)
    def get_url(self,rid="184847692",level:str="f"):
        level = "" if level == "f" else f"&level={level.strip()}"
        url = 防止滥用已删除,请自行通过自述了解内容
        resp = req.get(url, headers=headers)
        if resp.status_code != 200:
            print(f'[ERROR] 获取失败,{resp.status_code}')
            return error_json
        print(f'[INFO] 获取成功,{resp.status_code}')
        if not resp.json()['data']['url']:
            return error_json
        return resp.json()['data']['url']
class q:
    def __init__(self):
        # Uses [云智Api](https://api.jkyai.top/)
        pass
    def search(self,s):
        url = 防止滥用已删除,请自行通过自述了解内容
        sr = req.get(url, headers=headers)
        if sr.status_code != 200:
            print(f'[ERROR] 获取失败,{sr.status_code}')
            return error_json
        origin_data = sr.json()
        if origin_data['code'] != 200:
            print(f'[ERROR] 获取失败,{sr.status_code}')
            return error_json
        ret_data = {
            "code":200,
            "data":origin_data['data']['songs']
        }
        num = 0
        for d in ret_data['data']:
            num = num+1
            d['pic'] =防止滥用已删除,请自行通过自述了解内容
            d['id'] = num
            for i in ['number','album','source']:
                d.pop(i,None)
        #print(json.dumps(ret_data,ensure_ascii=False,indent=1))
        return json.dumps(ret_data,ensure_ascii=False,indent=1)
    def get_url(self,id,level,query):
        global q_pic_cache
        url = 防止滥用已删除,请自行通过自述了解内容
        dr = req.get(url, headers=headers)
        if dr.status_code != 200:
            print(f'[ERROR] 获取失败,{dr.status_code}')
            return ""
        down_data = dr.json()
        if down_data.get('code',-1) != 200:
            print(f'[ERROR] 返回信息解析错误,{down_data.get('code',-1)}')
            return ""
        q_pic_cache[query][id] = down_data['data']['cover']
        print(query,id)
        print(q_pic_cache[query][id])
        for format in down_data['data']['formats']:
            if format['quality'] == level:
                return format['url']
        return ""
    def get_img(self,id,query):
        print(query,id)
        print(q_pic_cache[query][id])
        try:
            return q_pic_cache[query][id]
        except:
            return 防止滥用已删除,请自行通过自述了解内容
class e:
    def __init__(self):
        # Uses Cenguigui API
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
            "Referer": "https://music.163.com/search/",
        }
        self.req = requests.session()

    def search(self,s):
        self.req.get('https://music.xxx.com/', headers=self.headers)
        url = 防止滥用已删除,请自行通过自述了解内容
        resp = self.req.get(url, headers=self.headers)
        if resp.status_code != 200:
            print(f'[ERROR] 获取失败,{resp.status_code}')
            return error_json
        d = json.loads(resp.text)
        ret_data = {
            "code":200,
            "data":d['result']['songs']
        }
        artists = ''
        for d in ret_data['data']:
            pic = False
            for artist in d['artists']:
                if not pic:
                    pic = artist['img1v1Url']
                artists = artists + artist['name'] + '&'
            if not pic:
                pic = 防止滥用已删除,请自行通过自述了解内容
            artists = artists[:-1]
            for i in ['album','artists','duration','copyrightId','status','alias','rtype','ftype','mvid','fee','rUrl','mark']:
                d.pop(i,None)
            d['artist'] = artists
            d['pic'] = pic
        return json.dumps(ret_data,ensure_ascii=False,indent=1)
    def get_url(self,id,level):
        url = 防止滥用已删除,请自行通过自述了解内容
        resp = req.get(url, headers=self.headers)
        if resp.status_code != 200:
            return ""
        return resp.json()['data']['url']
....CLASS对接
class Api:
    def search(self,msg,source):
        """
        :param msg: 搜索值
        :param source: 默认xxx
        :return: json_text json.dumps
        """
        if source == "k":
            return ...
        else:
            print('[ERROR] 不支持的歌曲源!')
            return error_json
    def get_url(self,id,source,level,query):
        """
        :param id: 歌曲ID
        :param source: 
        :return: PLAIN_TEXT PLAY_URL
        """
        if source == "kuwo":
            return xxx.get_url(id,level)
        else:
            return "不支持的音源"
    def get_img(self,id,query):
        return ....get_img(id,query)
api = Api()
#MAIN
win = webview.create_window('DEMO Music', 'music.html',width=1100, height=800,easy_drag=True,js_api=api,frameless=True)
webview.start(debug=True,private_mode=False,storage_path='D:/1newProgram/Music/cache')
